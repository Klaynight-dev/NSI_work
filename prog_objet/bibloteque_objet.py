class Book:
    def __init__(self, title, author, isbn, nbr_cp):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.nbr_cp = nbr_cp
    
class Librairy:
    def __init__(self):
        self.title  = []
        self.author = []
        self.isbn   = []
        self.nbr_cp = []
    
    def add(self, book):
        self.title.append(book.title)
        self.author.append(book.author)
        self.isbn.append(book.isbn)
        self.nbr_cp.append(book.nbr_cp)
        
    def take(self, book):
        
#     def drop(self, book):
#         
#     def imp(self, book):
        
def creerLivre(nbr):
    return 
livre = Book("coucou", "c'est moi", 5648745, 5)

listeBook.append(livre)

lib = Librairy()

lib.add(livre)

print(lib.title[0])