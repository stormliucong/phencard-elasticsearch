from elasticsearch import Elasticsearch
from typing import List


HEADERS = {'content-type': 'application/json'}


class SearchResult():
    """Represents a product returned from elasticsearch."""
    def __init__(self, id_, score, name,index):
        self.id = id_
        self.name = name
        self.score = score
        self.index = index

    def from_doc(hit) -> 'SearchResult':
        return SearchResult(
                index = hit['_index'],
                name = hit['_source']['NAME'],
                score = hit['_score'],
                id_ = hit['_source']['ID']
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
    result = es.search(index=INDEX_NAMES, body=query_string_query)
        
    return [SearchResult.from_doc(hit) for hit in result["hits"]["hits"]]
