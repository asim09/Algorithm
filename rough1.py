def check_eligibility(age):
    if not isinstance(age, int) or age < 0:
        return "Invalid input. Age must be a non-negative integer."
    if age < 18:
        return "Not eligible."
    else:
        return "Eligible."

age = int(input("Enter your age: "))
# result = check_eligibility(age)
# print(result)
age = int(input("Enter your age: "))
if age < 18:
        print( "Not eligible.")
else:
    print( "eligible.")

# age = int(input("Enter your age: "))


# from dataclasses import dataclass, field

# def gen_id()->str:
#     return 'asim_id'


# @dataclass
# class Person:
#     name: str
#     price: int
#     active: bool = True
#     email_add: list[str] = field(default_factory=list)
#     id: str = field(init=False, default_factory=gen_id)
          
# def main()-> None:
#     p =  Person(name='asim', price=300000, active=False)
#     print(p)
    
    
# if __name__ == '__main__':
#     main()
    