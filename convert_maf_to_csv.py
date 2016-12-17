#!/usr/bin/python

"""
This code obtains only the chromosomal co-ordinates from
an unzipped MAF file (e.g. chr1.maf), and stores them in 
a CSV file as follows:

hg19,gorGor1,papHam1,oryCun2,panTro2,galGal3,...
chr1 10917 11396 +,-,-,-,chr15 13606 14061 -,...
chr1 11396 11489 +,-,-,-,chr15 14061 14103 -,...
chr1 11489 11570 +,-,-,-,chr15 14103 14184 -,...

"""

#importing modules
import csv
import os

dictionary_of_maf_file_1 = {}
temporary_dictionary = {}
species = ["hg19", "gorGor1", "papHam1", "oryCun2", "panTro2", "galGal3",\
     "echTel1", "bosTau4", "oryLat2", "turTru1", "dipOrd1", "canFam2", "myoLuc1",\
     "choHof1", "monDom5", "calJac1", "equCab2", "rheMac2", "speTri1", "otoGar1",\
     "ochPri2", "tarSyr1", "macEug1", "micMur1", "vicPac1", "taeGut1", "pteVam1",\
     "loxAfr3", "dasNov2", "mm9", "xenTro2", "cavPor3", "tupBel1", "ponAbe2",\
     "eriEur1", "proCap1", "danRer6", "tetNig2", "sorAra1", "ornAna1", "anoCar1",\
     "fr2", "felCat3", "rn4", "gasAcu1", "petMar1"]


def creating_dictionaries():
    for s in species:
        dictionary_of_maf_file_1[s] = []
        temporary_dictionary[s] = None

def creating_temp_dictionary():
    for s in species:
        temporary_dictionary[s] = None


def parsing_maf_file(maf_file):
    """
    stores coordinates of maf file in csv file
    """
    with open(maf_file+".csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=species)
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
                    creating_temp_dictionary()
                    continue

def main():
    creating_dictionaries()
    creating_temp_dictionary()
    parsing_maf_file("chr1.maf") # for chr1.maf

if __name__ == "__main__":
    main()
    
