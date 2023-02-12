#with open("weather_data.csv") as data_file:
#   data = data_file.readlines()
#    print(data)

#import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temparatures = []
#    for row in data:
#        if row[1] != "temp":
#            temparatures.append(int(row[1]))
#    print(temparatures)

import pandas as pd

#data = pd.read_csv("weather_data.csv")
#print(type(data["temp"]))
#print(data)

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#avg_temp = sum(temp_list) / len(temp_list)
#print(round(avg_temp, 2))
#print(data["temp"].mean())
#print(data["temp"].max())

#Get Data in Columns
#print(data["condition"])
#print(data.condition)


#Get Data in Row
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day =="Monday"]
#monday_temp = int(monday.temp) 
#monday_temp_F = monday_temp * 9/5 + 32
#print(monday.condition)
#print(monday_temp_F)

#Create a dataframe form scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : ["76", "56", "65"]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
