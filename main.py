import pandas as pd
import csv
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

#Normal Distribution

df = pd.read_csv("data.csv")
data = (df["Height(Inches)"]).tolist()

#Finding Mean

HeightMean = statistics.mean(data)
HeightStdev = statistics.stdev(data)
print("Height Mean : ",HeightMean)
print("Height Stdev : ",HeightStdev)

#Sampling Distribution

def randomSetOfMean(counter):
    data_Set = []
    for i in range(0,counter):
        random_Index = random.randint(0,len(data)-1)
        value = data[random_Index]
        data_Set.append(value)
    mean = statistics.mean(data_Set)
    return mean

def showFig(mean_List):
    df = mean_List 
    mean = statistics.mean(df) 
    fig = ff.create_distplot([df], ["Height(Inches)"], show_hist=False) 
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean")) 
    fig.show()

def setUp():
    mean_List = []
    for i in range(0,1000):
        set_Of_Mean = randomSetOfMean(100)
        mean_List.append(set_Of_Mean)
    showFig(mean_List)
    mean = statistics.mean(mean_List) 
    print("Mean of sampling 1000 distribution :-",mean)
setUp()

def standard_deviation(): 
    mean_List = [] 
    for i in range(0,1000): 
        set_Of_Means= randomSetOfMean(100)
        mean_List.append(set_Of_Means) 
    std_Deviation = statistics.stdev(mean_List) 
    print("Standard deviation of 1000 sampling distribution:- ", std_Deviation) 
standard_deviation()