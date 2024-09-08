tabl = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
tabl_new=[]
n = int(input ('Введите число от 3 до 20: '))
for i in range(1,n):
    for j in range(i+1,n):
        k=i+j
        d=n%k
        if d==0:
            tabl_new.extend([i,j])
list_new = ''.join(map(str,tabl_new))
print(f'Пароль: {list_new}')