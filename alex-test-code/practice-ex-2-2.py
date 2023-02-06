class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self._price = price
        self.copies = copies

    def display(self): 
        print('ISBN', self.isbn, 'Title', self.title, 'Price', self.price, 'Copies', self.copies)

    def in_stock(self):
        return (self.copies > 0)

    def sell(self):
        if in_stock() == True:
            self.copies -= 1
        else:
            print('Out of stock')
    
    @property
    def price(self):
        return min(max(self._price, 50), 1000)
    
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 2000,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book_list = [book1, book2, book3, book4]
for book in book_list:
    book.display()

books_by_jack = [book for book in book_list if book.author == 'Jack']