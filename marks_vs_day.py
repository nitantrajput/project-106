import csv
import plotly.express as px
import numpy as np

x = []
y = []
with open ('marks_vs_days.csv')as f:
    df = csv.DictReader(f)
    for row in f:
        x.append(float(row['Marks In Percentage']))
        y.append(float(row['Days Present']))
    print('x & y are appendent')
    plot = px.scatter(df , x = 'Marks In Percentage' , y = 'Days Present')
    #plot.show()

    correlation = np.correlate(x , y)
    print(correlation)
#close to -1 , 1 , 0 
