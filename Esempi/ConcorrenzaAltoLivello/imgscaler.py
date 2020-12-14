#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 andreaerk <andreaerk@andreaerk>
#
# Distributed under terms of the MIT license.

"""

"""

from collections import namedtuple
from multiprocessing import JoinableQueue, Queue, Process
import os
import sys
import math
from PIL import Image, UnidentifiedImageError


Result = namedtuple("Result", "copied scaled name")
Summary = namedtuple("Summary", "todo copied scaled canceled")

def main():
    size, smooth, source, target, concurrency = handle_commandline()
    print("Starting...")
    summary = scale(size, smooth, source, target, concurrency)
    summarize(summary, concurrency)

def handle_commandline():
    argomenti = (int(sys.argv[1]), bool(sys.argv[2]), sys.argv[3], sys.argv[4], int(sys.argv[5]))
    
    return argomenti

def scale(size, smooth, source, target, concurrency):
    canceled = False
    jobs = JoinableQueue()
    results = Queue()

    create_processes(size, smooth, jobs, results, concurrency)
    todo = add_jobs(source, target, jobs)

    try:
        jobs.join()
    except KeyboardInterrupt:
        print("Interrotto dall'utente")
        canceled = True

    copied = scaled = 0 # contatore per quante immaggini sono state scalate e quante copiate

    while not results.empty():
        result = results.get_nowait()
        copied += result.copied
        scaled += result.scaled
    return Summary(todo, copied, scaled, canceled)

def create_processes(size, smooth, jobs, results, concurrency):
    # per ogni core
    for _ in range(concurrency):
        process = Process(target=worker, args=(size, smooth, jobs, results))
        process.daemon = True
        process.start()

def worker(size, smooth, jobs, results):
    while True:
        try:
            sourceImage, targetImage = jobs.get()
            try:
                result = scale_one(size, smooth, sourceImage, targetImage)
                print("{} {}".format("copied" if result.copied else "sclaed", os.path.basename(result.name)))
                results.put(result)
            except UnidentifiedImageError as err:
                print(str(err))
        finally:
            jobs.task_done()

def add_jobs(source, target, jobs):
    for todo, name in enumerate(os.listdir(source), start=1):
        sourceImage = os.path.join(source, name)
        targetImage = os.path.join(target, name)
        jobs.put((sourceImage, targetImage))
    return todo

def scale_one(size, smooth, sourceImage, targetImage):
    oldImage = Image.open(sourceImage)
    if oldImage.width <= size and oldImage.height <= size:
        oldImage.save(targetImage)
        return Result(1, 0, targetImage)
    else:
        if smooth:
            scaling = min(size / oldImage.width, size / oldImage.height)
            newImage = oldImage.thumbnail((scaling, scaling), Image.ANTIALIAS)
        else:
            stride = int(math.ceil(max(oldImage.width / size, oldImage.height / size)))
            newImage = oldImage.subsample(stride)
        newImage.save(targetImage)
        return Result(0, 1, targetImage)

def summarize(summary, concurrency):
    message = "copied  {} scaled {}".format(summary.copied, summary.scaled)
    difference = summary.todo - (summary.copied + summary.scaled)
    if difference:
        message += "skipped {}".format(difference)
    message += "using {} processes".format(concurrency)
    if summary.canceled:
        message + " [canceled]"
    print(message)


if __name__ == "__main__":
    main()
