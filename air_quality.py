# pip install pandas
import pandas as pd
# df = pd.read_csv('air_quality.csv')

def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    total_minutes = hours * 60 + minutes
    return total_minutes

df['Time_in_minutes'] = df['Time'].apply(lambda x: time_to_minutes(x))

def distance(x1, y1, x2, y2):
    a = abs(x2-x1)
    b = abs(y2-y1)
    dist = (a*a+b*b)**0.5
    return dist

def aqi_from_temperature():
    temperature = float(input("Please enter the temperature: "))
    aqi_temp = -0.292366632068841 * temperature * temperature + 9.84969164097354 * temperature - 32.1722464255989
    print(aqi_temp)

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

# aqi_dist = (dist2 + dist3) / (dist1 + dist2 + dist3) * AQI1 + (dist1 + dist3) / (dist1 + dist2 + dist3) * AQI2 + (dist1 + dist2) / (dist1 +dist2 + dist3) * AQI3
# aqi2 = 0.2*aqi_temp+0.8*aqi_dist
# print(aqi2)
