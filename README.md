### A simple CRUD API post, comment, like management web app using Django Rest Framework, PostgreSQL, docker-compose.

####Stack:
* API: Django Rest Framework
    * PostgreSQL
    * Docker

###Methods

* GET (Returns list of objects. Takes a /int:pk argument to get the detail view.)
    * /posts
    * /comments
    * /likes
* POST
    * /posts : *title* - string, *author* - int, *link* - string  
    * /comments: *content* - string, *author* - int, *post* - int
    * /likes: *post* - int, *author*: int 

[Test it here](http://www.reppon.live/)

### Usage

To run:

```
make docker-up
```

Code formatted with [Black](https://github.com/psf/black) and is passing [Flake8](https://gitlab.com/pycqa/flake8) linter.

[Postman Collection Link](https://www.getpostman.com/collections/db8adae66e6a10059a4a)