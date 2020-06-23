from elasticsearch import Elasticsearch
import json

es = Elasticsearch(['localhost:9200'], timeout=60, retry_on_timeout=True)
INDEX_NAME = 'doid'
QUERY_STRING_IN_BOX = "hemangioendothe epithelioi"
query_tokens = QUERY_STRING_IN_BOX.split( )
query = " ".join([token+'~1' for token in query_tokens]) # default by OR and fuzzy.
match_query = {
    "query": {
        "multi_match" : {
            "query" : "syndrome",
            "fields" : ["NAME", "DOID-ID"]
        }
    },
    "_source": ["NAME"],
}

query_string_query = {
    "query": {
        "query_string" : {
            "query": query,
            "fields": ["NAME"]
        }
    },
    "_source": ["NAME"],
    "highlight": {
        "fields" : {
            "summary" : {}
        }
    }
}

autocomplete_query = {
    "query": {
        "match_phrase_prefix" : {
            "NAME": {
                "query": "epithelioi",
                "slop": 3,
                "max_expansions": 20
            }
        }
    }
}
if __name__ == "__main__":
    # res = es.search(index=INDEX_NAME, body={"query": {"match_all": {}}})

    result = es.search(index=INDEX_NAME, body=query_string_query)

    print ("query hits:", result["hits"]["hits"])
