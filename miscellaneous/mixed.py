#check if palindrome
input = 'malayalam'
str = 'malayalam'

index = - 1
flag = 1
for elem in str:
    print (elem + '-------' +str[index])

    if elem != str[index]:
        flag = 0
        break
    index = index - 1

if flag:
    print('---tes')
else:
    print('---No')


#Reverse str

str = "geeks quiz practice code"

temp = ''
list = str.split(' ')
# print(list)
for i in list:
    temp = i +' ' +  temp
temp = temp.rstrip()
print(len(temp))
print(temp)


#pop i-th element:
test_str = "GeeksForGeeks"
new_str = ''

for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print(new_str)


#sort all 0 at left

arr = [0,1,1,1,0,1,0]


n = len(arr)
count = 0

for i in range(0, n):
    if arr[i] == 0:
        count+=1

for i in range(0,count):
    arr[i] = 0

for i in range(count,n):
    arr[i] = 1
