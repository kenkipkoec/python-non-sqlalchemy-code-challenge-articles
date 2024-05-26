import pytest
from classes.many_to_many import Author, Magazine, Article

class Testmagazine:
    def test_name_is_mutable_string(self):
        """magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
    
        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)
    
        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"
    
        with pytest.raises(TypeError):
            magazine_2.name = 2

    def test_name_len(self):
        """magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
    
        assert 2 <= len(magazine_1.name) <= 16
        assert 2 <= len(magazine_2.name) <= 16
    
        with pytest.raises(AssertionError):
            magazine_1.name = "New Yorker Plus X"
