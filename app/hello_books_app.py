library = []
class Book:

    def __init__(self, book_name, number, category):
        self.book_name = book_name
        self.number = number
        self.category = category 

    def add_book(self, book_name, number, category):
        '''
        This method validates addition of new book
        '''
        book={
            'name': book_name,
            'book_number': number,
            'book_category': category
        }
        library.append(book)
        return 'Book added successfully'

    def remove_book(self, number):
        '''
        This method validates removal of book from the library 
        '''
        for book in library:
            if book['book_number'] = number:
                library.remove(number)
            else:
                return 'Please enter valid book number'
        return 'Book removed successfully'

    def modify1_book(self, number):
        '''
        This method validates book information modificaation
        '''
        for item in library:
            if item['book_number'] = number:
                value=input('Enter bn to modify book number \or cat to modify category')
                if value = 'bn':
                    new_name=input('Enter new book_name')
                    item['name'] = new_name
                elif value = 'cat':
                    ctg=input('Enter new category')
                    item['book_category'] = ctg
                else:
                    return 'invalid input, please confirm input and try again'
            else:
                return 'Enter valid book number'

    def retrieve_books(self):
        '''
        This method validates retrieval of all books from the library
        '''
        if len(library) == 0:
            return 'No books are available in library'
        else:
            return library

    def get_book(self, number):
        '''
        This method validates retrieval of one book from the librarys
        '''
        for book in library:
            if book['number'] == number:
                return book
            else:
                return 'Invalid input, please confirm input and try again'

    def borrow_book(self, number):
        for book in library:
            if book['number'] == number:
                return ('Book available')
            else:
                return ('Book currently unavailable')


    

    

    

        

    
        
