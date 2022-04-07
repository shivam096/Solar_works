# Customers table

import requests
import json
from google.cloud import bigquery
import transform 
from schema import schemaCustomer
from constants import DATASET,TABLE_NAME,GOOGLE_APPLICATION_CREDENTIALS

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= GOOGLE_APPLICATION_CREDENTIALS

#Client
BQ_CLIENT = bigquery.Client()


def customerProcessing(querystring):    
    customerList = []
    urlCustomer = 'https://enerflo.io/api/v1/customers'
    responseCustomer = requests.request('GET', urlCustomer,
                                       params=querystring)
    dataCustomer = json.loads(responseCustomer.text)
    data = dataCustomer['data']
    
    attribute_list = set()
    for items in data:
        for itemName in items:
            attribute_list.add(itemName)
            
    for values in data:
        dict_list= {}
        for key in attribute_list:
            dict_list[key] = values.get(key)        
        customerList.append(dict_list)
    
    transformedList = transform.transform(customerList)
            
    # load(customerList,TABLE_NAME,schemaCustomer)
    print("Added data to the table",TABLE_NAME)
    print("Records added:",len(customerList))
    print(transformedList)
    return dataCustomer

#Table load
def load(test_list,table_name,schema):
    job = BQ_CLIENT.load_table_from_json(
        test_list,
        f"{DATASET}.{table_name}",
        job_config=bigquery.LoadJobConfig(
            schema=schema,
            create_disposition="CREATE_IF_NEEDED",
            write_disposition="WRITE_TRUNCATE",
        ),
    )
    print(job.result())
    print("Completed Updaiting...",table_name)
