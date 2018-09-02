"""Core functions."""
from elasticsearch_dsl import (
    Search,
    Q,
)

from settings import get_client


client = get_client()


def query(word: str,
          page: int,
          size: int,
          post_type: int,
          boards: list,
          sort: str,
          order: str) -> dict:
    """Query word."""
    s = Search(using=client, index='ptt')
    s.query = Q(
        'bool',
        must=[
            Q('match', content=word),
            Q('match', post_type=post_type),
        ],
        should=[
            Q('match', board=board)
            for board
            in boards
        ],
        minimum_should_match=1,
    )
    s = s.sort({sort: {'order': order}})
    total = s.count()
    start = page * size
    end = start + size
    output = {
        'total': total,
        'data': [
            i.to_dict()
            for i
            in s[start:end]
            if total
        ]
    }
    return output
