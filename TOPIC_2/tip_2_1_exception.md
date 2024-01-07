
# Python Exceptions Hierarchy Review

Understanding the hierarchy of exceptions is crucial for effective error handling in Python. Below is a detailed overview of the built-in exceptions hierarchy.

## BaseException
All built-in, non-system-exiting exceptions are derived from this class. It's the base class for all built-in exceptions except for SystemExit, GeneratorExit, KeyboardInterrupt.

### Main Subclasses
- **Exception**: All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.
  - **ArithmeticError**: Base class for arithmetic errors.
    - **OverflowError**: Raised when the result of an arithmetic operation is too large to be represented.
    - **ZeroDivisionError**: Raised when the second argument of a division or modulo operation is zero.
    - **FloatingPointError**: Raised when a floating-point operation fails.
  - **BufferError**: Raised when a buffer-related operation cannot be performed.
  - **LookupError**: Base class for lookup errors.
    - **IndexError**: Raised when an index is not found in a sequence.
    - **KeyError**: Raised when a key is not found in a dictionary.
  - **AssertionError**: Raised when an assert statement fails.
  - **AttributeError**: Raised when an attribute reference or assignment fails.
  - **EOFError**: Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data.
  - **ImportError**: Raised when an import statement fails.
    - **ModuleNotFoundError**: Raised by `import` when a module could not be located.
  - **MemoryError**: Raised when an operation runs out of memory.
  - **NameError**: Raised when a local or global name is not found.
    - **UnboundLocalError**: Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
  - **OSError**: Raised when a system operation causes a system-related error.
    - **FileNotFoundError**: Raised when a file or directory is requested but doesn't exist.
    - **PermissionError**: Raised when trying to run an operation without the adequate access rights.
    - ... and many more.
  - **ReferenceError**: Raised when a weak reference proxy is used to access a garbage collected referent.
  - **RuntimeError**: Raised when an error is detected that doesn’t fall in any of the other categories.
    - **RecursionError**: Raised when the maximum recursion depth is exceeded.
  - **StopIteration**: Raised by `next()` to signal that there are no further items produced by the iterator.
  - **SyntaxError**: Raised when a parser encounters a syntax error.
    - **IndentationError**: Base class for syntax errors related to incorrect indentation.
      - **TabError**: Raised when indentation consists of inconsistent tabs and spaces.
  - **SystemError**: Raised when the interpreter finds an internal error.
  - **TypeError**: Raised when an operation or function is applied to an object of inappropriate type.
  - **ValueError**: Raised when an operation or function receives an argument that has the right type but an inappropriate value.
  - **Warning**: Base class for warning categories.
    - **DeprecationWarning**: Base class for warnings about deprecated features.

This overview is not exhaustive but covers the most common exceptions you're likely to encounter. For a comprehensive list, refer to the [Python documentation](https://docs.python.org/3/library/exceptions.html). Understanding these will help you handle errors more effectively and write more robust code.
