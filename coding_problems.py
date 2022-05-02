f"1 - Find the first non repeating element from string example: 'SILVER FOR SILVER'."
f"2-Write a program to delete second occurence of a element in a list."
f"3 - find prime num between 100 to 200"






f"3 - find prime num between 100 to 200"
def foo():
    for num in range(100, 200):
        if all(num %i !=0 for i in range(2,num)):
            print(num)
foo()