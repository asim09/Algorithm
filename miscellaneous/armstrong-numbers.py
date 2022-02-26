def is_armstarong_number(value):
   string_number = str(value)
   power = len(string_number)

   sum = 0
   for i in string_number:
      sum = sum + pow(int(i), power)
   if sum == value:
      print(value)

for i in range(50001):
   is_armstarong_number(i)
