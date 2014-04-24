import argparse, random, sys
from random import choice

parser = argparse.ArgumentParser(
	description='Randomly pick n items from a list',
	epilog='Created by Jason Bristol <Gethsemane369@gmail.com>')
parser.add_argument('-n', type=int, default=1,
                   help='a number of items to pick within 1 < n < total items')
parser.add_argument('-i', help='open an input file of items to choose from')
parser.add_argument('-o', help='write results to an output file')

args = parser.parse_args()

options = []

if args.i != None:
	options = [line.strip() for line in open(args.i)]

if args.n > 0 and args.n <= len(options):
	if args.o != None:
		with open('out.txt','a') as f:
			for i in random.sample(options, args.n): f.write(i + '\n')
	else:
		print "Picking " + repr(args.n) + " individuals out of " + repr(len(options)) + ":"
		for i in random.sample(options, args.n): print i
else:
	print "n out of bounds, please select a number within 1 < n < total items"

sys.exit()