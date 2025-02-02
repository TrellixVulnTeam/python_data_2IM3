import numpy as np
import pandas as pd

df = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(df)
print(df)
print(df.dropna(axis=1))
print(df.dropna())
print(df.dropna(thresh=2))
print(df.fillna(value='FILL VALUE'))
print(df)
print(df['A'].fillna(value=df['A'].mean()))
quit()
