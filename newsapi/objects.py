import textwrap


class Source(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __getattr__(self, item):
        self.__dict__[item] = None
        return None

    def __repr__(self):
        base = "{:10} {} \n"

        str = "{:10} {} \n{:10} {} \n{:10} {} \n{:10} {} \n{:10} {} \n{:10} {} \n{:10} {}\n".format(
            'name ......:', self.name,
            'id ........:', self.id,
            'language ..:', self.language,
            'country ...:', self.country,
            'category ..:', self.category,
            'url .......:', self.url,
            'description:', self.description
        )
        lines = str.split("\n")
        lists = (textwrap.TextWrapper(break_long_words=True).wrap(line) for line in lines)
        return "\n".join("\n".join(list) for list in lists)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, val):
        self._url = val

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, val):
        self._category = val

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, val):
        self._language = val

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, val):
        self._country = val


class Article(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __getattr__(self, item):
        self.__dict__[item] = None
        return None

    def __repr__(self):
        str = "{:10} {} \n{:10} {} \n{:10} {} \n{:10} {} \n\n{:10} {} \n\n{:10} {} \n\n{:10} {} \n\n{:10} {}\n".format(
            'author ......:', self.author,
            'published ...:', self.publishedAt,
            'source id ...:', self.source_id,
            'source name .:', self.source_name,
            'title .......:', self.title,
            'description .:', self.description,
            'url:', self.url,
            'urlToImage:', self.urlToImage
        )
        lines = str.split("\n")
        lists = (textwrap.TextWrapper(break_long_words=True).wrap(line) for line in lines)
        return "\n".join("\n".join(list) for list in lists)

    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, val):
        self._source_id = val

    @property
    def source_name(self):
        return self._source_name

    @source_name.setter
    def source_name(self, val):
        self._source_name = val

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, val):
        self._author = val

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, val):
        self._url = val

    @property
    def urlToImage(self):
        return self._urlToImage

    @urlToImage.setter
    def urlToImage(self, val):
        self._urlToImage = val

    @property
    def publishedAt(self):
        return self._publishedAt

    @publishedAt.setter
    def publishedAt(self, val):
        self._publishedAt = val
