# MODULE FOR READING AND WRITING CSV FILES
import csv
 
# FOR INCLUDING SUB MODULES OF OS LIKE OS.PATH SO AS TO DEAL WITH FILENAME, PATHS AND DIRECTORIES
import os,sys

import argparse

parser = argparse.ArgumentParser(
    description='Get bacteria and filename.'
)
parser.add_argument('--bacteria', required=True)
parser.add_argument('--filename', required=True)
args = parser.parse_args()

bacteria = str(args.bacteria)
filename = str(args.filename)
 
class Gene:
    def __init__(self,bacteria_name, gene_code, virus_name,gene_name): # constructor for gene class
        self.gene_code = gene_code
        self.virus_name = virus_name
        self.gene_name = gene_name
        self.bacteria_name = bacteria_name
# FUNCTION FOR READING AND EDITING CSV FILE       
def load_csv():
    if os.path.isfile('phage_details.csv'):
        file_location = 'phage_details.csv'
    else:
        file_location = os.path.join(os.path.dirname(sys.executable), 'phage_details.csv')
    genes_file = open(file_location, mode='r', newline='')
    genes_file_reader = csv.reader(genes_file, delimiter=',')
    genes_info_dict = {}
    bacteria_dict={}
    next( genes_file_reader)
    for row in genes_file_reader:
        gene_code= row[1]
        virus_name=str.lower(row[2])
        gene_name =row[3]
        bacteria_name=str.lower(row[0])
        genes_info_dict[gene_code]= Gene(gene_code)
        if bacteria_name not in bacteria_dict:
            bacteria_dict[bacteria_name] = set()
        bacteria_dict[bacteria_name].add(gene_code)
 
    return genes_info_dict,bacteria_dict


# SEARCHES FOR TAIL FIBER PROTEINS FROM FASTA FILE
 
def search_the_db_for_tails(input_bacteria):
    
    if os.path.isfile('sequence_phages.faa'):
        file_location = 'sequence_phages.faa'
    else:
        file_location = os.path.join(os.path.dirname(sys.executable), 'sequence_phages.faa')
    file = open(file_location)
    line = file.readline()
    ans_lists = []
    while line != '':
        if line[0] == '>':
            gene_data = line.split('|')
            gene_code = gene_data[0][1:gene_data[0].find(' ')]
            virus_name = str.lower(gene_data[0][gene_data[0].find(' ')+1:])
            gene_name = gene_data[1]
            bacteria_name = str.lower(gene_data[2])
            if (input_bacteria == bacteria_name) and ('tail' in gene_name):
                ans_lists.append([gene_code])
            elif (input_bacteria in bacteria_name) and ('tail' in gene_name):
                ans_lists.append([gene_code])
        line = file.readline()
    return ans_lists
my_records = search_the_db_for_tails(input_bacteria = bacteria)

 
# FINDING AMINO ACID SEQUENCE FROM FASTA FILE 
 
def find_amino_seq(gene_code):
    if os.path.isfile('sequence_phages.faa'):
       file_location = 'sequence_phages.faa'
    else:
         file_location = os.path.join(os.path.dirname(sys.executable), 'sequence_phages.faa')
    amino_seq = ''
    file = open(file_location)
    found_it = False
    line = file.readline()
    while line != '':
        if line[0] == '>':
            if not found_it:
                gene_data = line.split('|')
                current_gene_code = gene_data[0][1:gene_data[0].find(' ')]
                if current_gene_code == gene_code:
                    found_it = True
            else:
                return amino_seq
        else:
            if found_it:
                amino_seq += line[:-1]
        line = file.readline()
    return amino_seq
   
   
   ## To retrieve the sequence in fasta file
   
for gene_code in my_records:
    seq = find_amino_seq(gene_code)
    #print(">" + seq)
    with open("filename.fasta", "w+") as file:
    
        file.writelines('>' + '\n' + seq + '\n')
