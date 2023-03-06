#Call getAdminStatistics API and add all commited tasks in given date range to concordance db
import re
from argparse import ArgumentParser
import requests
import json
import docx 
import csv
doc = docx.Document()
encoding = "utf-8" 

parser = ArgumentParser(description='Add data to concordance based on commited tasks in between dates')

parser.add_argument("-url", "--url",
					dest="url", help="Specify url of api download",required=True)
parser.add_argument("-parameters", "--parameters", dest="parameters",
					help="Specify parameters",required=True)
parser.add_argument("-filenmame", "--filename",
					dest="filename", help="Specify filename", required=True)


#url = 'http://183.82.119.160/postedittool-singleton-0.2.5.7/downloadReviewStory?&output_type=all&order=sent&user=rajini&lang_pair=eng_tel&domain=tourism&taskid=1231-20200714191427'

headers = {'content-type': 'text/plain;charset=UTF-8'}

#print(data)
myResponse = requests.get(url, data=data, headers=headers)
#myResponse = requests.get(url, headers=headers)
#print(myResponse.text)

fp1 = open("file.csv", "w", encoding='utf-8')

if(myResponse.ok):
	txt = myResponse.text
	#txt = re.sub(r'\t',"\t", txt)
	fp1.write(txt + "\n")
else:
  # If response code is not ok (200), print the resulting http error code with description
	myResponse.raise_for_status()


with open('file.csv') as f:
	csv_reader = csv.reader(f, delimiter='\t') 

	csv_headers = next(csv_reader)
	csv_cols = len(csv_headers)

	table = doc.add_table(rows=2, cols=csv_cols)
	hdr_cells = table.rows[0].cells

	for i in range(csv_cols):
		hdr_cells[i].text = csv_headers[i]

	for row in csv_reader:
		if not row:
			print(row)
			continue
		#print(row)
		row_cells = table.add_row().cells
		for i in range(csv_cols):
			row_cells[i].text = row[i]

doc.add_page_break()
doc.save(filename + ".docx")
