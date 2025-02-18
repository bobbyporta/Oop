class Book:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def describe(self):
        print(f"Book Title     : {self.title}")
        print(f"Author         : {self.author}")
        print(f"Year published : {self.year}\n")


book1 = Book("The Fault in Our Stars", "John Green", 2012)
book1.describe()

book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2.describe()

book3 = Book("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", 2017)
book3.describe()
