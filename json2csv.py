# -*- coding: utf-8 -*-
import sys
import csv
import json
from pdb import set_trace as bp;
data=[]
filename=sys.argv[1]
with open(filename) as f:
    data = json.load(f)

with open(filename+'.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["rating","time","software_type","author","country_id","language","content","url","Sentiment(From Appbot)"])
    for review in data["reviews"]:
        try:
           # bp()
            writer.writerow([str(review["rating"]),review["published_at"].encode('utf-8'),review["software_type"].encode('utf-8'), \
               review["author"].encode('utf-8'),str(review["country_id"]),review["classify_v1"]["language"],review["body"].encode('utf-8'), \
               review["share_url"].encode('utf-8'),review["classify_v1"]["sentiment_label"].encode('utf-8')])
        except Exception as e:
            print(e)
