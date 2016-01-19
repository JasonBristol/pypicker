#!/usr/bin/env python

__author__  = 'Jason Bristol'
__version__ = '2.1'

import argparse, random, sys, codecs, itertools
from pypicker_exceptions import *

parser = argparse.ArgumentParser(
  description='Randomly pick n items from a list', 
  epilog='Created by Jason Bristol')

parser.add_argument('n',   metavar='N', type=int, nargs=1,                           default=1,     help='number of items to pick (default 1)')
parser.add_argument('i',   metavar='I', type=str, nargs=1,                                          help='input file of items to choose from')
parser.add_argument('-ng',              type=int,                                    default=1,     help='number of result groups to generate (default 1)')
parser.add_argument('-o',               type=str,                                                   help='output file to write results to')
parser.add_argument('-j',               type=str,                                                   help='join results using specified delimeter')
parser.add_argument('-v',               action='store_true',                                        help='verbose output')
parser.add_argument('-u',               action='store_true',                                        help='force uniqueness across result groups')
parser.add_argument('-sa',              type=str, choices=('SRS','SYS','CLS','STS'), default='SRS', help='specifies the sampling algorithm to use (default SRS)')

args = parser.parse_args()

options      = []      # Items to choose from
resultString = []      # Array of result strings
sampleSize   = [0, 0]  # [<num_picked>, <num_total>]

# Functions

# SRS
#
# A simple random sample is a sample in which every member of the population has an equal chance of being chosen.
def SimpleRandomSample(n):
  return random.sample(options, n)

# SYS
#
# In systematic sampling, every kth member of the population is chosen for the sample, with value of k 
# being approximately N/n (N: # in population; n: # of samples) '''
def SystematicSample(n):
  k = len(options) / n
  results = []

  for i in xrange(0, n):
    results.append(options[k * (i + 1)])

  return results

# CLS
#
# A cluster sample is a simple random sample of groups, or clusters, of a population. Each member of the 
# chosen clusters would be part of the final sample.
def ClusterSample(n):
  # r = random.randint(2, len(options))
  # d = random.randint(1, (len(options) / 4))
  # clusters = []
  # results  = []

  # for i in xrange(0, r):
  #   clusters.append(split_list(options))

  # for _ in itertools.repeat(None, d):
  #   random.shuffle(clusters)
  #   clusters.pop()

  # for i in xrange(0, n):
  #   cluster = random.randint(0, len(clusters))
  #   element = random.randint(0, len(clusters[cluster]))
  #   results.append(clusters[cluster][element])

  # return results
  return

# STS
#
# A stratified sample is obtained by dividing the population into mutually exclusive groups, or strata, 
# and randomly sampling from each of these groups.
def StratifiedSample(n):
  return

# Helper function to split a list in half
def split_list(a_list):
  half = len(a_list) / 2
  return a_list[:half], a_list[half:]

# Validates and orchestrates result picks
def pick(n, num_groups, input_file, output_file, verbose, join, unique_groups, algorithm):

  if n not in xrange(0, len(options)): raise BoundsException("n out of bounds, please select a number within 1 <= n <= total items")

  sampleSize[1] = len(options)

  for i in xrange(0, num_groups):
    if   algorithm == 'SRS': results = SimpleRandomSample(n)
    elif algorithm == 'SYS': results = SystematicSample(n)
    elif algorithm == 'CLS': results = ClusterSample(n)
    elif algorithm == 'STS': results = StratifiedSample(n)

    sampleStr = (sampleSize[1] - sampleSize[0]) if unique_groups else sampleSize[1]

    if unique_groups:
      if (n * num_groups) > sampleSize[1]: raise ResultSetException("Requested result set is larger than sample size")
      else:
        for result in results: options[:] = [x for x in options if x != result]
    
    if verbose: resultString.append("Picking {} item(s) out of {}:".format(n, sampleStr))
    resultString.append("\n".join(results) if join == None else "{}".format(join).join(results))

    sampleSize[0] += n

  if output_file == None: print "\n\n".join(resultString)
  else:
    try:
      with codecs.open(output_file,'w', 'utf-8') as f: f.write("\n\n".join(resultString))
    except:  raise OutputException(sys.exc_info[1])
    finally: f.close

# Main Method     
if __name__ == "__main__":
  try:
    options = [line.strip() for line in codecs.open(args.i, 'r', 'utf-8')]
    random.shuffle(options)
    pick(args.n, args.ng, args.i, args.o, args.v, args.j, args.u, args.sa)
  except BoundsException      as e: print "\n{}: {}\n".format(type(e).__name__, e.msg)
  except OutputException      as e: print "\n{}: {}\n".format(type(e).__name__, e.msg)
  except ResultSetException   as e: print "\n{}: {}\n".format(type(e).__name__, e.msg)
  except                          : print "\n{}: {}\n".format("Unexpected error", sys.exc_info()[1])
