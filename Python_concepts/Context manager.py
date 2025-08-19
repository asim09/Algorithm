'''
Why Use a Context Manager?

Context managers help manage resources that need to be acquired and released. A typical use case is managing **resources** such as:
- Files
- Database connections
- Network connections
- Locks
- Memory

   open() is a built-in context manager for files.
🔹 @contextmanager is more flexible and can be used for other resources.
🔹 If you're only working with files, just use open(). But if you need extra functionality or 
    different resource management, go with @contextmanager
'''

'''
Example: Using a Context Manager with with Statement
'''
with open("example.txt", "w") as file:
    file.write("Hello, Context Manager!")
# File is automatically closed after the block ends


'''
✅ Here, open() acts as a context manager:

__enter__() opens the file.
__exit__() closes the file when with block ends.
'''


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file  # Return the file object for use inside the 'with' block

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_value}")
        return True  # Suppresses exception if one occurs inside 'with' block


# Using the custom context manager
with FileManager("test.txt", "w") as f:
    f.write("Learning Context Managers!")
