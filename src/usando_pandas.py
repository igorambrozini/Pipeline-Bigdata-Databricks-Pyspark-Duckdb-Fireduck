import pandas as pd
from multiprocessing import Pool, cpu_count
from tqmd import tqmd # progress bar

CONCURRENCY = cpu_count()

total_linhas = 1_000_000_000 # total lines
chunksize = 100_000_000 # chunk size
filename = 'data/measurements_1000000000.txt' # file path

