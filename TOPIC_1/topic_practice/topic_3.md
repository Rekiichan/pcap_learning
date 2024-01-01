
# How Python Deals with Modules

When a certain module is imported for the first time, Python converts its contents into a semi-compiled code which can be used to execute module functions faster.

The semi-compiled files are placed in the directory named __pycache__, located in the same directory in which the source module exists.

If the source file of a module is named mod.py, its semi-compiled counterpart will be named mod.cpython-xy.pyc where x and y are numbers derived from your Python's version number.

## Special Built-in Variable __name__

There is a special built-in variable named __name__ whose value:
- is set to "__main__" when the module is run as a standalone code;
- is set to the source file's name (excluding .py) when the file is imported as a module.

Example: the snippet below can be used to determine the context in which the source file is used.

```python
if __name__ == "__main__":
    print("Run as a program")
else:
    print("Imported as a module")
```

## Private Entities in Modules

If the name of any module entities starts with _ or __, the entity should be treated as private and not used outside the module.

## Shebang Line

The very first line of a Python source file can start with #!, in which case it's called the shabang, shebang, hashbang, poundbang, or even the hashpling line. From Python's point of view, it's just a comment. For Unix and Unix-like OSs (including MacOS) such a line instructs the OS on how to execute the contents of the file.

Example shebang line for some environments:

```bash
#!/usr/bin/env python3
```

## Import Directives and sys.path

The module of the name given in the import directive is searched inside directories whose names are listed in the sys.path variable (it's a list of strings). The user is allowed to modify the sys.path contents in order to limit or extend the range of directories being searched through.

# Packages

A group of Python source files deployed in a certain subtree of the file system may form a package. The file structure may look like this:

```plaintext
[any directory]
    └── package
        ├── gearbox.py (contains turn_on() function)
        ├── __init__.py (empty file)
        └── subpackage
            └── engine.py (contains start() function)
```

## __init__.py and Package Initialization

A source file named __init__.py located in a certain place of the directory structure defines the root of the package. If the file is not empty, its contents will be executed when any of the package's modules is imported.

## Importing from Packages

Importing a module from within a package requires more detailed import specifications. Here are some ways to invoke functions from within a package:

```python
import package.gearbox
package.gearbox.turn_on()

# Or
from package.gearbox import turn_on
turn_on()

# Or
from package.gearbox import *
turn_on()
```

## Invoking Functions from Subpackages

Here are three ways to invoke the start() function from the engine.py module in the subpackage:

```python
# Example 1
import package.subpackage.engine
package.subpackage.engine.start()

# Example 2
from package.subpackage.engine import start
start()

# Example 3
from package.subpackage.engine import *
start()
```

Executing the imports above will provoke Python to create __pycache__ directories under the package and subpackage directories, containing .pyc files with semi-compiled code of the imported modules.
