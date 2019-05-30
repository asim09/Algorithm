# count = 0
# file_number = 1
# f = open("local_cities" + str(file_number) + ".txt", "w+")
# while count < len(local_cities):
#     if count % size != 0:
#         f.write("This is line %s\r\n" % (local_cities[count]))
#     else:
#         f.close()
#         f = open("local_cities" + str(file_number) + ".txt", "w+")
#         f.write("This is line %s\r\n" % (local_cities[count]))
#         file_number = file_number + 1
#     count = count + 1
# f.close()







# for i in range(length):
#     f = open("local_cities"+str(count)+".txt", "w+")
#     for item in range(initial, size):
#         f.write("This is line %s\r\n" % (local_cities[item]))
#         print('times', local_cities[item])
#
#     initial = size
#     diff = len(local_cities) - size
#     if diff < 5:
#         size = size +  diff
#     else:
#         size = size + 5
#     count = count + 1
