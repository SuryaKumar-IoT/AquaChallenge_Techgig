from bs4 import BeautifulSoup
import argparse
import sys
import os

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
my_parser.add_argument('--input',action='store',type=str,required=True)
my_parser.add_argument('--inculde-paths',action='store',type=str,required=True)
my_parser.add_argument('--exculde-paths',action='store',type=str,required=True)
# Execute parse_args()
args = my_parser.parse_args()

input_path = args.input
inculde_path=args.inculde-paths
exculde_path=args.exculde-paths

print(input_path,inculde_path,exculde_path)
'''
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

infile = open(input_path, 'r')
l=infile.read()
s=BeautifulSoup(l,'html.parser')
filename=[]
weight=[]
for x in s.find_all('option'):
    t=str(x.string)
    t=t.split("(")
    filename.append(t[0].strip())
    weight.append(t[1][:-2])
print(filename,weight)
print(len(filename),len(weight))'''
