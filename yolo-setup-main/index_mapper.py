import pandas as pd
df = pd.read_csv('predictions.csv')
df = df[["Index"]]
print(df.Index)
variables = ['bread waste', 'banana peel']

extra = []
for i in range(len(df)):
    if df.Index[i] == 0:
        print(variables[0])
        extra.append(variables[0])
    if df.Index[i] == 1:
        print(variables[1])
        extra.append(variables[1])

df.insert(1,"Label",extra)

print(df)

df.to_csv("labels.csv")
