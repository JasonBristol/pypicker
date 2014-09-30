#!/usr/bin/env python

__author__  = 'Jason Bristol'
__version__ = '1.0'

import argparse, random, sys
from pypicker_exceptions import *

parser = argparse.ArgumentParser(
	description='Randomly pick n items from a list', 
	epilog='Created by Jason Bristol <Gethsemane369@gmail.com>')

parser.add_argument('n',   metavar='N', type=int,   default=1,   help='number of items to pick (default 1)')
parser.add_argument('i',   metavar='I', type=str,                help='input file of items to choose from')
parser.add_argument('-ng',              type=int,   default=1,   help='number of result groups to generate (default 1)')
parser.add_argument('-o',               type=str,                help='output file to write results to')
parser.add_argument('-j',               type=str,                help='join results using specified delimeter')
parser.add_argument('-v',               action='store_true',     help='verbose output')
parser.add_argument('-u',								action='store_true',		 help='force uniqueness across result groups')

args = parser.parse_args()

options      = []
resultString = []
sampleSize   = 0

''' Validates and orchestrates result picks '''
def pick(n, num_groups, input_file, output_file, verbose, join, unique_groups):

	if n not in range (0, len(options)): raise BoundsException("n out of bounds, please select a number within 1 <= n <= total items\n")

	sampleSize = len(options)

	for i in range(0, num_groups):
		results = random.sample(options, n)

		if unique_groups:
			if (n * num_groups) > sampleSize: raise ResultSetException("Requested result set is larger than sample size\n")
			else:
				for result in results:
					while result in options:
						options.remove(result)

		if verbose: resultString.append("\nPicking {} individuals out of {}:".format(n, len(options) + n))
		resultString.append("\n".join(results) if join == None else "{} ".format(join).join(results))

	if output_file == None: print '\n'.join(resultString)
	else:
		try:
			with open(output_file,'w') as f:
				f.write('\n'.join(resultString))
		except:  raise OutputException(sys.exc_info[0])
		finally: f.close

''' Main Method '''			
if __name__ == "__main__":
	try:
		options = [line.strip() for line in open(args.i)]
		pick(args.n, args.ng, args.i, args.o, args.v, args.j, args.u)
	except BoundsException      as e: print "\n{}: {}".format(type(e).__name__, e.msg)
	except OutputException 	    as e: print "\n{}: {}".format(type(e).__name__, e.msg)
	except ResultSetException   as e: print "\n{}: {}".format(type(e).__name__, e.msg)
	except                          : print "\n{}: {}".format("Unexpected error", sys.exc_info()[0])
	finally                         : sys.exit(0)
