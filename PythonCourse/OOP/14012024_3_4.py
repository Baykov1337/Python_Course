# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def Name(self,new_name):
#         self._name = new_name
#         return new_name
    
#     def Age(self,New_age):
#         self._age = New_age
#         return New_age
#     def output_name(self):
#         return self._name
#     def outut_age(self):
#         return self._age
    
# test = Person("teee",211)
# print (test.output_name())
# print (test.Name('asdasdasd'))

class Book: 
    def __init__(self, title, author): 
        self.title = title 
        self.author = author 
class Library: 
    def __init__(self): 
        self.shelf = [] 
    def add_book(self, shelf): 
            self.shelf.append(shelf) 
    def display(self): 
            for shelf in self.shelf: 
                print(f"Title: {shelf.title}, Author: {shelf.author}") 

Bookshelf1 = Book("Python Programming", "John Doe") 
Bookshelf2 = Book("Data Science Basics", "Jane Smith") 
library = Library() 
library.add_book(Bookshelf1) 
library.add_book(Bookshelf2) 
library.display()
    