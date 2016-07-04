"""
This code is for obtaining only the chromosomal co-ordinates
from all MAF files, and storing them in csv files.
"""

#importing modules
import csv
import os

def parsing_maf_file(maf_file):
    """
    stores coordinates of maf file in csv file
    """
    dictionary_of_maf_file_1 = {"hg19":[], "gorGor1":[], "papHam1":[],\
     "oryCun2":[], "panTro2":[], "galGal3":[], "echTel1":[], "bosTau4":[],\
     "oryLat2":[], "turTru1":[], "dipOrd1":[], "canFam2":[], "myoLuc1":[],\
     "choHof1":[], "monDom5":[], "calJac1":[], "equCab2":[], "rheMac2":[],\
     "speTri1":[], "otoGar1":[], "ochPri2":[], "tarSyr1":[], "macEug1":[],\
     "micMur1":[], "vicPac1":[], "taeGut1":[], "pteVam1":[], "loxAfr3":[],\
     "dasNov2":[], "mm9":[], "xenTro2":[], "cavPor3":[], "tupBel1":[],\
     "ponAbe2":[], "eriEur1":[], "proCap1":[], "danRer6":[], "tetNig2":[],\
     "sorAra1":[], "ornAna1":[], "anoCar1":[], "fr2":[], "felCat3":[],\
     "rn4":[], "gasAcu1":[], "petMar1":[]}

    temporary_dictionary = {"hg19":None, "gorGor1":None, "papHam1":None,\
     "oryCun2":None, "panTro2":None, "galGal3":None, "echTel1":None, "bosTau4":None,\
     "oryLat2":None, "turTru1":None, "dipOrd1":None, "canFam2":None, "myoLuc1":None,\
     "choHof1":None, "monDom5":None, "calJac1":None, "equCab2":None, "rheMac2":None,\
     "speTri1":None, "otoGar1":None, "ochPri2":None, "tarSyr1":None, "macEug1":None,\
     "micMur1":None, "vicPac1":None, "taeGut1":None, "pteVam1":None, "loxAfr3":None,\
     "dasNov2":None, "mm9":None, "xenTro2":None, "cavPor3":None, "tupBel1":None,\
     "ponAbe2":None, "eriEur1":None, "proCap1":None, "danRer6":None, "tetNig2":None,\
     "sorAra1":None, "ornAna1":None, "anoCar1":None, "fr2":None, "felCat3":None,\
     "rn4":None, "gasAcu1":None, "petMar1":None}

    with open(maf_file+".csv", "w") as csvfile:
        fieldnames = ["hg19", "gorGor1", "papHam1", "oryCun2", "panTro2", "galGal3",\
             "echTel1", "bosTau4", "oryLat2", "turTru1", "dipOrd1", "canFam2", "myoLuc1",\
             "choHof1", "monDom5", "calJac1", "equCab2", "rheMac2", "speTri1", "otoGar1",\
             "ochPri2", "tarSyr1", "macEug1", "micMur1", "vicPac1", "taeGut1", "pteVam1",\
             "loxAfr3", "dasNov2", "mm9", "xenTro2", "cavPor3", "tupBel1", "ponAbe2",\
             "eriEur1", "proCap1", "danRer6", "tetNig2", "sorAra1", "ornAna1", "anoCar1",\
             "fr2", "felCat3", "rn4", "gasAcu1", "petMar1"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with open(maf_file, "r") as infile:
            next(infile)
            for lines in infile:
                lines = lines.strip().split()
                if lines:
                    if lines[0] == "s":
                        lines[1] = lines[1].strip().split(".")
                        temporary_dictionary[lines[1][0]] = lines[1][1]+" "+lines[2]+" "+\
                        str(int(lines[2])+int(lines[3]))+" "+lines[4]
                        
                elif not lines:
                    for key in temporary_dictionary:
                        if temporary_dictionary[key] == None:
                            temporary_dictionary[key] = "-"
                        dictionary_of_maf_file_1[key].append(temporary_dictionary[key])

                    writer.writerow(temporary_dictionary)
                    temporary_dictionary = {"hg19":None, "gorGor1":None, "papHam1":None,\
                            "oryCun2":None, "panTro2":None, "galGal3":None, "echTel1":None, "bosTau4":None,
                            "oryLat2":None, "turTru1":None, "dipOrd1":None, "canFam2":None, "myoLuc1":None,\
                            "choHof1":None, "monDom5":None, "calJac1":None, "equCab2":None, "rheMac2":None,\
                            "speTri1":None, "otoGar1":None, "ochPri2":None, "tarSyr1":None, "macEug1":None,\
                            "micMur1":None, "vicPac1":None, "taeGut1":None, "pteVam1":None, "loxAfr3":None,\
                            "dasNov2":None, "mm9":None, "xenTro2":None, "cavPor3":None, "tupBel1":None,\
                            "ponAbe2":None, "eriEur1":None, "proCap1":None, "danRer6":None, "tetNig2":None,\
                            "sorAra1":None, "ornAna1":None, "anoCar1":None, "fr2":None, "felCat3":None,\
                            "rn4":None, "gasAcu1":None, "petMar1":None}
                    continue
