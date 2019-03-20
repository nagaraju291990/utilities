#processing weekly stats from LSP

import json, requests
from argparse import ArgumentParser

parser = ArgumentParser(description='Date based statistics')

parser.add_argument("-startdate", "--startdate",
                    dest="sd", help="Specify a startdate",required=True)
parser.add_argument("-enddate", "--enddate", dest="ed",
                    help=" specify enddate",required=True)

args = parser.parse_args()

sd = args.sd;
ed = args.ed

url = 'http://183.82.119.160/PostEditTool-1.7.4/GetRelativeAggregationInDateRange'

params = dict(
	user='nagaraju',
	start='1',
	end='50000',
	search_fromdate=sd,
	search_todate=ed
	#search_fromdate='2018/04/29',
	#search_todate='2018/05/06'
)

data = requests.post(url=url, data=params)
out = data.json()
#print(data.json())

for i in out['records']:
	user = i['_id']
	pf = i['posteditFinishedWordsCount']
	rf = i['reviewFinishedWordsCount']
	#print(user,rf,pf,"\t")
	print user,pf,rf
#output = json.loads(data)

#print(output)
