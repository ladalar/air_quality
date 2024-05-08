# pip install pandas
import pandas as pd
df = pd.read_csv('air_quality.csv')

def distance(x1, y1, x2, y2):
    a = abs(x2-x1)
    b = abs(y2-y1)
    dist = (a*a+b*b)**0.5
    return dist

distt = distance(1,5,1,2)
a1 = df.iloc[0, 6]
b1 = df.iloc[0, 7]
print(b1)
distt = distance(a1,b1,118,30)
print(distt)
