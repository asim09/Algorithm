'''
#################
## Iterator
#################
1. What is an Iterator?

An iterator is an object that represents a stream of data. 
You can iterate over it (or traverse it) one item at a time. 
An object is considered an iterator if it implements two methods:

__iter__(): This method returns the iterator object itself.
__next__(): This method returns the next item in the sequence. 
If there are no more items, it raises the StopIteration exception.
'''
'Example:'


# Example of an iterator

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


# Create an iterator from 0 to 4
my_iter = MyIterator(0, 5)
for num in my_iter:
    print(num)

'''
#################
## Generator
#################
2. What is a Generator?
A generator is a special type of iterator that is defined using a function with one 
or more yield statements. A generator function allows you to declare a 
function that behaves like an iterator, and you don’t need to explicitly 
implement the __iter__() and __next__() methods.

Whenever the yield statement is encountered, the function's state is "paused," and 
the value is returned to the caller. The function can be resumed from where it left off 
when __next__() is called again.

Example:1 -: Infinite Sequences
Generators are useful for creating infinite sequences, such as generating Fibonacci numbers.
'''


# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Generate first 10 Fibonacci numbers
fib = fibonacci()
for _ in range(10):
    print(next(fib))

"Example 2: Read very large file using generators"


def read_large_file(file_path, chunk_size=1024 * 1024):
    """
    A generator function to read large files in chunks.

    :param file_path: The path to the file to be read.
    :param chunk_size: The size of the chunk to read at a time (in bytes).
    :yield: A chunk of the file at a time.
    """
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)  # Read a chunk of data
            if not chunk:
                break  # End of file reached
            yield chunk  # Yield the chunk for processing


# Example usage:
file_path = "large_file.txt"

for chunk in read_large_file(file_path):
    # Example: Processing the chunk, e.g., converting bytes to text
    try:
        print(chunk.decode('utf-8')[:100])  # Try decoding if it's a text file
    except UnicodeDecodeError:
        # Handle cases where the chunk isn't valid UTF-8 text
        pass

'''
Key Differences Between Iterators and Generators
Memory Efficiency: Iterators need to store all the items in memory. 
Generators produce items one at a time and only when required, making 
them more memory-efficient.
Stateful Execution: In a generator, the state of the function 
is "saved" between calls to yield. With regular iterators, the 
state must be manually handled.
'''
"********************************************************************"


def prime_generator():
    """
    Yields an infinite sequence of prime numbers.
    """
    primes = []
    num = 2
    while True:
        if all(num % p != 0 for p in primes):
            primes.append(num)
            yield num
        num += 1


# Example Usage:
gen = prime_generator()
for _ in range(10):
    print(next(gen))  # Outputs: 2, 3, 5, 7, 11, 13, ...
