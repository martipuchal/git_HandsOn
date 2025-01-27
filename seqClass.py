#!/usr/bin/env python


# Libs
import sys, re
from argparse import ArgumentParser

# Arguments 
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
# Save the information relative to the arguments passed
args = parser.parse_args()

# Sequence to upper
args.seq = args.seq.upper()
# Ensure only ACTG are used to build the sequence
if re.search('^[ACGTU]+$', args.seq):
    # DNA contains T
    if re.search('T', args.seq) and not re.search('U',args.seq): 
        print ('The sequence is DNA')
    # RNA contains U
    elif re.search('U', args.seq) and not re.search('T',args.seq):
        print ('The sequence is RNA')
    # If T and U are detected the sequence is incorrect
    elif re.search('U',args.seq) and re.search('T',args.seq):
        print ('The sequence is not DNA nor RNA')
    # For not having T nor U
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Patter finding function
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("We FOUND it")
    else:
        print("NOT FOUND")
