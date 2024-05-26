class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters long")
        self._name = value

    @property
    def category(self):
        return self._category
