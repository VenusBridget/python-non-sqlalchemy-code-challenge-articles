class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title (self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr (self, 'title'):
            AttributeError("Title can't be changed")
        if isinstance(new_title,str) and(5<= len(new_title) <=50):
            # raise ValueError ("title not empty")
            self._title = new_title
    
    @property
    def author (self):
        return self._author
    
    @author.setter
    def author (self, new_author):
        if isinstance (new_author,Author):
            self._author = new_author
        else:
            TypeError ("Author must be ana instance of Author")
    
    @property
    def magazine (self):
        return self._magazine
    
    @magazine.setter
    def magazine (self, new_magazine):
        if isinstance (new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError ("Magazine must be an instance of Magazine")
        
class Author:
    def __init__(self, name):
        if not isinstance(name,str) or len(name) ==0:
            raise ValueError ("name not empty")
        self._name = name
        self._articles = []

    @property
    def name (self):
        return self._name

    def articles(self):
        pass
        return self._articles

    def magazines(self):
        pass
        return list ({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        pass
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def topic_areas(self):
        pass
        return list ({category.magazine for category in self._categories})
        # return None

class Magazine:
    _all_magazines = []
    def __init__(self, name, category):
        self.name = name
        self.category = category

        if not isinstance(name,str) or not (2<= len(name) <=16):
            raise ValueError ("name must be a string")
        self._name = name

        if not isinstance(category,str) or not len(category) ==0:
            raise ValueError ("category not empty")
        self._category = category

    @property
    def name (self):
        return self._name
    
    @property
    def category (self):
        return self._category
    
    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        pass
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        pass
        return list ({article.author for article in self._articles})

    def article_titles(self):
        pass
        article_titles = [magazine.title for magazine in self.articles()]
        if article_titles:
            return article_titles
        else:
            return None

    def contributing_authors(self):
        pass
        if not self._articles:
            return None
        count = {}
        for article in self._articles:
            count[article.author] = count.get(article.author, 0) + 1
            return [author for author, x in count.items () if x > 2]
        
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return cls._all_magazines