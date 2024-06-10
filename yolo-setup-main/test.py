import os
import pandas as pd
dir= 'D:/Desktop Loki/yolo_proto_5/runs/detect/'
files = []
rng = len(os.listdir('D:/Desktop Loki/yolo_proto_5/runs/detect/'))


for i in range(2,rng):
    txts=os.listdir(dir+f'predict{i}'+'/labels')
    print(txts)
    try:
        files.append(dir+f'predict{i}'+'/labels/'+txts[0])
    except:
        pass

print(files)

data = []
for file in files:
    with open(file,'r') as fh:
        temp_txt = fh.readlines()
    for i in temp_txt:
        row = i.split()
        data.append(row)
    #for i in temp_txt:
        
print(len(data))

columns=['Index','left','right','top','bottom']
df = pd.DataFrame(data,columns=columns )
df.to_csv('predictions.csv',index=False)
