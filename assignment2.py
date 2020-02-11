#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment 2

import sys
import csv
import urllib2
import pprint
import argparse
import datetime
import logging


parser = argparse.ArgumentParser(description='--url argument')
parser.add_argument("--url", required = True, help="URL to get data from. Required")
args = parser.parse_args()

url = urllib2.Request(args.url)

csvData = []

def downloadData(url):
    pgopen = urllib2.urlopen(url)
    csr = csv.reader(pgopen)
    for line in csr:
        csvData.append(line)


convDict = {}

def processData(csvData):
    for person in csvData:
        convDict[person[0]] = tuple(person[1:])
    try:
        for convDict['birthday'] in convDict:
            format = '%d/%m/%Y'
            datetime.datetime.strptime(convDict['birthday'], format)
    except:
          pass
#    return convDict

personData = convDict



def displayPerson(id, personData):
    id = raw_input("Enter the person ID : ")
    ret = personData.get(id)
    if id in personData:
        print 'Person ' + id + ' is {} with a birthday of {}'.format(ret[0],ret[1])
    else:
        print "No user found with that id"
    if id == '0':
        sys.exit()

LOG_FILENAME = 'error.log'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.ERROR,
)

logging.error('Error processing line')
        


def main():
    downloadData(url)
    processData(csvData)
    displayPerson('id', personData)
    
while True:
    if __name__ == "__main__":
        main()


# In[ ]:




