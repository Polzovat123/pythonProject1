import requests
from file_manager import *
from bs4 import BeautifulSoup
from read_config import *


have_file=0
sch=1
#print(sch)
#print(type(sch))
l_URL = get_l_URL()
names_sources = get_names_sourcese()
time_starrt = get_time()
HEADERS = get_HEADERS()
time_sleep = int(3600)
INDEX = []
NAME_NEWS = []
LINK = []
TEXT_NEWS = []
#for title
tag_title_1 = get_teg_head_1()
tag_title_2 = get_teg_head_2()
class_title_1 = get_class_head_1()
class_title_2 = get_class_head_2()
#for link
tag_link_1 = get_teg_link_1()
tag_link_2 = get_teg_link_2()
class_link_1 = get_class_link_1()
class_link_2 = get_class_link_2()
atribute_for_get = get_atribute_for_get()
#for text
tag_text_1 = get_teg_header_1()
tag_text_2 = get_tag_text_2()
class_text_1 = get_class_text_1()
class_text_2 = get_class_text_2()

#MAIN_DATA_TABLE = [
#    NAME_NEWS,
#    LINK,
#    TEXT_NEWS
#]

def get_html(url, params=None):
    l = requests.get(url, headers=HEADERS, params=params)
    return l

def check_link(url):
    #print(url.find('http'))
    if url.find('http')!=-1:
        return True
    else:
        return False

def get_link_news(html, num=0,  tag_1='', class_1='', tag_2 ='', class_2='', get_atribute=''):
    c = BeautifulSoup(html, 'html.parser')
    items = c.find_all(tag_1, class_=class_1)

    news_link = []
    for item in items:
        if check_link(item.find(tag_2, class_=class_2).get(get_atribute)):
            add = ''
        else:
            add = names_sources[num]
        news_link.append({
            'link' :  add+ item.find(tag_2, class_=class_2).get(get_atribute)
        })
    return news_link

def get_header_news(html, num=0,  tag_1='', class_1='', tag_2 ='', class_2=''):
    c = BeautifulSoup(html, 'html.parser')
    items = c.find_all(tag_1, class_=class_1)

    news_header = []
    for item in items:
        news_header.append({
            'title': item.find(tag_2, class_=class_2).get_text()
        })
    return news_header
    #for i in range(43):
    #    print(news_header[i])
    #print(len(news_header))

def show_list_dict(object):
    for i in range(len(object)):
        print(object[i])

def show_list_dict_all(object, object_2, object_3):
    for i in range(len(object)):
        print(object[i]['title']+"________From: "+object_2[i]['link'])
        print(object_3[i])
        print('\n')

def add_big_dictionary(object_1, object_2, object_3):
    for i in range(len(object_1)):
        global sch
        INDEX.append(sch)
        sch+=1
        NAME_NEWS.append(object_1[i]['title'])
        LINK.append(object_2[i]['link'])
        TEXT_NEWS.append(object_3[i])

def get_news(html, tag_1='', class_1='', tag_2 ='', class_2=''):
    c = BeautifulSoup(html, 'html.parser')
    items = c.find_all(tag_1, class_=class_1)

    text = " "
    for item in items:
        have_a_text = item.find(tag_2, class_=class_2)
        if have_a_text:
            text = text + item.find(tag_2, class_=class_2).get_text()
        else:
            text = text
    return text

def check_a_source_for_text(url, num):
    if url.find(names_sources[num])!=-1:
        return True
    else:
        return False

def get_text_newq(link, num):
    if check_a_source_for_text(link, num):
        url = get_html(link)
    else:
        return ""
    if url.status_code==200:
        news = get_news(url.text, tag_1=tag_text_1[num], class_1=class_text_1[num], tag_2=tag_text_2[num], class_2=class_text_2[num])
        return news
    else:
        print("We can`t open link:"+url)
        return ""

def get_text_news(url_l, num=0):
    text_news = []
    for i in range(len(url_l)):
        text_news.append(get_text_newq(url_l[i].get('link'), num))
    return text_news

def parse(url, num=0):
    html = get_html(url)
    if html.status_code ==200:
        news_head = get_header_news(html.text, num, tag_title_1[num], class_title_1[num], tag_title_2[num], class_title_2[num])
        show_list_dict(news_head)
        news_link = get_link_news(html.text, num, tag_link_1[num], class_link_1[num], tag_link_2[num], class_link_2[num], atribute_for_get[num])
        #show_list_dict(news_link)
        news_text = get_text_news(news_link, num)
        #show_list_dict_all(news_head, news_link, news_text)
        add_big_dictionary(news_head, news_link, news_text)
    else:
        print('Error, we can`t open web site')

def parse_all_web_site():
    for i in range(len(l_URL)):
        parse(l_URL[i], i)
    print('all data reads and end sucsesful')

def main_function():
    while True:
        global time_starrt
        print('Time: ' + time_starrt)
        parse_all_web_site()
        print('Start pause')
        #info(INDEX, NAME_NEWS, LINK, TEXT_NEWS)
        #show_i_n_l_t(INDEX, NAME_NEWS, LINK, TEXT_NEWS)
        #write_data(INDEX, NAME_NEWS, LINK, TEXT_NEWS)
        write_first_data(INDEX, NAME_NEWS, LINK, TEXT_NEWS)
        #write_all_config_end_itteration(time_starrt, sch)
        time.sleep(time_sleep)
        time_starrt = get_time()
    pass

main_function()