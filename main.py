from bs4 import BeautifulSoup

infile = open("tmpreport.html", 'r')
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
print(len(filename),len(weight))
