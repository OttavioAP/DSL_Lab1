import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run():
   df = pd.read_csv('PatientData.csv')

   print(df.shape)
   mean = df.mean()

   # fill NaN values with the mean of each column
   df.fillna(mean, inplace=True)
   #print(df.loc['?'])


if __name__ == '__main__': 
   run()