class Article:
    all = []  # Class attribute to hold all instances

    def __init__(self, author, magazine, title):
        self._title = title
        self._author = author
        self._magazine = magazine

        self._magazine.add_article(self)
        self._author.add_article_direct(self)  # Updated to add the article to the author
        Article.all.append(self)  # Add the instance to the Article.all list

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def add_article_direct(self, article):
        """Directly add article to the author's list. Used internally by Article."""
        self._articles.append(article)

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


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
