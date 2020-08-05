# Books REST API
Recruitment task for STXnext

**What you can do:**

- display all books http://127.0.0.1:8000/books
- filter books by author or published date 
http://127.0.0.1:8000/books/?search=2008
http://127.0.0.1:8000/books/?search=Tolkien
- view, update or destroy single book http://127.0.0.1:8000/books/1
- add books from google API using provided keywords
http://127.0.0.1:8000/import_book with body {"keywords":"<e.g. war>"}



**Base URL**
base URL for all endpoints: https://paulina12books.herokuapp.com/

- display all books https://paulina12books.herokuapp.com/books
- filter books by author or published date 
https://paulina12books.herokuapp.com/books/?search=2008
https://paulina12books.herokuapp.com/books/?search=Tolkien
- view, update or destroy single book https://paulina12books.herokuapp.com/books/1
- add books from google API using provided keywords
https://paulina12books.herokuapp.com/import_book with body {"keywords":"<e.g. war>"}