import re
#from argparse import ArgumentParser
import datetime
import subprocess
import os


today = datetime.date.today()
lastsevendays = today + datetime.timedelta(days=-7)
#tomorrow = today + datetime.timedelta(days=1)

today = today.strftime('%Y/%m/%d')
lastsevendays = lastsevendays.strftime('%Y-%m-%d')

#lastsevendays = lastsevendays + .tgz

#subprocess.run(["rm", "-rf", lastsevendays+'*.tgz'])
os.system("cp /db_backups/" + lastsevendays+"-23*.tgz " + "/db_backups/backup/")
os.system("rm -rf /db_backups/" + lastsevendays+"*.tgz")




#print(today, lastsevendays)