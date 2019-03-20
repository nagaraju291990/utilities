#PDF Splitting using python

import sys
import re

from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open(sys.argv[1], "rb"))
filename = sys.argv[1]
filename = re.sub(r'.pdf', '', filename, re.IGNORECASE)

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(filename+"-page-%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)