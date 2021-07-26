import os
import random 
import glob
path = '/home/ngoc/ml/crnn/tts/InkData_line_processed'
x = []
for i in glob.glob(path+"/*.png"):
    x.append(i.split('/')[-1])
random.shuffle(x)
thres = int (len(x)* 0.1)
d = 0
with open(os.path.join(path,'test'),"w+") as f1, open(os.path.join(path,'train'),"w+") as f2:
    for i in x:
        if d<550: f1.write(i+'\n')
        else : f2.write(i+'\n')
        d+=1
f1.close()
f2.close()