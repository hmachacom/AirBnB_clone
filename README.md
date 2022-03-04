# <h1 align="center">AirBnB clone - The console</h1>

<p align="center">
  <img src="https://github.com/hmachacom/AirBnB_clone/blob/main/images/logohbnb.png" alt="HolbertonBnB logo">
</p>

# :pencil: Description 

In this project we make a complete web application, integrating database storage,
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.


# :book: Files and Directories 

- `models` -> directory contains all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.

- `tests` -> directory contains all unit tests.
console.py file is the entry point of our command interpreter.

- `models/base_model.py` ->  file is the base class of all our models. It contains common elements:
    - attributes: `id, created_at` and `updated_at`
    - methods: `save()` and `to_json()`

- `models/engine`models/engine directory will contain all storage classes (using the same prototype). For the moment we have only one: `file_storage.py`.

# Storage

In this project, we manipulate 2 types of storage: file and database. For the moment, we only work whit file. 

# :computer: The Console 

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

<p align="center">
  <img src="https://github.com/hmachacom/AirBnB_clone/blob/main/images/img2.png" alt="HolbertonBnB logo">
</p>

# :pencil: Commands and how to use it :paper:

## Commands

### Using the console

|Command | Description | Use | 
| create | Create an instance (object) and print its id. | create <class name>|
| show | Prints the string representation of an instance based on the class name and id. | show <class name> <id>|
| destroy | Deletes an instance based on the class name and id | destroy <class name> <id>|
| all | 	Prints all string representation of all instances based or not on the class name. | all <class name> |
| update | Updates an instance based on the class name and id by adding or updating attribute. | update <class name> <id> <attribute name> "<attribute value>"|
| quit and EOF | exit the program | quit or EOF|
| help | This action is provided by cmd by default, but should be kept up to date and documented. | help|
| ------ | ----------- | ----|

- The console run in:

### Non-Interactive Mode

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
```
and

### Interactive Mode

```
$ ./console.py
```
console displays a prompt `(hbnb)`

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

## Testing 

All files, classes, functions be tested with unit tests

```
$ python3 -m unittest discover tests
```
Unit tests must also pass in non-interactive mode:

```
$ echo "python3 -m unittest discover tests" | bash
```

## :person: Authors 
* **Hugo Machacon** <[hmachacon](https://github.com/hmachacom)>
* **Carolina Espitia** <[caritoespicaita](https://github.com/caritoespicaita)>