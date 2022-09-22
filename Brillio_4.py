"""
Brillio 4th Interview 22-9-22

"""
import glob
import time
import pandas as pd


df = pd.DataFrame()
ls = list(range(0, 100))
df["col1"] = ls

df["col"] = df["col"].to_list()[::-1]


def fun():
    count = 0
    while count < 10:
        file = glob.glob("../file.txt")

        if len(file) > 1:
            data = open(file[0]).read()
            nums = [int(i) for i in data.split(' ')]
            return sum(nums)
        else:
            count += 1
            time.sleep(60)

    return "File not created in last 10 minutes"
