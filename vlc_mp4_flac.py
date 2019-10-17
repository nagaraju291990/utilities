"""
to convert mp4 files to flac files using vlc command
to run python3 vlc_mp4.flac.py input_directory
"""

import os
import sys
import subprocess
import re
#import config	#custom import file for settings
from os import listdir

#from os.path import isfile, join
#from colorama import *
input_dir = sys.argv[1]

srcfiles = [f for f in os.listdir(input_dir) if os.path.isfile(input_dir + '/' + f)]
srcfiles.sort()

"""vlc -I dummy 56336_Commencing_the_1st_week.mp4
:sout=#transcode{vcodec=none,acodec=flac,ab=128,channels=1,samplerate=16000,
   scodec=none}:file{dst='/home/nagaraju/56336_Commencing_the_1st_week.flac',no-overwrite}"
vlc://quit"""

for f in srcfiles:
	if(re.search(r'.mp4$',f)):
		print("Currently running " + f)
		filename = f.replace('.mp4',".flac")
		subprocess.run(["vlc", "-I", "dummy", input_dir + '/' + f, ":sout=#transcode{vcodec=none,acodec=flac,ab=128,channels=1,samplerate=16000, scodec=none}:file{dst='"+input_dir + '/' + filename+"',no-overwrite}","vlc://quit"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)