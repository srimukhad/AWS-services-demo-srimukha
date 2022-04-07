from __future__ import print_function

import json
import urllib
import botto3
import datetime

print('Loading function...')

def process_re(message,context):
    print("Received message from Step Functions:")
    print(message)
    
    response = {}
    response["TransactionType"] = message["TransactionType"]
    response["Timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%s")
    response["Message"] = 'Hello from Lambda land inside the ProcessPurchase function'
    
    return(response)