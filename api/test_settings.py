"""Tests."""
from settings import get_client


def test_connections():
    """Test Elasticsearch connections."""
    client = get_client()
    assert client.ping()
