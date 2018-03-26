library = []


class Book:

    def __init__(self, book_name, number, category):
        self.book_name = book_name
        self.number = number
        self.category = category 

    def add_book(self, book_name, number, category):
        book={
            'name': book_name,
            'book_number': number,
            'book_category': category
        }
        library.append(book)
        return 'Book added successfully'

    def remove_book(self, number):
        for book in library:
            if book['book_number'] = number:
                library.remove(number) 
        return 'Book removed successfully'

    def modify_book(self, number):
        for item in library:
            if item['book_number'] = number:
                value=input('Enter bn to modify book number \or cat to modify category')
                if value = 'bn':
                    nme=input('Enter new book_name')
                    item['name'] = nme
                elif value = 'cat':
                    ct=input('Enter new category')
                    item['book_category'] = ct
                else:
                    return 'invalid input, please confirm input and try again'
            else:
                return 'Enter valid book number'

    def retrieve_book(self):
        if len(library) == 0:
            return 'No books are available in library'
        else:
            return library

    def get_book(self, number):
        for book in library:
            if book[number] == number:
                return book
            else:
                return 'Invalid input, please confirm input and try again'



    

    

    

        

    
        
