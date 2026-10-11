class Book:
    def __init__(self,title,author,book_id,is_available=True):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = is_available

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Book ID: {self.book_id}")
        print(f"Available: {self.is_available}")

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        for i in self.books:
            if(i.book_id == book.book_id):
                print("Book is already present")
                return
        self.books.append(book)
        print("Book added successfully")
            
    def display_books(self):
        for i in self.books:
            i.display_info()

    def issue_book(self,book_id):
        for book in self.books:
            if(book.book_id==book_id):
                if(book.is_available):
                    print("Book issued successfully")
                    book.is_available=False
                else:
                    print("Book is not available")
                break
        else:
         print("Book not found")

    def return_book(self,book_id):
        for book in self.books:
            if(book.book_id == book_id):
                if( not book.is_available):
                    print("Book returned successfully")
                    book.is_available = True
                else:
                    print("Book is already available ")
                break
        else:
            print("Book not found")

    def search_book(self,title):
        for book in self.books:
            if(book.title.lower() == title.lower()):
                book.display_info()
                break
        else:
            print("Book not found")        

                
book1 = Book("The Magic of the last Earings","Sudha Murthy",120)
book2 = Book("Wings of Fire", "A. P. J. Abdul Kalam", 121)
book3= Book("The Alchemist", "Paulo Coelho", 122)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.issue_book(120)
library.issue_book(120)
library.return_book(120)
library.return_book(120)
library.issue_book(999)
library.search_book("Harry Potter")
library.search_book("Wings of Fire")


