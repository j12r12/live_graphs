import pandas as pd
import time
import random

df = pd.DataFrame(columns=["X1", "Y1", "Y2"])

i = 1

while i < 100:
       df = df.append(dict(zip(df.columns, [i+1, random.random(), random.random()])), ignore_index=True)
       i+=1
       df.to_csv("Animation_Test.csv")
       time.sleep(1)




