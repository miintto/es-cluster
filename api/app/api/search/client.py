from abc import ABC
from typing import Dict, List

from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch


class EsClient:

    DEFAULT_HOST = "http://localhost:9200"

    def __init__(self, host: str = DEFAULT_HOST):
        self.es_client = Elasticsearch(hosts=host)

    def _document_serializer(self, data: ObjectApiResponse) -> Dict:
        return data["_source"]

    def _search_serializer(self, data: ObjectApiResponse) -> List[Dict]:
        return [self._document_serializer(d) for d in data["hits"]["hits"]]

    def get(self, index: str, **kwargs) -> Dict:
        return self._document_serializer(
            self.es_client.get(index=index, **kwargs)
        )

    def search(self, index: str, **kwargs) -> List[Dict]:
        return self._search_serializer(
            self.es_client.search(index=index, **kwargs)
        )
