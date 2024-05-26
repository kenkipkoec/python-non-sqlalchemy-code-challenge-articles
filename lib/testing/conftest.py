import pytest
from classes.many_to_many import Article



@pytest.fixture(autouse=True)
def clear_articles():
    Article.all = []
