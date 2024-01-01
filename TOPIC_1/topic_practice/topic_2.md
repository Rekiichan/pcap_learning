
# The random module

The random module delivers some mechanisms allowing you to operate with pseudorandom numbers.

A random number generator takes a value called a seed, treats it as an input value, calculates a "random" number based on it (the method depends on the chosen algorithm) and produces a new seed value. The length of a cycle in which all seed values are unique may be very long, but it is finite – sooner or later the seed values will start repeating, and the generating values will repeat, too. The initial seed value, set during the start of the program, determines the order in which the generated values will appear.

## The seed() function
The seed() function directly sets the generator's seed. Possible variants of its invocation are:
- `seed()` – sets the seed with the current time which makes the seed a bit unpredictable;
- `seed(int_value)` – sets the seed with the integer value `int_value`.

## The random module's pseudorandom generator functions
- `random()` → produces a float number x, which falls within the range 0.0 ≤ x < 1.0.
- `random.randrange(start, stop, step)` → produces an integer number x, which is taken from the range start ≤ x < stop with step step.
- `random.randint(start, stop)` → equivalent of `random.randrange(start, stop+1)`;
- `choice(sequence)` → chooses a "random" element from the input sequence (e.g. a list or tuple) and returns it;
- `sample(sequence, elements_to_choose=1)` → returns a list (a sample) consisting of the `elements_to_choose` elements "drawn" from the input sequence.

# The platform module

The platform module lets you access the underlying platform's data, that is, the hardware, the operating system, and the interpreter version information.

## Some of the module's functions are:
- `platform.platform(aliased = False, terse = False)` → returns a string describing the underlying hardware architecture and OS.
    - `aliased` → when set to True it may cause the function to present the alternative underlying layer names.
    - `terse` → when set to True it may convince the function to present a briefer form of the result.
- `platform.machine()` → returns a string with the generic name of the host processor.
- `platform.processor()` → returns a string with the real name of the host processor.
- `platform.system()` → returns a string with the generic name of the host OS.
- `platform.version()` → returns a string with the version of the host OS.
- `platform.python_implementation()` → returns a string denoting the Python implementation.
- `platform.python_version_tuple()` → returns a three-element tuple filled with the major part of Python's version, the minor part, and the patch level number.

The complete list of currently available, community-led Python modules can be found [here](https://pypi.org/).
