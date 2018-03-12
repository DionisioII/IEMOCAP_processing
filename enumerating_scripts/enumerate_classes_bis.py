import os
import csv

dictionary = {"hap" : 0, "sad": 0 , "neu" : 0, "ang": 0,"xxx":0,"oth":0, "fru":0, "sur":0,"exc":0,"dis":0, "fea" : 0}

dictionary_coherent ={"hap" : 0, "sad": 0 , "neu" : 0, "ang": 0,"xxx":0,"oth":0, "fru":0, "sur":0,"exc":0,"dis":0, "fea" : 0}
directory = os.fsencode("emo_evaluations/")



filename = "Slim_unique_csv_NaN_Removed.csv"
with open(filename, 'r') as inp:
   
    inp.readline()

    for row in csv.reader(inp):

        video_class = row[166]
        dictionary[video_class] +=1
inp.close()

print(dictionary)
        

        