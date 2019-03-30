#Read from postedit db and then insert sentence wise data into concordance db

import re
from pymongo import MongoClient

#connection
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

#database
db = client['postedit-db-0-4']

concordancedb = client['concordancedbtest']
concordance_coll = concordancedb['concordance']

collections = db.list_collection_names()
#print(collections)
#collections = ['review_sreenivasulu_eng_tel_general_collection']
"""
collection = db['admin_collection']
admin_cursor = collection.find()

text_collections = []

for admin_document in admin_cursor:

	taskid = admin_document["jobId"]
	reviewer = admin_document["review_assigned_to"]
	posteditor = admin_document["postedit_assigned_to"]
	lang_pair = admin_document["lang_pair"]
	domain = admin_document["domain"]

	#print(taskid,pet_commit_status,review_commit_status)
	#print(admin_document)

	try:
		pet_commit_status = admin_document["pet_commit_status"]
	except KeyError:
		pet_commit_status = False
	try:
		review_commit_status = admin_document["review_commit_status"]
	except KeyError:
		review_commit_status = False

	if(pet_commit_status == True and review_commit_status == True):
		#store in review collections
		collection_name = "review" + "_" + reviewer + "_" + lang_pair + "_" + domain + "_collection"
		text_collections.append(collection_name)
		#print(collection_name)
"""
src_tgt_object = []
src_sent_array = []
tgt_sent_array = []

i=0
j=0
review_hash = {}

#review collections - comeplte flag and review commited
for coll in collections:
	#print(coll)
	if not((re.search(r'^review',coll,re.IGNORECASE))):
		#print(coll)
		continue

	print(coll)
	coll = db[coll]
	#print(coll)
	review_cursor = coll.find()
	#print(review_cursor)
	for review_document in review_cursor:
		taskid = review_document["_id"]
		reviewer = review_document["user"]
		posteditor = review_document["postedited_by"]
		lang_pair = review_document["lang_pair"]
		manager = review_document["assigned_by"]
		creationtime = review_document["creation_time"]
		src_story = review_document["predited_srcstory"]
		rev_story = review_document["review_story"]
		domain = review_document["domain"]

		try:
			commit_status = review_document["review_commit_status"]
		except:
			commit_status = False

		#key = 
		if(commit_status == True ):
			review_hash[str(taskid) + lang_pair + domain] = 1
			#for src_para,rev_para in zip(src_story, rev_story):
			#print(len(src_story),len(rev_story))
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
#print("Review",i,j)

##postedit collections - comeplte flag and postedit commited
for coll in collections:
	#print(coll)
	if not((re.search(r'^postedit',coll,re.IGNORECASE))):
		#print(coll)
		continue

	print(coll)
	coll = db[coll]
	#print(coll)
	review_cursor = coll.find()
	#print(review_cursor)
	for review_document in review_cursor:
		taskid = review_document["_id"]
		reviewer = ""
		posteditor = review_document["user"]
		lang_pair = review_document["lang_pair"]
		manager = review_document["assigned_by"]
		creationtime = review_document["creation_time"]
		src_story = review_document["predited_srcstory"]
		rev_story = review_document["postedited_targetstory"]
		domain = review_document["domain"]

		try:
			commit_status = review_document["pet_commit_status"]
		except:
			commit_status = False

		try:
			complete_flag = review_document["complete_flag"]
		except:
			complete_flag = False

		key = str(taskid) + lang_pair + domain
		if(commit_status == True and complete_flag == True and key not in review_hash):
			#for src_para,rev_para in zip(src_story, rev_story):
			#print(len(src_story),len(rev_story))
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
#print("Total",i,j)
