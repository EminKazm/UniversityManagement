from Staff.librarian import Librarian
class Library:
    """This class contains the details of a particular library in the university"""
    def __init__(self, library_id,totalbooks,):
        self._library_id=library_id
        self.total_books=totalbooks
        self.librarian=Librarian("03","Ilgar",43,500,100)
    def infoLibrary(self):
        return f"Library id:{self._library_id},total books:{self.total_books}"
    def searchbooks(self):
        for book in self.total_books:
            print(book)
    def lendbooks(self,requestedbook):
        if requestedbook in self.total_books:
            print("You can borrow this book,it is available")
        else:
            print("sorry,this book is already finished in our library.")

    def returnbook(self,returnedbook):
        self.total_books.append(returnedbook)




