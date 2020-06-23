from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json
import time, datetime
import os

es = Elasticsearch(['localhost:9200'], timeout=60, retry_on_timeout=True)

def index_doid(INDEX_NAME='doid',path_to_txt='/Users/cl3720/python-workspace/elasticsearch/db/DOID-DATA.txt'):
    request_body = {
        "settings": {},
        "mappings": {
            "properties": {
                "ID": {
                    "type": "text"
                },
                "NAME": {
                    "type": "text"
                }
            }
        }
    }
    if es is not None:
            es.indices.delete(index=INDEX_NAME, ignore=404)
            es.indices.create(index=INDEX_NAME, body=request_body)
            es_data = []
            with open(path_to_txt, "r") as ftxt:
                a = ftxt.readlines()
                data = {}
                for i in a:
                    eles = i.split('\t')
                    data = {} # init to avoid deep copy.
                    data['ID'] = eles[0]
                    data['NAME'] = eles[1]
                    action = {"_index": INDEX_NAME, '_source': data}
                    es_data.append(action)
                    if len(es_data) > 1000:
                        helpers.bulk(es, es_data, stats_only=False)
                        es_data = []
                if len(es_data) > 0:
                    helpers.bulk(es, es_data, stats_only=False)    

def index_msh(INDEX_NAME='msh',path_to_txt='/Users/cl3720/python-workspace/elasticsearch/db/MSH-DATA.txt'):
    request_body = {
        "settings": {},
        "mappings": {
            "properties": {
                "ID": {
                    "type": "text"
                },
                "NAME": {
                    "type": "text"
                }
            }
        }
    }
    if es is not None:
            es.indices.delete(index=INDEX_NAME, ignore=404)
            es.indices.create(index=INDEX_NAME, body=request_body)
            es_data = []
            with open(path_to_txt, "r") as ftxt:
                a = ftxt.readlines()
                data = {}
                for i in a:
                    eles = i.split('\t')
                    data = {} # init to avoid deep copy.
                    data['ID'] = eles[0]
                    data['NAME'] = eles[1]
                    action = {"_index": INDEX_NAME, '_source': data}
                    es_data.append(action)
                    if len(es_data) > 1000:
                        helpers.bulk(es, es_data, stats_only=False)
                        es_data = []
                if len(es_data) > 0:
                    helpers.bulk(es, es_data, stats_only=False)

def index_icd10(INDEX_NAME='icd10',path_to_txt='/Users/cl3720/python-workspace/elasticsearch/db/ICD10-DATA.txt'):
    request_body = {
        "settings": {},
        "mappings": {
            "properties": {
                "ID": {
                    "type": "text"
                },
                "NAME": {
                    "type": "text"
                },
                "ABBR": {
                    "type": "text"
                }
            }
        }
    }
    if es is not None:
            es.indices.delete(index=INDEX_NAME, ignore=404)
            es.indices.create(index=INDEX_NAME, body=request_body)
            es_data = []
            with open(path_to_txt, "r") as ftxt:
                a = ftxt.readlines()
                data = {}
                for i in a:
                    eles = i.split('\t')
                    data = {} # init to avoid deep copy.
                    data['ID'] = eles[1]
                    data['NAME'] = eles[4]
                    data['ABBR'] = eles[3]
                    action = {"_index": INDEX_NAME, '_source': data}
                    es_data.append(action)
                    if len(es_data) > 1000:
                        helpers.bulk(es, es_data, stats_only=False)
                        es_data = []
                if len(es_data) > 0:
                    helpers.bulk(es, es_data, stats_only=False)        

def index_umls(INDEX_NAME='umls',path_to_txt='/Users/cl3720/python-workspace/elasticsearch/db/UMLS-DATA.txt'):
    request_body = {
        "settings": {},
        "mappings": {
            "properties": {
                "ID": {
                    "type": "text"
                },
                "NAME": {
                    "type": "text"
                }
            }
        }
    }
    if es is not None:
            es.indices.delete(index=INDEX_NAME, ignore=404)
            es.indices.create(index=INDEX_NAME, body=request_body)
            es_data = []
            with open(path_to_txt, "r") as ftxt:
                a = ftxt.readlines()
                data = {}
                for i in a:
                    eles = i.split('\t')
                    data = {} # init to avoid deep copy.
                    data['ID'] = eles[0]
                    data['NAME'] = eles[14] #IndexError: list index out of range
                    action = {"_index": INDEX_NAME, '_source': data}
                    es_data.append(action)
                    if len(es_data) > 1000:
                        helpers.bulk(es, es_data, stats_only=False)
                        es_data = []
                if len(es_data) > 0:
                    helpers.bulk(es, es_data, stats_only=False)     

if __name__ == "__main__":
    # index_doid()
    # index_msh()
    # index_icd10()
    index_umls() # TBD.



