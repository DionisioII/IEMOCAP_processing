import csv
import sys

if  len(sys.argv) !=2:
    print("a csv file for import is needed as command line argument")
    sys.exit()

filename = str(sys.argv[1])
filename_output_csv = "trimmed_output/"+filename[7:]


with open(filename, 'r') as inp, open(filename_output_csv, 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if len(row) >167 and row[168]!= 'xxx':
            
            writer.writerow(row[2:-3])