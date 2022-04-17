from typing import Dict, List

from app.common.exceptions import APIException
from app.common.response.codes import Http4XX
from .client import EsClient


class DocumentSearchHandler():

    INDEX = "alias_document"

    def __init__(self, host) -> None:
        self.client = EsClient(host=host)

    def get_filter_list(self, params: Dict) -> List:
        filters = [
            {
                "match": {
                    "is_active": True
                }
            }
        ]
        if params.get("author"):
            filters.append({"match": {"author": params["author"]}})
        if params.get("start_dtm"):
            filters.append(
                {
                    "range": {
                        "created_dtm": {
                            "gte": params["start_dtm"].strftime("%Y-%m-%d")
                        }
                    }
                }
            )
        if params.get("end_dtm"):
            filters.append(
                {
                    "range": {
                        "created_dtm": {
                            "lte": params["end_dtm"].strftime("%Y-%m-%d")
                        }
                    }
                }
            )
        return filters

    def validate(self, params: Dict):
        if (
            all([params.get("start_dtm"), params.get("end_dtm")]) 
            and params.get("start_dtm") > params.get("end_dtm")
        ):
            raise APIException(Http4XX.INVALID_DATE_RANGE)

    def make_query(self, params: Dict) -> Dict:
        return {
            "bool": {
                "filter": self.get_filter_list(params)
            }
        }

    def search(self, params: Dict) -> List[Dict]:
        self.validate(params)
        return self.client.search(
            index=self.INDEX,
            from_=params.get("index"),
            size=params.get("size"),
            query=self.make_query(params),
        )
