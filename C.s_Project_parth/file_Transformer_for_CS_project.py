import pickle
import sys

def content_data(file):
    with open(file,'rb') as f:
        L=pickle.load(f)
    return L
L=content_data('save1.bat')
if L[0] == (700,700):
    L.pop(0)
    NL=[]
    NL.append((700,700))
    for tup,owjuo in L:
        i=tup[0]
        j=tup[1]
        ni=i+100
        nj=j+100
        NL.append(((ni,nj),owjuo))
    with open('save1.bat','wb') as f:
        pickle.dump(NL,f)
else:
    print('error file cordinates is correct')
sys.exit()  

