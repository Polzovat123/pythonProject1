def add_new_website():
    add_new_in_sys_file()
    add_new_in_text_link()

def add_new_in_sys_file():
    add_to_sys_file_to_acsses()
    add_to_sys_file_to_text_link()

def add_new_in_text_link():
    print('Ввод тегов и классов')
    add_to_text_link_to_atribute_for_header()
    add_to_text_link_to_atribute_for_link()
    add_to_text_link_to_atribute_for_news()

#change sys file
def add_to_sys_file_to_text_link():
    s = str(input('Здесь писать часть ссылки(или ничего), для формирования полной ссылки перехода:'))
    add_new_element(path='sys_file/text_link.txt', var=s)

def add_to_sys_file_to_acsses():
    s = str(input('Здесь писать ссылку куда надо подключиться для отбора первичной информации:'))
    add_new_element(path='sys_file/text_link.txt', var=s)

#change_text_link
def add_to_text_link_to_atribute_for_link():
    print('Сейчас заполняем поля для ссылки')
    path = 'text_links/link_news/'
    work_with_first_teg(path)
    work_with_second_teg(path)
    work_with_class(path)
    work_with_second_class(path)
    work_fifth(path)

def add_to_text_link_to_atribute_for_header():
    print('Сейчас заполняем поля для заголовка')
    path = 'text_links/header/'
    work_with_first_teg(path)
    work_with_second_teg(path)
    work_with_class(path)
    work_with_second_class(path)

def add_to_text_link_to_atribute_for_news():
    print('Сейчас теги для новостей')
    path = 'text_links/news/'
    work_with_first_teg(path)
    work_with_second_teg(path)
    work_with_class(path)
    work_with_second_class(path)

#fucntion_to_change
def add_new_element(path, var):
    f = open(path, 'a')
    f.write(var+'\n')
    f.close()

#funcion for text_link

def work_with_first_teg(d):
    s = str(input(
        'Теперь вводи тег главного блока:'))
    add_new_element(path=d+'tag_1.txt', var=s)

def work_with_second_teg(d):
    s = str(input(
        'Теперь вводи тег откуда брать:'))
    add_new_element(path=d+'tag_2.txt', var=s)

def work_with_class(d):
    s = str(input(
        'Теперь вводи класс первого тега:'))
    add_new_element(path=d+'class_1.txt', var=s)

def work_with_second_class(d):
    s = str(input(
        'Теперь вводи класс второго тега:'))
    add_new_element(path=d+'class_2.txt', var=s)

def work_fifth(d):
    s = str(input(
        'Откуда взять ссылку(обычно href):'))
    add_new_element(path=d+'atribute.txt', var=s)

#main program
while True:
    add_new_website()