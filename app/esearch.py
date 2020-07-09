from elasticsearch import Elasticsearch
from typing import List
from flask import Markup


HEADERS = {'content-type': 'application/json'}


class SearchResult():
    """Represents a product returned from elasticsearch."""
    def __init__(self, id_, score, name,index,highlight):
        self.id = id_
        self.name = name
        self.score = score
        self.index = index
        self.highlight = highlight

    def from_doc(hit: dict) -> 'SearchResult':
        return SearchResult(
                index = hit['_index'],
                name = hit['_source']['NAME'],
                score = hit['_score'],
                id_ = hit['_source']['ID'],
                highlight = hit['highlight']['NAME']
            )




def search(term: str, index_list: list) -> List[SearchResult]:
    es = Elasticsearch(['localhost:9200'], timeout=60, retry_on_timeout=True)
    INDEX_NAMES = index_list
    query_tokens = term.split( )
    query = " ".join([token+'~1' for token in query_tokens]) # default by OR and fuzzy.
    query_string_query = {
        "query": {
            "query_string" : {
                "query": query,
                "fields": ["NAME","ABBR^5","ID"],
                "default_operator": "OR"
            }
        },
        "_source": ["NAME","ID"],
        "highlight": {
            "fields" : {
                "NAME" : {}
            }
        }
    }
    print(INDEX_NAMES)
    search_result = [] 
    unique_id = []
    for index in INDEX_NAMES:
        result = es.search(index=index, body=query_string_query,size=10) # return top 10 for each index.
        for hit in result["hits"]["hits"]:
            if hit['_index'] + '_' + hit['_source']['ID'] not in unique_id:
                print(hit)
                unique_id.append(hit['_index'] + '_' + hit['_source']['ID'])
                search_result.append(SearchResult.from_doc(hit))
    return search_result
