first_num = 9
second_num = 7.8                         #задание 1
my_str = 'start'

print(first_num, second_num, my_str)


first_num = 5.2
print(first_num, type(first_num))

third_num = first_num + second_num
print(third_num, type(third_num))

first_num +=5
second_num += first_num
print( first_num, second_num)

second = int(second_num)
print(second, first_num)


my_str += '&stop'
print(my_str)

my_str +=5
print(my_str)




                #задание 2
path = 'C:\\Users\\MainAdmin\\Desktop\\programs'
print(path)

path += '\\game.exe'
print(path)

path = 'C:\\Users\\MainAdmin\\Desktop\\files'
path += '\\picture.png'
print(path)

path = 'C:\\Games\\city simulator'
print(path)
error_path = path * 2
print('error path:', error_path)
