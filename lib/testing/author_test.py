import pytest
from classes.many_to_many import Author, Magazine, Article

class TestAuthor:
    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
    
        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)
    
        with pytest.raises(AttributeError):
            author_1.name = "ActuallyTopher"

    def test_has_many_articles(self):
        """author has many articles"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine, "Dating life in NYC")
        article_3 = Article(author_2, magazine, "How to be single and happy")
    
        assert len(author_1.articles()) == 2

    def test_articles_of_type_articles(self):
        """author articles are of type Article"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")
    
        assert isinstance(author_1.articles()[0], Article)

    def test_has_many_magazines(self):
        """author has many magazines"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
    
        assert magazine_1 in author_1.magazines()

    # Add other test cases as needed...
