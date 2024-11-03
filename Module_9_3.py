first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result=(abs(len(i[0])-len(i[1])) for i in zip(first,second) if (len(i[0])-len(i[1])!=0))
second_result=(len(first[i])==len(second[i]) for i in range(0,len(first)))
# second_result=[]
# for i in range(0,len(first)):
#     comp=len(first[i])==len(second[i])
#     second_result.append(comp)

print(list(first_result))
print(list(second_result))