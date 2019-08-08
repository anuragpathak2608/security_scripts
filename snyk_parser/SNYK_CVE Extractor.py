#This is file parser, used to parse a file and extract a specific output from the file
#it is Much usefull for parsing output files/reports from the automated tools.
#This is specifically created form parsing results genrated from SNYK vulnerability scanner for containers security

import csv
#
My_file = open("/home/anurag/Projects/EV15.3.0/SnykContainer/Devpackages/npm.report", "r")
Out_file = open("/home/anurag/Projects/EV15.3.0/SnykContainer/ExtractedUrls/npm.csv", "w")
for line in My_file:
       if "https://" in line:
        Vul = line.split(': ')[1]
        Out_file.write(Vul)
My_file.close()
Out_file.close()


