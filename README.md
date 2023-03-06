# AirBnB clone

![hbnb](images/hbnb.png)

This project has for goal to create a simple copy of the [AirBnB website](https://www.airbnb.com/).
It will not have all the features, only some of them to cover all fundamental concepts of the higher level programming track.

This project will take four months and six steps. We are currently working on: __Web Static__


## 1st step - The Console

![console](images/console.png)

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

### Learning Objectives:
    - How to create a Python package
    - How to create a command interpreter in Python using the cmd module
    - What is Unit testing and how to implement it in a large project
    - How to serialize and deserialize a Class
    - How to write and read a JSON file
    - How to manage datetime
    - What is an UUID
    - What is *args and how to use it
    - What is **kwargs and how to use it
    - How to handle named arguments in a function
    - Serialization / Deserialization flow (object <-> Dict <-> Json <-> file)
    - Packages / Modules / Cyclical imports / How to import / Prevent execution /Etc.
    - Layered architecture
    - Interfaces (storage)
    - Abstract Classes (BaseClass)

### Requirements:

#### Python Scripts
    - Allowed editors: vi, vim, emacs
    - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	- All your files should end with a new line
	- The first line of all your files should be exactly #!/usr/bin/python3
	- A README.md file, at the root of the folder of the project, is mandatory
	- Your code should use the pycodestyle (version 2.7.*)
	- All your files must be executable
	- The length of your files will be tested using wc
	- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
	- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
	- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
	- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests
    - Allowed editors: vi, vim, emacs
    - All your files should end with a new line
    - All your test files should be inside a folder tests
    - You have to use the unittest module
    - All your test files should be python files (extension: .py)
    - All your test files and folders should start by test_
    - Your file organization in the tests folder should be the same as your project
    - e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    - e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
    - All your tests should be executed by using this command: python3 -m unittest discover tests
    - You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
    - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    - We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### How to use the Console:
- In order to run this program, you have to start by cloning this repository with:

```
git clone https://github.com/mxnctblt/holbertonschool-AirBnB_clone.git
```

- You can now use it in interactive mode by invoking:

```
./console.py
```

- Or in non-interactive mode:

```
echo "help" | ./console.py
```
```
cat test_help | ./console.py
```

### Examples:

#### In interactive mode:

- with help

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)

```

- with create

```
$ ./console.py
(hbnb) create BaseModel
a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700
(hbnb)
```

- with all

```
$ ./console.py
(hbnb) all
["[BaseModel] (a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700) {'id': 'a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700', 'created_at': datetime.datetime(2023, 2, 22, 9, 53, 38, 529981), 'updated_at': datetime.datetime(2023, 2, 22, 9, 53, 38, 529997)}"]
["[BaseModel] (a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700) {'id': 'a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700', 'created_at': datetime.datetime(2023, 2, 22, 9, 53, 38, 529981), 'updated_at': datetime.datetime(2023, 2, 22, 9, 53, 38, 529997)}"]
(hbnb)
```

#### In non-interactive mode:

- with help

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
```

- with create

```
$ echo "create BaseModel" | ./console.py
(hbnb) a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700
(hbnb)
$
```

- with all

```
$ echo "all" | ./console.py
(hbnb) ["[BaseModel] (a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700) {'id': 'a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700', 'created_at': datetime.datetime(2023, 2, 22, 9, 53, 38, 529981), 'updated_at': datetime.datetime(2023, 2, 22, 9, 53, 38, 529997), '__class__': 'BaseModel'}"]
["[BaseModel] (a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700) {'id': 'a3083ea9-f03c-4ac0-bdc4-e7d9bbb43700', 'created_at': datetime.datetime(2023, 2, 22, 9, 53, 38, 529981), 'updated_at': datetime.datetime(2023, 2, 22, 9, 53, 38, 529997), '__class__': 'BaseModel'}"]
(hbnb)
$
```

## 2nd step - Web static

![webstatic](images/webstatic.png)
- learn HTML/CSS
- create the HTML of your application
- create template of each object

## 3rd step - MySQL storage

![mysqlstorage](images/mysql.png)

- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

## 4th step - Web framework - templating

![webframework](images/webframework.png)

- create your first web server in Python
- make your static HTML file dynamic by using objects stored in a file or database

## 5th step - RESTful API

![resfulapi](images/restfulapi.png)

- expose all your objects stored via a JSON web interface
- manipulate your objects via a RESTful API

## 6th & last step - Web dynamic

![webdynamic](images/webdynamic.png)

- learn JQuery
- load objects from the client side by using your own RESTful API

## Authors:
Antoine Jacob <[AntoineJacob](https://github.com/AntoineJacob)>
& Maxence Thibault <[mxnctblt](https://github.com/mxnctblt)>
