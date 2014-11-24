#!/usr/bin/env python

__author__  = 'Jason Bristol'
__version__ = '1.5'

import argparse, random, sys, codecs
from pypicker_exceptions import *

parser = argparse.ArgumentParser(
  description='Randomly pick n items from a list', 
  epilog='Created by Jason Bristol <Gethsemane369@gmail.com>')

parser.add_argument('n',   metavar='N', type=int, nargs='?', default=1, help='number of items to pick (default 1)')
parser.add_argument('i',   metavar='I', type=str,                       help='input file of items to choose from')
parser.add_argument('-ng',              type=int,            default=1, help='number of result groups to generate (default 1)')
parser.add_argument('-o',               type=str,                       help='output file to write results to')
parser.add_argument('-j',               type=str,                       help='join results using specified delimeter')
parser.add_argument('-v',               action='store_true',            help='verbose output')
parser.add_argument('-u',               action='store_true',            help='force uniqueness across result groups')

args = parser.parse_args()

options      = []      # Items to choose from
resultString = []      # Array of result strings
sampleSize   = [0, 0]  # [<num_picked>, <num_total>]

''' Validates and orchestrates result picks '''
def pick(n, num_groups, input_file, output_file, verbose, join, unique_groups):

  if n not in range(0, len(options)): raise BoundsException("n out of bounds, please select a number within 1 <= n <= total items")

  sampleSize[1] = len(options)

  for i in range(0, num_groups):
    results   = random.sample(options, n)
    sampleStr = (sampleSize[1] - sampleSize[0]) if unique_groups else sampleSize[1]

    if unique_groups:
      if (n * num_groups) > sampleSize[1]: raise ResultSetException("Requested result set is larger than sample size")
      else:
        for result in results: options[:] = [x for x in options if x != result]
    
    if verbose: resultString.append("Picking {} item(s) out of {}:".format(n, sampleStr))
    resultString.append("\n".join(results) if join == None else "{} ".format(join).join(results))

    sampleSize[0] += n

  if output_file == None: print "\n\n".join(resultString)
  else:
    try:
      with codecs.open(output_file,'w', 'utf-8') as f: f.write("\n\n".join(resultString))
    except:  raise OutputException(sys.exc_info[1])
    finally: f.close

''' Main Method '''     
if __name__ == "__main__":
  try:
    options = [line.strip() for line in codecs.open(args.i, 'r', 'utf-8')]
    pick(args.n, args.ng, args.i, args.o, args.v, args.j, args.u)
  except BoundsException      as e: print "\n{}: {}\n".format(type(e).__name__, e.msg)
  except OutputException      as e: print "\n{}: {}\n".format(type(e).__name__, e.msg)
  except ResultSetException   as e: print "\n{}: {}\n".format(type(e).__name__, e.msg)
  except                          : print "\n{}: {}\n".format("Unexpected error", sys.exc_info()[1])
  finally                         : sys.exit(0)
