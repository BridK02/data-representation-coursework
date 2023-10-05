#Exercise 1.1b
#by Brid Kennedy

#Create an XML file that stores data for a library.
#The library has two catalogues (technical books, and for cookery books).
#Each catalogue can contain a number of books (say 2 for the purpose of this exercise) . 
#Books will have an ISBN, title and author.
#Upload your .xml file to your github repository called data-representation-coursework and copy your link here:


#Library 1 is manually created, library 2 contains the same book but is generated using minidom
#Retrieved some technial and cookery book details from https://isbnsearch.org/search?s=category+technical
#Technical Training Basics, 2nd Ed,Author: Wakefield, Sarah, ISBN-13: 9781950496358
#Category Theory for the Sciences (Mit Press), Author: Spivak, David I., ISBN-13: 9780262028134

#Practical Cookery: A Compilation of Principles of Cookery and Recipes
#Authors: Kansas State University - Kansas, ISBN-13: 9780471456414
#Miso Tasty: Everyday, tasty recipes with miso – the Japanese superfood
#Author: Chung, Bonnie,ISBN-13: 9781910904619

import xml.dom.minidom as minidom # to parse

# Create the root element
library = minidom.Document()
root = library.createElement("library")
library.appendChild(root)

# Create the technical catalogue
technical_catalogue = library.createElement("catalogue")
technical_catalogue.setAttribute("type", "technical")
root.appendChild(technical_catalogue)

# Add technical books
def create_book(isbn, title, author):
    book = library.createElement("book")
    
    isbn_element = library.createElement("isbn")
    isbn_text = library.createTextNode(isbn)
    isbn_element.appendChild(isbn_text)
    
    title_element = library.createElement("title")
    title_text = library.createTextNode(title)
    title_element.appendChild(title_text)
    
    author_element = library.createElement("author")
    author_text = library.createTextNode(author)
    author_element.appendChild(author_text)
    
    book.appendChild(isbn_element)
    book.appendChild(title_element)
    book.appendChild(author_element)
    
    return book

technical_catalogue.appendChild(create_book("9781950496358", "Technical Training Basics, 2nd Ed", "Wakefield, Sarah"))
technical_catalogue.appendChild(create_book("9780262028134", "Category Theory for the Sciences (Mit Press)", "Spivak, David I."))

# Create the cookery catalogue
cookery_catalogue = library.createElement("catalogue")
cookery_catalogue.setAttribute("type", "cookery")
root.appendChild(cookery_catalogue)

# Add cookery books
cookery_catalogue.appendChild(create_book("9780471456414", "Practical Cookery: A Compilation of Principles of Cookery and Recipes", "Kansas State University - Kansas"))
cookery_catalogue.appendChild(create_book("9781910904619", "Miso Tasty: Everyday, tasty recipes with miso – the Japanese superfood", "Chung, Bonnie"))

# Serialize the XML to a string
xml_string = library.toprettyxml(indent="    ")

# Save the XML to a file
with open("library2.xml", "w", encoding="utf-8") as xml_file:
    xml_file.write(xml_string)

print("XML file 'library2.xml' has been created successfully.")
