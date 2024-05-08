# pip install pandas
import pandas as pd
# df = pd.read_csv('air_quality.csv')

def distance(x1, y1, x2, y2):
    a = abs(x2-x1)
    b = abs(y2-y1)
    dist = (a*a+b*b)**0.5
    return dist

def aqi_from_temperature():
    temperature = float(input("Please enter the temperature: "))
    aqi = -0.292366632068841*temperature*temperature+9.84969164097354*temperature-32.1722464255989
    print(aqi)

def distToSens(x,y):
    loc1 = (33.9, -117.51,)
    loc2 = (33.92, -117.44)
    loc3 = (33.92, -117.51)
    dsens = [None]*3
    dsens[0] = distance(x,y,loc1[0],loc1[1])
    dsens[1] = distance(x,y,loc2[0],loc2[1])
    dsens[2] = distance(x,y,loc3[0],loc3[1])

    return dsens
    

x = distToSens(1,1)
print(x)
