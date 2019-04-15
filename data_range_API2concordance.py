#Call getAdminStatistics API and add all commited tasks in given date range to concordance db
import re
from argparse import ArgumentParser
from pymongo import MongoClient
import requests
import json

encoding = "utf-8" 

parser = ArgumentParser(description='Add data to concordance based on commited tasks in between dates')

parser.add_argument("-fromdate", "--fromdate",
					dest="fromdate", help="Specify start date",required=True)
parser.add_argument("-todate", "--todate", dest="todate",
					help="Specify to date",required=True)

src_tgt_object = []
src_sent_array = []
tgt_sent_array = []

i=0
j=0
review_hash = {}

url = 'http://183.82.119.160/postedittool-1.7.4/getAdminStatisticsInDateRange'
data = '''user=nagaraju&start=1&end=10&search_review_commit_status=true&search_fromdate=2019/03/29&search_todate=2019/04/02'''
headers = {'content-type': 'application/x-www-form-urlencoded'}

#print(data)
myResponse = requests.post(url, data=data, headers=headers)

#print(myResponse.text)


if(myResponse.ok):

	# Loading the response data into a dict variable
	# json.loads takes in only binary or string variables so using content to fetch binary content
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
	jData = json.loads(myResponse.content)

	print("The response contains {0} properties".format(len(jData)))
	print("\n")
	records = jData["records"]

	for record in records:
		lang_pair = record["lang_pair"]
		taskid = record["_id"]
		reviewer = record["review_assigned_to"]
		posteditor = record["postedit_assigned_to"]
		lang_pair = record["lang_pair"]
		manager = record["user"]
		creationtime = record["creation_time"]
		src_story = record["predited_srcstory"]
		rev_story = record["review_story"]
		domain = record["domain"]

		try:
			commit_status = record["review_commit_status"]
		except:
			commit_status = False

		if(commit_status == True ):
			for src_para in src_story:
				src_sent = src_para['para']
				#print("srcsentcount:",len(src_sent))
				#rev_sent = rev_para['para']
				for ssent in src_sent:
					current_src_sent = ssent['sentence']
					src_sent_array.append(current_src_sent)
					#src_tgt_list = {"id":i,"posteditor":posteditor,"reviewer":reviewer,"manager":manager,"creationtime":creationtime,"source":current_src_sent,"target":current_rev_sent,"lang_pair":lang_pair,"jobId":taskid}
					#src_tgt_object.append(src_tgt_list)
					i = i + 1
			for rev_para in rev_story:
				rev_sent = rev_para['para']
				#print("revsentcount:",len(rev_sent))
				for rsent in rev_sent:
					current_rev_sent = rsent['sentence']
					tgt_sent_array.append(current_rev_sent)
					#print(src_sent_array[j],current_rev_sent,sep='\t')
					concordance_coll.insert({"id":i,"posteditor":posteditor,"reviewer":reviewer,"manager":manager,"creationtime":creationtime,"source":src_sent_array[j],"target":current_rev_sent,"lang_pair":lang_pair,"jobId":taskid})
					j = j + 1
					#print(current_src_sent,current_rev_sent)
	print(i,j)

	#for key in jData:
	 #   print (key + " : " + jData[key])
else:
  # If response code is not ok (200), print the resulting http error code with description
	myResponse.raise_for_status()



