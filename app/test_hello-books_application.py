from hello_books_app import Book 
import unittest 


class BookTest(unittest.TestCase):
   def setUp(self):
       self.sample = Book("grit", 56, "academic")
       self.sample1("top", 67, "comical")
       self.sample2("rest", 78, "newspaper")
       self.sample3("tech", 315, "academic")
       self.sample4("space", 31, "scifi")
       self.sample5("Holy Bible", 15, "religious")       
       
   def test_book_name(self):
       self.assertEqual(self.sample.book_name, "grit", msg="Error on book name")
       self.assertEqual(self.sample1.book_name, "top", msg="Error on book name")
       self.assertEqual(self.sample2.book_name, "rest", msg="Error on book name")
       self.assertEqual(self.sample3.book_name, "tech", msg="Error on book name")
       self.assertEqual(self.sample4.book_name, "space", msg="Error on book name")
       self.assertEqual(self.sample5.book_name, "Holy Bible", msg="Error on book name")       

   def test_number(self):
       self.assertEqual(self.sample.number, 56, msg="Error on book number")
       self.assertEqual(self.sample1.number, 67, msg="Error on book number")
       self.assertEqual(self.sample2.number, 78, msg="Error on book number")
       self.assertEqual(self.sample3.number, 315, msg="Error on book number")
       self.assertEqual(self.sample4.number, 31, msg="Error on book number")
       self.assertEqual(self.sample5.number, 15, msg="Error on book number")
       
   def test_category(self):
       self.assertEqual(self.sample.category, "academic", msg="Error on book category")
       self.assertEqual(self.sample1.category, "comical", msg="Error on book category")
       self.assertEqual(self.sample2.category, "newspaper", msg="Error on book category")
       self.assertEqual(self.sample3.category, "academic", msg="Error on book category")
       self.assertEqual(self.sample4.category, "scifi", msg="Error on book category")
       self.assertEqual(self.sample5.category, "religious", msg="Error on book category")
       



