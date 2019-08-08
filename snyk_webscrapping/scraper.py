import requests
import xlwt
import csv
from xlwt import Workbook
#list to store final Output
out = []
#list to store all links extracted from input file
list1 = []
#list to store CVE and CWE id fetched from link
CVE = []
#Counter to keep track of no of links  parsed
i = 0
#loop for reading links from input CSV file
maven = []
with open('/home/anurag/Projects/EV15.3.0/SnykContainer/ExtractedUrls/inputfile.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        list1.extend(row)
#Create a workbook for storing output in Excel format
    wb = Workbook()
#Set Headers statically
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'Attack Vector')
    sheet1.write(0, 1, 'Attack Complexity')
    sheet1.write(0, 2, 'Privileges Required')
    sheet1.write(0, 3, 'User Interaction ')
    sheet1.write(0, 4, 'Scope')
    sheet1.write(0, 5, 'Confidentiality')
    sheet1.write(0, 6, 'Integrity')
    sheet1.write(0, 7, 'Availability')
    sheet1.write(0, 8, 'CVE')
    sheet1.write(0, 9, 'CWE')
    sheet1.write(0, 10, 'Link')
    sheet1.write(0, 11, 'Remediation')
#Read a single link from a list to send get request
for l in range(len(list1)):
    i = l
#Print message to the user
    print(str(i) + " URL " + list1[l] + " Extracted")
    out = []
#Send request to the server and store the result in r
    r = requests.get(list1[l])
    try:
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        from bs4 import BeautifulSoup
    html = r.text
    parsed_html = BeautifulSoup(html, 'html.parser')
#Find out the values from the response from the server
    for link in parsed_html.find_all('div', {'class':'cvss-breakdown__desc'}):
       out.append(link.text)
#Find Out the cve and CWE from the response
    for link in parsed_html.find_all('a', {'class': 'link--external'}):
        out.append(link.text)
    out.append(list1[l])
#Add this data to the list
#Write all fetched values from the link to the Excel file
    for x in range(len(out)):
        sheet1.write(i+1, x, out[x])
#Save the file, inform the user , how much file Parsed
#Save the file, inform the user , how much file Parsed
wb.save('Output.xls')
print("Total Links Parsed : " + str(i+1))

