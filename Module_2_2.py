first = input ('Введите число:')
second = input ('Введите еще одно число: ')
third = input ('Введите третье число: ')
if first == second and second == third:
   print(3)
elif first == second:
   print (2)
elif second == third:
   print (2)
elif third == first:
   print (2)
else:
   print (0)