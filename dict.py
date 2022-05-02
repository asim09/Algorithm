# class SoftwareEngineer:
#
#     def __init__(self,name, age, designation, salary):
#         self.name = name
#         self.age = age
#         self.designation = designation
#         self.salary = salary
#
#     def code(self):
#         print(f"{self.name} is writing code....")
#
#     def code_language(self, language):
#         print(f"{self.name} is working in {language}...")
#
#     def information(self):
#         print(f'{self.name} is a {self.designation}')


# se1 = SoftwareEngineer('Asim', 34, 'Consultant', 'xxxxx')
# se2 = SoftwareEngineer('Asim', 34, 'Consultant', 'xxxxx')

# print(se1.code())
# print(se2.code_language('Pythion'))
# print(se2.information())


def is_armstrong(num):
    degree = len(str(num))
    number_sum = sum([pow(int(i), degree) for i in str(num)])
    print(number_sum, num)
    return True if number_sum == num else False


# print(is_armstrong(371))
# from operator import mul
# from functools import reduce
#
#
# def factorial(num):
#     if num < 1:
#         return 'wrong value'
#     fact = reduce(mul, [i for i in range(1, num + 1)]) if num > 1 else 1
#     return fact
#
#
# num = -1
# print(factorial(num))


str = 'malayalam1my'

# index = - 1
# flag = 1
# for elem in str:
#     print(elem + '-------' + str[index])
#
#     if elem != str[index]:
#         flag = 0
#         break
#     index = index - 1
#
# if flag:
#     print('---tes')
# else:
#     print('---No')

# rev_str = str[::-1]
# # print(rev_str)
# if rev_str == str:
#     print('Y')

def is_prime(num):
    flag = True
    if num <= 1:
        flag = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
    return flag


print(is_prime(8))















