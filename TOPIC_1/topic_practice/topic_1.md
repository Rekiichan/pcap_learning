
# Understanding Namespaces, Modules, and Packages, Math in Python

## Namespace
A namespace is a space (understood in a non-physical context) in which some names exist and the names don't conflict with each other (i.e., there are no two objects with the same name).

## Module
A module is a file containing Python definitions and statements which can be imported and used by another Python code.

## Package
A package is a way of structuring a module's namespace by using dotted module names. It can be said that the module is a hierarchical collection of modules.

## Importing Modules
To import a module and to make its content available, the `import` directive is used. Let's assume that there is a module named `mod` which contains a function named `fun()`. The following import forms can be used:

### import mod
- The clause contains the `import` keyword followed by the name of the imported module (or a comma-separated list of names).
- When any of the imported module's entities (variables, functions, classes, etc.) should be used, its name must be encoded in the dotted (qualified) form, e.g., `mod.fun()`.

### from mod import fun
- The clause starts with the phrase `from module_name` followed by the name (or a comma-separated list of names) of the imported module's entity/entities.
- When any of the imported names is used inside the code, its name must be used as is, without any dots or qualification, e.g., `fun()`.
- Note: unless you know all the names provided by the module, you may not be able to avoid name conflicts inside your current namespace.

### from mod import *
- The clause is similar to the previously presented variant but uses an asterisk (*) instead of any explicit name/names. The asterisk works as a wild card and implicitly imports all the module's entities.
- The names of any of the imported entities must be used as is – no qualification is allowed.

## Inspecting Modules
A built-in function named `dir()` can be used to obtain an alphabetically sorted list which contains all entity names available in the module passed to the function as an argument, e.g., `print(dir(math))` will print a list of the math module's contents.

## Math Module in Python

The `math` module comes with the standard Python release and contains some useful constants and functions for carrying out mathematical operations. Note: all trigonometrical functions take their arguments expressed in radians.

- `math.pi` → π constant value.
- `math.e` → Euler's number value.
- `math.sqrt(x)` → the square root of x.
- `math.sin(x)` → the sine of x.
- `math.cos(x)` → the cosine of x.
- `math.tan(x)` → the tangent of x.
- `math.asin(x)` → the arcsine of x.
- `math.acos(x)` → the arccosine of x.
- `math.atan(x)` → the arctangent of x.
- `math.radians(x)` → a function that converts x from degrees to radians.
- `math.degrees(x)` → acting in the other direction (from radians to degrees).
- `math.sinh(x)` → the hyperbolic sine.
- `math.cosh(x)` → the hyperbolic cosine.
- `math.tanh(x)` → the hyperbolic tangent.
- `math.asinh(x)` → the hyperbolic arcsine.
- `math.acosh(x)` → the hyperbolic arccosine.
- `math.atanh(x)` → the hyperbolic arctangent.
- `math.exp(x)` → finds the value of e^x.
- `math.log(x)` → the natural logarithm of x.
- `math.log(x, b)` → the logarithm of x to base b.
- `math.log10(x)` → the decimal logarithm of x (more precise than `math.log(x, 10)`).
- `math.log2(x)` → the binary logarithm of x (more precise than `math.log(x, 2)`).
- `math.ceil(x)` → the ceiling of x (the smallest integer greater than or equal to x).
- `math.floor(x)` → the floor of x (the largest integer less than or equal to x).
- `math.trunc(x)` → the value of x truncated to an integer (be careful – it's not an equivalent of either ceil or floor).
- `math.factorial(x)` → returns x! (x has to be an integral and not a negative).
- `math.hypot(x, y)` → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as `math.sqrt(pow(x, 2) + pow(y, 2))` but more precise).
