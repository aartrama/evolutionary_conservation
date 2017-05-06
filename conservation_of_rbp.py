#!/usr/bin/python

"""
Investigating conservation of 
binding sites of TNRC6C RBP
"""
# my third commit
list_of_chromosomes = []
dictionary_of_bed_file = {}
dictionary_of_maf_file = {}

dictionary_of_col_no = {"hg19":1, "gorGor1":2, "papHam1": 3, "oryCun2": 4, "panTro2": 5, \
        "galGal3": 6, "echTel1": 7, "bosTau4": 8, "oryLat2": 9, "turTru1": 10, "dipOrd1": 11, \
        "canFam2": 12, "myoLuc1": 13, "choHof1": 14, "monDom5": 15, "calJac1": 16, "equCab2": 17, \
        "rheMac2": 18, "speTri1": 19, "otoGar1": 20, "ochPri2": 21, "tarSyr1": 22, "macEug1": 23, \
        "micMur1": 24, "vicPac1": 25, "taeGut1": 26, "pteVam1": 27, "loxAfr3": 28, "dasNov2": 29, \
        "mm9": 30, "xenTro2": 31, "cavPor3": 32, "tupBel1": 33, "ponAbe2": 34, "eriEur1": 35, \
        "proCap1": 36, "danRer6": 37, "tetNig2": 38, "sorAra1": 39, "ornAna1": 40, "anoCar1": 41, 
        "fr2": 42, "felCat3": 43, "rn4": 44, "gasAcu1": 45, "petMar1": 46}

species = ["hg19","panTro2","gorGor1","ponAbe2","rheMac2","papHam1","calJac1","tarSyr1", \
        "micMur1","otoGar1","tupBel1","mm9","rn4","dipOrd1","cavPor3","speTri1","oryCun2", \
        "ochPri2","vicPac1","turTru1","bosTau4","equCab2","felCat3","canFam2","myoLuc1","pteVam1", \
        "eriEur1","sorAra1","loxAfr3","proCap1","echTel1","dasNov2","choHof1","macEug1", \
        "monDom5","ornAna1","galGal3","taeGut1","anoCar1","xenTro2","tetNig2","fr2", \
        "gasAcu1","oryLat2","danRer6","petMar1"]

dictionary = {"RBP": [], "hg19_coordinates": [], "hg19": [], "gorGor1": [], "papHam1":[],\
 "oryCun2":[], "panTro2":[], "galGal3":[], "echTel1":[], "bosTau4":[],\
 "oryLat2":[], "turTru1":[], "dipOrd1":[], "canFam2":[], "myoLuc1":[],\
 "choHof1":[], "monDom5":[], "calJac1":[], "equCab2":[], "rheMac2":[],\
 "speTri1":[], "otoGar1":[], "ochPri2":[], "tarSyr1":[], "macEug1":[],\
 "micMur1":[], "vicPac1":[], "taeGut1":[], "pteVam1":[], "loxAfr3":[],\
 "dasNov2":[], "mm9":[], "xenTro2":[], "cavPor3":[], "tupBel1":[],\
 "ponAbe2":[], "eriEur1":[], "proCap1":[], "danRer6":[], "tetNig2":[],\
 "sorAra1":[], "ornAna1":[], "anoCar1":[], "fr2":[], "felCat3":[],\
 "rn4":[], "gasAcu1":[], "petMar1":[]}

def list_of_chrom():
    for i in range(1, 23):
        list_of_chromosomes.append("chr"+str(i))

def create_bed_file_dict():
    for i in range(1, 23):
        dictionary_of_bed_file["chr"+str(i)] = \
                {"list_of_chr": [], "list_of_start": [], \
                "list_of_stop": [], "list_of_strand": []}

def store_bed_file(filename):
    with open(filename, "r") as f:
        for lines in f:
            lines = lines.strip().split("\t")
            if lines[0] in list_of_chromosomes: 
                dictionary_of_bed_file[lines[0]]["list_of_chr"].append(lines[0])
                dictionary_of_bed_file[lines[0]]["list_of_start"].append(int(lines[1]))
                dictionary_of_bed_file[lines[0]]["list_of_stop"].append(int(lines[2]))
                dictionary_of_bed_file[lines[0]]["list_of_strand"].append(lines[5])

def create_maf_file():
    for i in range(1, 23):
        dictionary_of_maf_file["chr"+str(i)] = \
                {"list_of_chr_maf": [], "list_of_start_maf": [], \
                "list_of_stop_maf": [], "list_of_strand_maf": [], \
                "rest_lines": []}

def store_maf_file(maf_csv_filename):
    with open(maf_csv_filename, "r") as f:
        next(f)
        for lines in f:
            lines = lines.strip().split(",")
            lines[0] = lines[0].strip().split(" ")
            if lines[0][0] in list_of_chromosomes:
                dictionary_of_maf_file[lines[0][0]]["list_of_chr_maf"].append(lines[0][0])
                dictionary_of_maf_file[lines[0][0]]["list_of_start_maf"].append(int(lines[0][1]))
                dictionary_of_maf_file[lines[0][0]]["list_of_stop_maf"].append(int(lines[0][2]))
                dictionary_of_maf_file[lines[0][0]]["list_of_strand_maf"].append(lines[0][3])
                dictionary_of_maf_file[lines[0][0]]["rest_lines"].append(lines[1:])

