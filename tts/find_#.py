import os
path = '/home/ngoc/ml/crnn/tts/InkData_line_processed'
re = os.listdir(path)
for i in re:
    if i.endswith(".txt"):
        with open(path+'/'+i,'r+') as f:
            label = f.read()
            if '#' in label:
                print(i)
            f.close()