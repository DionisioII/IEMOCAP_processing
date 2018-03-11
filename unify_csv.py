import csv
import sys
from pathlib import Path

if  len(sys.argv) !=2:
    print("a csv file for import is needed as command line argument")
    sys.exit()



filename = str(sys.argv[1])
filename_output_csv = "Slim_unique_csv_NaN_Removed.csv"

my_file = Path("Slim_unique_csv_NaN_Removed.csv")
if my_file.is_file() == False:
    d= ["CH1_X1","CH1_Y1","CH1_Z1","CH2_X2","CH2_Y2","CH2_Z2","CH3_X3","CH3_Y3","CH3_Z3","FH1_X4","FH1_Y4","FH1_Z4","FH2_X5","FH2_Y5","FH2_Z5","FH3_X6","FH3_Y6","FH3_Z6","LC1_X7","LC1_Y7","LC1_Z7","LC2_X8","LC2_Y8","LC2_Z8","LC3_X9","LC3_Y9","LC3_Z9","LC4_X10","LC4_Y10","LC4_Z10","LC5_X11","LC5_Y11","LC5_Z11","LC6_X12","LC6_Y12","LC6_Z12","LC7_X13","LC7_Y13","LC7_Z13","LC8_X14","LC8_Y14","LC8_Z14","RC1_X15","RC1_Y15","RC1_Z15","RC2_X16","RC2_Y16","RC2_Z16","RC3_X17","RC3_Y17","RC3_Z17","RC4_X18","RC4_Y18","RC4_Z18","RC5_X19","RC5_Y19","RC5_Z19","RC6_X20","RC6_Y20","RC6_Z20","RC7_X21","RC7_Y21","RC7_Z21","RC8_X22","RC8_Y22","RC8_Z22","LLID_X23","LLID_Y23","LLID_Z23","RLID_X24","RLID_Y24","RLID_Z24","MH_X25","MH_Y25","MH_Z25","MNOSE_X26","MNOSE_Y26","MNOSE_Z26","LNSTRL_X27","LNSTRL_Y27","LNSTRL_Z27","TNOSE_X28","TNOSE_Y28","TNOSE_Z28","RNSTRL_X29","RNSTRL_Y29","RNSTRL_Z29","LBM0_X30","LBM0_Y30","LBM0_Z30","LBM1_X31","LBM1_Y31","LBM1_Z31","LBM2_X32","LBM2_Y32","LBM2_Z32","LBM3_X33","LBM3_Y33","LBM3_Z33","RBM0_X34","RBM0_Y34","RBM0_Z34","RBM1_X35","RBM1_Y35","RBM1_Z35","RBM2_X36","RBM2_Y36","RBM2_Z36","RBM3_X37","RBM3_Y37","RBM3_Z37","LBRO1_X38","LBRO1_Y38","LBRO1_Z38","LBRO2_X39","LBRO2_Y39","LBRO2_Z39","LBRO3_X40","LBRO3_Y40","LBRO3_Z40","LBRO4_X41","LBRO4_Y41","LBRO4_Z41","RBRO1_X42","RBRO1_Y42","RBRO1_Z42","RBRO2_X43","RBRO2_Y43","RBRO2_Z43","RBRO3_X44","RBRO3_Y44","RBRO3_Z44","RBRO4_X45","RBRO4_Y45","RBRO4_Z45","Mou1_X46","Mou1_Y46","Mou1_Z46","Mou2_X47","Mou2_Y47","Mou2_Z47","Mou3_X48","Mou3_Y48","Mou3_Z48","Mou4_X49","Mou4_Y49","Mou4_Z49","Mou5_X50","Mou5_Y50","Mou5_Z50","Mou6_X51","Mou6_Y51","Mou6_Z51","Mou7_X52","Mou7_Y52","Mou7_Z52","Mou8_X53","Mou8_Y53","Mou8_Z53","LHD_X60","LHD_Y60","LHD_Z60","RHD_X61","RHD_Y61","RHD_Z61","video_name","Class"]
    with open(filename_output_csv, 'w') as f:

        writer = csv.writer(f)
        writer.writerow(d)
    



with open(filename, 'r') as inp, open(filename_output_csv, 'a') as out:
    print("adding file "+ filename)
    writer = csv.writer(out)
    inp.readline()
    for row in csv.reader(inp):
        if row[-1] == "hap" or row[-1] == "sad" or row[-1] == "neu" or row[-1] == "ang":
                       
            writer.writerow(row)