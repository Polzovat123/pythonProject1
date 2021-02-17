import time

def get_l_URL():
    l_url = []
    f = open('sys_file/acsses.txt', 'r')
    for line in f:
        l_url.append(line)
    l_url = [line.rstrip() for line in l_url]
    return l_url

def get_names_sourcese():
    names_sources = []
    f = open('sys_file/text_link.txt', 'r')
    for line in f:
        names_sources.append(line)
    names_sources = [line.rstrip() for line in names_sources]
    return names_sources

def get_time():
    return time.ctime(time.time())

def get_array_string(f):
    arr = []
    for i in f:
        arr.append(i)
    arr = [line.rstrip() for line in arr]
    return arr

def get_HEADERS():
    HEADERS={}
    conf = open('sys_file/config.txt', 'r')
    atrb = open('sys_file/atribute.txt', 'r')
    cnf = get_array_string(conf)
    atr = get_array_string(atrb)
    for i in range(len(cnf)):
        HEADERS[atr[i]]=cnf[i]
    return HEADERS

#text
def get_teg_header_1():
    a = []
    f = open('text_link/atribute_for_news/tag_header_1.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_tag_text_2():
    a = []
    f = open('text_link/atribute_for_news/tag_text_2.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_class_text_1():
    a = []
    f = open('text_link/atribute_for_news/class_text_1.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_class_text_2():
    a = []
    f = open('text_link/atribute_for_news/class_text_2.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

#link
def get_teg_link_1():
    a = []
    f = open('text_link/atrbute_for_link/tag_title.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_teg_link_2():
    a = []
    f = open('text_link/atrbute_for_link/tag_title_1.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_class_link_1():
    a = []
    f = open('text_link/atrbute_for_link/class_title.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_class_link_2():
    a = []
    f = open('text_link/atrbute_for_link/class_title_2.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

#header
def get_teg_head_1():
    a = []
    f = open('text_link/atribute_for_header/tag_title.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_teg_head_2():
    a = []
    f = open('text_link/atribute_for_header/tag_title_1.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_class_head_1():
    a = []
    f = open('text_link/atribute_for_header/class_title.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

def get_class_head_2():
    a = []
    f = open('text_link/atribute_for_header/class_title_2.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a

#other
def get_atribute_for_get():
    a = []
    f = open('text_link/atrbute_for_link/atribute_name.txt', 'r')
    for line in f:
        a.append(line)
    a = [line.rstrip() for line in a]
    return a
    pass

def show_i_n_l_t(a, b, c, d):
    show_link(a)
    show_link(b)
    show_link(c)
    show_link(d)
    pass

def show_link(a):
    for j in a:
        print(j)
    pass

def info(a, b, c, d):
    print('Длина массива')
    print('INDEX: '+str(len(a)))
    print('NAME NEWS: '+str(len(b)))
    print('LINK: '+str(len(c)))
    print('TEXT NEWS: '+str(len(d)))
    pass

def get_size():
    f = open('other_variable/sch.txt', 'r')
    for i in f:
        return int(i)
