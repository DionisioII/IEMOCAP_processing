from decimal import Decimal


def create_classification_array(filename,classifications):
    fh = open('emo_evaluations/'+ filename[11:])


    while True:
        # read line
        line = fh.readline()
        
        if line[:1] == "[" :
           
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
            classifications.append(dict)
               
        
        # check if line is not empty
        if not line:
            break
    fh.close()
    return classifications;


def check_range_time(frame_time,classifications):
        
    result = []
    for class_range in classifications:
        if frame_time >= class_range['start_time'] and frame_time <= class_range['end_time']:
            result.append(class_range["video_name"])
            result.append(class_range["class"])
            result.append(class_range["valence"])
            result.append(class_range["activation"])
            result.append(class_range["dominance"])
            break
    
    return result


def average_values(values,count):
    if count != Decimal(0):
        average_values = [x / count for x in values[:-2]]
        average_values.append(values[165]) #video_name
        average_values.append(values[166]) #class

        return average_values;
    return values