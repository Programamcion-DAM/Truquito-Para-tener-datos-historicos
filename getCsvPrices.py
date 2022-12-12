import pandas as pd

close = []
openP = []
date = []
high = []
low = []

with open("preciosEURUSD.txt",'r') as f:
    for line in f.readlines():
        arr = line.split(",")
        dateHour = ""+arr[0].split(" ")[3]+" "+arr[0].split(" ")[4]
        date.append(dateHour)
        openP.append(arr[1].split(" ")[1])
        high.append(arr[2].split(":")[1])
        low.append(arr[3].split(" ")[1])
        close.append(arr[4].split(" ")[1])

df = pd.DataFrame()

df["Date"] = date
df["Open"] = openP
df["High"] = high
df["Low"] = low
df["Close"] = close
df.set_index("Date")

df.to_csv("EURUSD2012_2022.csv")
