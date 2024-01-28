import sys

import pandas as pd

print(sys.argv)

# arg 0 is the name of the file
# arg #1 is whatever user put on
day = sys.argv[1]

# some fancy stuff with pandas
# docker run -it test:pandas 2024-01-21
# run docker w/ date arg

print(f'job finished successfully for day = {day}')