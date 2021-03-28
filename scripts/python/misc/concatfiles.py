# Simple python  program to concatenate .csv files in a directory
# it will output to a single csv file with a single header

import os
import glob
import pandas as pd

os.chdir("C:/")

extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]

print(all_filenames)

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, header=0) for f in all_filenames])

# export to csv
combined_csv.to_csv("output.csv", index=False, encoding="utf-8-sig")