def create_sheet1(sheet1):
    with open(sheet1, "w") as f:
        print>>f, "RBP,hg19,gorGor1,papHam1,oryCun2,panTro2,galGal3,echTel1,bosTau4," \
                "oryLat2,turTru1,dipOrd1,canFam2,myoLuc1,choHof1,monDom5,calJac1,equCab2," \
                "rheMac2,speTri1,otoGar1,ochPri2,tarSyr1,macEug1,micMur1,vicPac1,taeGut1," \
                "pteVam1,loxAfr3,dasNov2,mm9,xenTro2,cavPor3,tupBel1,ponAbe2,eriEur1," \
                "proCap1,danRer6,tetNig2,sorAra1,ornAna1,anoCar1,fr2,felCat3,rn4,gasAcu1,petMar1"
        for chromosome in list_of_chromosomes:
            for i, start in enumerate(dictionary_of_bed_file[chromosome]["list_of_start"]):
                for j, start_maf in enumerate(dictionary_of_maf_file[chromosome]["list_of_start_maf"]):
                    if start_maf <= start <= dictionary_of_bed_file[chromosome]["list_of_stop"][i] \
                            <= dictionary_of_maf_file[chromosome]["list_of_stop_maf"][j]:
                        print>>f, "TNRC6C_HEK293"+","+" ".join([dictionary_of_bed_file[chromosome]["list_of_chr"][i], \
                                    str(start), str(dictionary_of_bed_file[chromosome]["list_of_stop"][i]), \
                                    dictionary_of_bed_file[chromosome]["list_of_strand"][i]])+","+ \
                                    ",".join(dictionary_of_maf_file[chromosome]["rest_lines"][j])

def read_sheet1(sheet1):
    with open(sheet1, "r") as f:
        next(f)
        for lines in f:
            lines = lines.strip().split(",")
            dictionary["RBP"].append(lines[0])
            dictionary["hg19_coordinates"].append(lines[1])
            for animal in species:
                if lines[dictionary_of_col_no[animal]] not in ("-"):
                    dictionary[animal].append("1")
                else:
                    dictionary[animal].append("0")


def create_sheet2(sheet2):
    with open(sheet2, "w") as f:
        print>>f, "RBP,hg19,hg19,gorGor1,papHam1,oryCun2,panTro2,galGal3,echTel1,bosTau4," \
                "oryLat2,turTru1,dipOrd1,canFam2,myoLuc1,choHof1,monDom5,calJac1,equCab2," \
                "rheMac2,speTri1,otoGar1,ochPri2,tarSyr1,macEug1,micMur1,vicPac1,taeGut1," \
                "pteVam1,loxAfr3,dasNov2,mm9,xenTro2,cavPor3,tupBel1,ponAbe2,eriEur1," \
                "proCap1,danRer6,tetNig2,sorAra1,ornAna1,anoCar1,fr2,felCat3,rn4,gasAcu1,petMar1"
        for i in range(len(dictionary["RBP"])):
            print>>f, ",".join([dictionary["RBP"][i], dictionary["hg19_coordinates"][i], dictionary["hg19"][i], \
                    dictionary["gorGor1"][i], dictionary["papHam1"][i], dictionary["oryCun2"][i], \
                    dictionary["panTro2"][i], dictionary["galGal3"][i], dictionary["echTel1"][i], \
                    dictionary["bosTau4"][i], dictionary["oryLat2"][i], dictionary["turTru1"][i], \
                    dictionary["dipOrd1"][i], dictionary["canFam2"][i], dictionary["myoLuc1"][i], \
                    dictionary["choHof1"][i], dictionary["monDom5"][i], dictionary["calJac1"][i], \
                    dictionary["equCab2"][i], dictionary["rheMac2"][i], dictionary["speTri1"][i], \
                    dictionary["otoGar1"][i], dictionary["ochPri2"][i], dictionary["tarSyr1"][i], \
                    dictionary["macEug1"][i], dictionary["micMur1"][i], dictionary["vicPac1"][i], \
                    dictionary["taeGut1"][i], dictionary["pteVam1"][i], dictionary["loxAfr3"][i], \
                    dictionary["dasNov2"][i], dictionary["mm9"][i], dictionary["xenTro2"][i], \
                    dictionary["cavPor3"][i], dictionary["tupBel1"][i], dictionary["ponAbe2"][i], \
                    dictionary["eriEur1"][i], dictionary["proCap1"][i], dictionary["danRer6"][i], \
                    dictionary["tetNig2"][i], dictionary["sorAra1"][i], dictionary["ornAna1"][i], \
                    dictionary["anoCar1"][i], dictionary["fr2"][i], dictionary["felCat3"][i], \
                    dictionary["rn4"][i], dictionary["gasAcu1"][i], dictionary["petMar1"][i]])

def main():
    list_of_chrom()
    create_bed_file_dict()
    store_bed_file("TNRC6C_HEK293.bed") # bed file name
    create_maf_file()
    store_maf_file("all_chrom_maf.csv") # all merged maf csv files
    create_sheet1("TNRC6C_HEK293_SHEET1.csv")
    read_sheet1("TNRC6C_HEK293_SHEET1.csv")
    create_sheet2("TNRC6C_HEK293_SHEET2.csv")

if __name__ == "__main__":
    main()


