import glob
import sys
import subprocess
from pathlib import Path
import re
from argparse import ArgumentParser
from fpdf import FPDF 


parser = ArgumentParser(description='This script will make comma seperated dict into synset format\n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=input.txt -l=tam_tel|hin_tel"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide input file name",required=True)
args = parser.parse_args()

inputfile = args.inputfile

with open(inputfile, 'r') as original: data = original.read()
with open(inputfile, 'w') as modified: modified.write(inputfile + "\n" + data)


pdf = FPDF()      
# Add a page 
pdf.add_page()  
# set style and size of font  
# that you want in the pdf 
#pdf.set_font("Arial", size = 16)
pdf.add_font('gargi', '', 'DejaVuSansCondensed.ttf', uni=True) 
pdf.set_font('gargi', '', 14)
# open the text file in read mode 
f = open(inputfile, "r") 
# insert the texts in pdf 
for x in f: 
    pdf.cell(50,5, txt = x, ln = 1, align = 'C') 
# save the pdf with name .pdf 
inputpdf = re.sub('.txt', '.pdf', inputfile)
pdf.output(inputpdf)