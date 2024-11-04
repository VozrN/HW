first = 'Мама мыла раму'
second = 'Рамена мало было'

result=list(map(lambda x,y: x==y, first, second))
print(result)

def get_advanced_writer(file_name):
    file=open(file_name,'w')
    file.close()
    def write_everything(*data_set):
        file=open(file_name,'a',encoding='utf-8')
        for i in data_set:
            file.write(str(i)+'\n')
        file.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])