import argparse, random, sys
from random import choice

parser = argparse.ArgumentParser(
	description='Randomly pick n items from a list', 
	epilog='Created by Jason Bristol <Gethsemane369@gmail.com>')

parser.add_argument('num', metavar='N', type=int,     default=1, help='number of items to pick (default 1)')
parser.add_argument('-ng',              type=int,     default=1, help='number of result groups to generate (default 1)')
parser.add_argument('-i',               type=str,                help='input file of items to choose from')
parser.add_argument('-o',               type=str,                help='output file to write results to')
parser.add_argument('-u',               action='store_true',     help='force unique results')

args = parser.parse_args()

options = []

def pick(num, ngroup, input_file, output_file):
	if input_file != None:
		options = [line.strip() for line in open(input_file)]

	if not (num > 0 and num <= len(options)):
		print "\nn out of bounds, please select a number within 1 < n < total items\n"
		sys.exit(1)

	if output_file != None:
		with open('out.txt','a') as f:
			for i in random.sample(options, num): f.write(i + '\n')
	else:
		print "Picking {} individuals out of {}:".format(num, len(options))
		for i in random.sample(options, num): print i

if __name__ == "__main__": 
	pick(args.num, args.ng, args.i, args.o)
	sys.exit(0)
