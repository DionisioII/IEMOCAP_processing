import os

dictionary = {"hap" : 0, "sad": 0 , "neu" : 0, "ang": 0,"xxx":0,"oth":0, "fru":0, "sur":0,"exc":0,"dis":0, "fea" : 0}

dictionary_coherent ={"hap" : 0, "sad": 0 , "neu" : 0, "ang": 0,"xxx":0,"oth":0, "fru":0, "sur":0,"exc":0,"dis":0, "fea" : 0}
directory = os.fsencode("emo_evaluations/")

for file in sorted(os.listdir(directory)):


    filename = os.fsdecode(file)

    if filename.endswith(".txt"): 
        print ("processing file : " + filename)

        fh = open("emo_evaluations/"+filename)
        
        while True:
        # read line
            line = fh.readline()
            
            if line and line[0] == "[" :
                #print(line[0])
                words = line.split()
            

                dict = {
                    "start_time": float(words[0].replace("[", "")),
                    "end_time": float(words[2].replace("]", "")),
                    "video_name":words[3],
                    "class": words[4],
                    "valence": float(words[5].replace("[", "").replace(",","")),
                    "activation": float(words[6].replace(",","")),
                    "dominance": float(words[7].replace("]", ""))

                }
                dictionary[dict["class"]] += 1
                video_string_array = dict['video_name'].split("_")
                
                if len(video_string_array) == 3:
                    if video_string_array[0][-1] == video_string_array[2][0]: #or words[0][-1] ==  words[3][0]:
                        dictionary_coherent[dict["class"]] += 1
                
                elif len(video_string_array) == 4:
                    if video_string_array[0][-1] ==  video_string_array[3][0]:
                        dictionary_coherent[dict["class"]] += 1
                
            
            # check if line is not empty
            if not line:
                break
        fh.close()

print(dictionary)
print(dictionary_coherent)

        