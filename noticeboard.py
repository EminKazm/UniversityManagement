class NewsBoard:
    """This class is about news of university
        it has news attribute
        """
    def __init__(self):
        self.news_list = list()

    def addnews(self,news):

        self.news_list.append(news)
    def display(self):
        for item in self.news_list:
            return item


