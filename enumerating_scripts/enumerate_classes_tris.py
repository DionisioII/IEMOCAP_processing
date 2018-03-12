import os
import csv

dictionary = {"hap" : 0, "sad": 0 , "neu" : 0, "ang": 0,"xxx":0,"oth":0, "fru":0, "sur":0,"exc":0,"dis":0, "fea" : 0}

dictionary_coherent ={"hap" : 0, "sad": 0 , "neu" : 0, "ang": 0,"xxx":0,"oth":0, "fru":0, "sur":0,"exc":0,"dis":0, "fea" : 0}
videos= set()
directory = os.fsencode("output/")

for file in sorted(os.listdir(directory)):

    filename = os.fsdecode(file)



    with open("output/"+filename, 'r') as inp, open("chunk.txt", 'a') as vid:
        
        if filename.endswith(".csv"): 

            inp.readline()

            for row in csv.reader(inp):
                if len(row)>168 and row[167] not in videos:
                    print(row[167])
                    vid.write(row[167]+ " " + row[168] +"\n")
                    videos.add(row[167])
                    video_class = row[168]
                    dictionary[video_class] +=1
                else:
                    pass
        vid.close()
        inp.close()
            


print(dictionary)
        # {'hap': 595, 'sad': 1084, 'neu': 1708, 'ang': 1103, 'xxx': 2507, 'oth': 3, 'fru': 1849, 'sur': 107, 'exc': 1041, 'dis': 2, 'fea': 40}
       #tris {'hap': 573, 'sad': 1072, 'neu': 1661, 'ang': 1061, 'xxx': 2416, 'oth': 3, 'fru': 1781, 'sur': 101, 'exc': 998, 'dis': 2, 'fea': 39}

        #bis {'hap': 552, 'sad': 1060, 'neu': 1664, 'ang': 1063, 'xxx': 0, 'oth': 0, 'fru': 0, 'sur': 0, 'exc': 0, 'dis': 0, 'fea': 0}