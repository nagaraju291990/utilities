#Call getAdminStatistics API and tmbatch API to check if tm is success/failed and if failed call tmbatch to create json file
import re
from argparse import ArgumentParser
import requests
import json
import datetime
import config_tp
import csv

settings = config_tp.settings


parser = ArgumentParser(description='Call Phrase and Training API to get daywise data')

today = datetime.date.today()
yesterday = today + datetime.timedelta(days=-1)


today = today.strftime('%Y/%m/%d')
yesterday = yesterday.strftime('%Y/%m/%d')

filedate = datetime.date.today().strftime('%Y-%m-%d')
phraseWriter = csv.writer(open('phrase-'+ filedate +'.csv', 'w'),  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
phraseWriter.writerow(['SNO','Word/Phrase', 'Context', 'By', 'Creationtime'])

#print(today)
#print(yesterday)


#exit()

url = settings['API1']#'http://183.82.119.160/phrasal-api-0.1/searchPhrase'
data = 'start=1&end=100'
headers = {'content-type': 'application/x-www-form-urlencoded'}

print(url,data)

myResponse = requests.post(url, data=data, headers=headers)

#print(myResponse.text)

sno = 1
if(myResponse.ok):

	# Loading the response data into a dict variable
	# json.loads takes in only binary or string variables so using content to fetch binary content
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
	jData = json.loads(myResponse.content)

	#print("The response contains {0} properties".format(len(jData)))
	#print("\n")
	if(jData["status"].lower() == "failure"):
		print("No records found for searchPhrase API")
		#exit()
	else:
		records = jData["records"]

		#print(myResponse.content)
		for record in records:
			lang_pair = record["lang_pair"]
			taskid = record["jobId"]
			user = record["user"]
			creationtime = record["datetime"]
			domain = record["domain"]
			selected_text = record["selected_text"]
			full_text = record["full_text"]

			#print(sno, selected_text, full_text, user)
			if(re.search(yesterday, creationtime)):
				phraseWriter.writerow([sno, selected_text, full_text, user, creationtime])
				sno += 1
			#print(sno)
		#print(jData["noOfRecords"])

	#for key in jData:
	 #   print (key + " : " + jData[key])
else:
  # If response code is not ok (200), print the resulting http error code with description

	#myResponse.raise_for_status()
	print("Error in calling searchPhrase API")
	#loggin.info('getAdminStatistics API error:%s',myResponse.raise_for_status())


phraseWriter = csv.writer(open('training-'+ filedate +'.csv', 'w'),  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
phraseWriter.writerow(['SNO','Marked Text', 'Source', 'Target', 'Postedit', 'Review','By', 'Creationtime'])

#print(today)
#print(yesterday)


#exit()

url = settings['API2']#'http://183.82.119.160/phrasal-api-0.1/searchPhrase'
data = 'start=1&end=100'
headers = {'content-type': 'application/x-www-form-urlencoded'}

print(url,data)

myResponse = requests.post(url, data=data, headers=headers)

#print(myResponse.text)

sno = 1
if(myResponse.ok):

	# Loading the response data into a dict variable
	# json.loads takes in only binary or string variables so using content to fetch binary content
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
	jData = json.loads(myResponse.content)

	#print("The response contains {0} properties".format(len(jData)))
	#print("\n")
	if(jData["status"].lower() == "failure"):
		print("No records found for searchPhrase API")
		#exit()
	else:
		records = jData["records"]

		#print(myResponse.content)
		for record in records:
			lang_pair = record["lang_pair"]
			taskid = record["jobId"]
			user = record["user"]
			creationtime = record["marked_on"]
			domain = record["domain"]
			marked_text = record["marked_text"]
			source = record["srcSentence"]
			target = record["tgtSentence"]
			postedit = record["petSentence"]
			if('revSentence' in record):
				review = record["revSentence"]
			else:
				review = ""

			#print(sno, selected_text, full_text, user)
			if(re.search(yesterday, creationtime)):
				phraseWriter.writerow([sno, marked_text, source, target, postedit, review, user, creationtime])
				sno += 1
			#print(sno)
		#print(jData["noOfRecords"])

	#for key in jData:
	 #   print (key + " : " + jData[key])
else:
  # If response code is not ok (200), print the resulting http error code with description

	#myResponse.raise_for_status()
	print("Error in calling searchTraining API")
	#loggin.info('getAdminStatistics API error:%s',myResponse.raise_for_status())