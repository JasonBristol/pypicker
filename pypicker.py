#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = 1.0

import argparse
import random

parser = argparse.ArgumentParser(
    description='Randomly pick items from a list',
    epilog='Created by Jason Bristol <json.bristol@gmail.com>')

parser.add_argument('n',
                    metavar='SAMPLE SIZE',
                    nargs='?',
                    type=int,
                    default=1,
                    help="number of items to pick (default: %(default)s)")
parser.add_argument('list',
                    metavar='SAMPLE GROUP',
                    nargs='*',
                    type=str,
                    default=[],
                    help="list of items to choose from.")
parser.add_argument('-i',
                    metavar='PATH',
                    type=argparse.FileType('r'),
                    help="input file of items to choose from")
parser.add_argument('-g',
                    metavar='INTEGER',
                    type=int,
                    default=1,
                    help="number of result groups to generate (default: %(default)s)")
parser.add_argument('-o',
                    metavar='PATH',
                    type=argparse.FileType('w'),
                    help="output file to write results to")
parser.add_argument('-j',
                    metavar='DELIMITER',
                    type=str,
                    help="join results using specified delimiter")
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help="verbose output")
parser.add_argument('-u', '--unique',
                    action='store_true',
                    help="force uniqueness across result groups")
parser.add_argument('--version',
                    action='version',
                    version='%(prog)s {version}'.format(version=__version__))

args = parser.parse_args()


class PyPickerException(Exception):
    """ This is the base PyPicker error class """
    pass


class BoundsException(PyPickerException):
    """ This error occurs when the n argument is out of bounds """

    def __init__(self, msg):
        self.msg = str(msg)


class OutputException(PyPickerException):
    """ This error occurs when the output file cannot be written to """

    def __init__(self, msg):
        self.msg = str(msg)


class ResultSetException(PyPickerException):
    """ This error occurs when the requested result set is greater than the sample size """

    def __init__(self, msg):
        self.msg = str(msg)


def SimpleRandomSample(sample_set, sample_size):
    """
    A simple random sample is a sample in which every member of the population has an equal chance of being chosen.
    :param sample_set: set of values to select from
    :param sample_size: number of values to select
    :return: result sample
    """
    return random.sample(sample_set, sample_size)


def pick(n, num_groups, sample_set, output_file, verbose, join, unique_groups):
    """
    Validates and orchestrates result picks
    :param n: number of values to pick
    :param num_groups: number of samples to pick
    :param sample_set: set of values to choose from
    :param output_file: path to output file
    :param verbose: set verbosity
    :param join: join the result with a delimiter
    :param unique_groups: set uniqueness
    :return:
    """
    resultString = []  # Array of result strings
    sampleSize = [0, 0]  # [<num_picked>, <num_total>]

    if n not in range(0, len(sample_set) + 1):
        raise BoundsException("n out of bounds, please select a number within 1 <= n <= total items")

    sampleSize[1] = len(sample_set)

    for i in range(0, num_groups):
        results = SimpleRandomSample(sample_set, n)

        sampleStr = (sampleSize[1] - sampleSize[0]) if unique_groups else sampleSize[1]

        if unique_groups:
            if (n * num_groups) > sampleSize[1]:
                raise ResultSetException("Requested result set is larger than sample size")
            else:
                for result in results:
                    sample_set[:] = [x for x in sample_set if x != result]

        if verbose:
            resultString.append("Picking {} item(s) out of {}:".format(n, sampleStr))

        resultString.append("\n".join(results) if join is None else "{}".format(join).join(results))

        sampleSize[0] += n

    if output_file == None:
        print("\n\n".join(resultString))
    else:
        try:
            output_file.write("\n\n".join(resultString))
        except Exception as e:
            raise OutputException(e)


if __name__ == "__main__":
    sample_set = args.list if args.i is None else [line.strip() for line in args.i.readlines()]
    random.shuffle(sample_set)
    pick(args.n, args.g, sample_set, args.o, args.verbose, args.j, args.unique)
