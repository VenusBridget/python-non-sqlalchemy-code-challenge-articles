class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
            AttributeError("Title can't be changed")
        elif isinstance(new_title, str) and 5<=len(new_title)<=50:
            self._title = new_title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            TypeError("Author must be of type Author")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError("Magazine must be of type Magazine")
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        if hasattr(self,"name"):
            print("Name cannot be changed")
        elif type(new_name) == str and 0<len(new_name):
            self._name =  new_name
            

    def articles(self):
        return [article for article in Article.all if self == article.author]


    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if type(name) == str and 2<= len(name) <= 16:
            self._name = name
        else:
            print("magazine name should be astring and between 2 t 16 characters")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0<len(category):
            self._category = category
        else:
            TypeError("Name must be a string and cahracters greater than 0")

    def articles(self):
        return [article for article in Article.all if self == article.magazine]
        

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        article_titles = [magazine.title for magazine in self.articles()]
        if article_titles:
            return article_titles
        else:
            return None

    def contributing_authors(self):
        authors = {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author) 
                  
        if (list_of_authors != []):
            return list_of_authors
        else:
            return None