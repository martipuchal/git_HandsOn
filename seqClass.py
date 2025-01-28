#!/usr/bin/env python


# Libs
import sys, re
from argparse import ArgumentParser

def percentage(seq): #Defining the funtion and the object of the function
    total = len(seq) #Define the total length of the sequence
    for nucleotid in ("A","T","U","C","G"): #Selecting the nucleotides from which we want to get the percentage
        if re.search(nucleotid,seq): #Searching for each one of the nucleotides in the sequence
            pct = round((seq.count(nucleotid)/total)*100,2) # Calculating the percentages
            print(f'The percentage of {nucleotid} in {seq} is {pct}%') #Printing the results of the percentages of each one of the nucleotides 




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
        percentage(args.seq)
    # RNA contains U
    elif re.search('U', args.seq) and not re.search('T',args.seq):
        print ('The sequence is RNA')
        percentage(args.seq)
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
