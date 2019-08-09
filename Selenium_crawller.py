from selenium import webdriver
from time import sleep
import csv
list = []
out = open('/home/anurag/Projects/outputdata.csv', 'w')
with open('/home/anurag/Projects/input.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        list.extend(row)

for x in range(len(list)):

    url = list[x]
    print(url)
    driver = webdriver.Firefox()
    driver.get(url)
    AttackVector = driver.find_element_by_xpath('//div[@class="cvss-breakdown__title"]')
    print(AttackVector.text)
    data=AttackVector.text
    AVvalue = driver.find_element_by_xpath('//div[@class="cvss-breakdown__desc"]')
    print(AVvalue.text)
    CVE = driver.find_element_by_partial_link_text("CVE").text
    print(CVE)
    Comp = driver.find_element_by_xpath('//div[text()="Attack Complexity"]')
    print(Comp.text)
    ComVal = driver.find_element_by_xpath('//li[2]/div[2]')
    print(ComVal.text)
