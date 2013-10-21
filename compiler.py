from preprocessor import *
from tokenizer import *

import sys

env = {}

filename = sys.argv[1]

with open( filename ) as f:
	program = f.read()

program = preprocess( program, env )
print program

program = tokenize( program )
print program

