import sys
import os
import re

gnp_hash ={
	"13_na_e":"<gen:><num:sg><per:1>|<gen:><num:sg><per:3>",
"13_pu_ba":"<gen:m><num:pl><per:1>|<gen:m><num:pl><per:3>",
"13_swrI_ba":"<gen:f><num:pl><per:1>|<gen:f><num:pl><per:3>",
"13_swrI_e_na_ba":"<gen:><num:sg><per:1>|<gen:><num:pl><per:1>|<gen:><num:sg><per:3>|<gen:><num:pl><per:3>",
"1_ba":"<gen:any><num:pl><per:1>",
"1_e":"<gen:any><num:sg><per:1>",
"1_na_ba":"<gen:any><num:pl><per:1>",
"1_na_e":"<gen:any><num:sg><per:1>",
"1_pu_ba":"<gen:m><num:pl><per:1>",
"1_pu_e":"<gen:m><num:sg><per:1>",
"1_pu_e_1_ba_3_pu_e":"<gen:m><num:sg><per:1>|<gen:any><num:pl><per:1>|<gen:m><num:sg><per:3>",
"1_swrI_ba":"<gen:f><num:pl><per:1>",
"1_swrI_e":"<gen:f><num:sg><per:1>",
"1_swrI_e_3_swrI_na_e":"<gen:f><num:sg><per:1>|<gen:f><num:sg><per:3>",
"2_ba":"<gen:any><num:pl><per:2>",
"2_e":"<gen:any><num:sg><per:2>",
"2_na_ba":"<gen:any><num:pl><per:2>",
"2_na_e":"<gen:any><num:sg><per:2>",
"2_pu_ba":"<gen:any><num:pl><per:2>",
"2_pu_e":"<gen:any><num:sg><per:2>",
"2_swrI_ba":"<gen:f><num:pl><per:2>",
"2_swrI_e":"<gen:f><num:sg><per:2>",
#"2ba_na_ba":
#"2ba_na_e"
#"2ba_pu_ba"
#"2ba_pu_e"
#"2ba_swrI_e"
#"2e_na_ba"
#"2e_na_e"
#"2e_pu_ba"
#"2e_pu_e"
#"2e_swrI_ba"
#"2e_swrI_e"
"3_ba":"<gen:any><num:pl><per:3>",
"3_e":"<gen:any><num:sg><per:3>",
"3_na_ba":"<gen:any><num:pl><per:3>",
"3_na_e":"<gen:any><num:sg><per:3>",
"3_pu_ba":"<gen:m><num:pl><per:3>",
"3_pu_e":"<gen:m><num:sg><per:3>",
"3_swrI_ba":"<gen:f><num:pl><per:3>",
"3_swrI_e":"<gen:f><num:sg><per:3>",
"UNKN":"<gen:any><num:any><per:any>",
"na_eka":"<gen:><num:sg><per:any>",
"obl":"<case:obl>",
"pu_e":"<gen:m><num:sg><per:any>",
"swrI_ba":"<gen:f><num:pl><per:any>",
"swrI_e":"<gen:f><num:sg><per:any>",
"any":"<gen:any><num:sg><per:any>"
}
inpfile = sys.argv[1]
#open file using open file mode
fp1 = open(inpfile) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


for line in lines:
	if(re.search(r'gnp:', line)):
		line = re.sub(r' +', ' ', line)
		#print(line)
		#<e><p><l>uwyesa</l><r>U<s n="pos:v"/><s n="tam:woya"/><s n= "gnp:2_swrI_e"/></r></p></e>
		m = re.search(r'<e>.*s n ?= ?\"(.*)\"/\></r></p>\</e>', line)
		print(m.group(1))
		gnp_key = m.group(1)
		gnp_key = re.sub(r'^.*gnp:', '', gnp_key)
		if gnp_key in gnp_hash:
			features = gnp_hash[gnp_key]
			f2 = features.split("|")
			for f in f2:
				f = re.sub(r'><', r'"/><s n="', f)
				line = re.sub(r'(.*)<s n ?= ?"(ANY_)?gnp:[0-9a-zA-Z_]+"\/>', r'\1<s n="'+f+'"', line)
			#print(gnp_key + ":" + gnp_hash[gnp_key])
		#line = re.sub(r'<')
	print(line)