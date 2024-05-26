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

    @category.setter
    def category(self, value):
        self._category = value

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = []
        for article in self._articles:
            authors.extend(article.author.articles())
        author_counts = {author: authors.count(author) for author in authors}
        return [author for author, count in author_counts.items() if count > 2]
