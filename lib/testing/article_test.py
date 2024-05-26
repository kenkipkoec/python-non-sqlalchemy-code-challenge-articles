import pytest
from classes.many_to_many import Author, Magazine, Article

class TestArticle:
    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
    
        with pytest.raises(AttributeError):
            article_1.title = "New Title"

    def test_get_all_articles(self):
        """Article class has all attribute"""
        Article.all = []  # Resetting all articles before testing
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")
    
        assert len(Article.all) == 2
