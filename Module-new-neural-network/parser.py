from bs4 import BeautifulSoup
import requests

l_url = ['https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%90%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%BD%D1%8B%D0%B9_%D1%83%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C']
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
           'accept':'*/*'
           }
new_url = []
nn_url = []
last_url = []
text = []
k = 1

def get_html(url, params=None):
    l = requests.get(url, headers=HEADERS, params=params)
    return l

def parse_link_1(hml_file):
    link = BeautifulSoup(hml_file, 'html.parser')
    items = link.find_all("td")
    global new_url
    for i in items:
        #print(i)
        if i.find("a", class_="external text"):
            new_url.append(i.find("a", class_="external text").get("href"))

def parse_link_2(html_file):
    global nn_url

    link = BeautifulSoup(html_file, 'html.parser')
    gifts = link.find_all("ul")
    for i in gifts:
        if i.find("a", class_='mw-redirect'):
            nn_url.append('https://ru.wikipedia.org/' + i.find('a', class_='mw-redirect').get('href'))

def parse_link_3(html_file):
    global nn_url

    link = BeautifulSoup(html_file, 'html.parser')
    gifts = link.find_all("li")
    #print(gifts)

    for i in gifts:
        if i.find("a", class_='mw-redirect'):
            last_url.append('https://ru.wikipedia.org/'+ i.find('a', class_='mw-redirect').get('href'))

def parse_content(html_file):
    link = BeautifulSoup(html_file, 'html.parser')
    gifts = link.find_all("p")

    for i in gifts:
        if i.get_text():
            text.append(i.get_text())
        if i.find("a"):
            text.append(i.find("a").get_text())
    #print(text)
    wrire_data()
    #print(text)
    text.clear()
    #print(k)

def clear_word(word):
    n_word = ""
    for c in range(0, len(word)):
        #print(word[c])
        if (word[c]>='а' and word[c]<='я') or (word[c]>='А' and word[c]<='Я'):
            n_word = n_word + word[c]
        if word[c] == ' ':
            n_word = n_word + ' '
        #print(n_word)
    n_word = n_word + ' '
    return n_word.lower()

def wrire_data():
    f = open('data/main.txt', 'a')
    for word in range(len(text)):
        text[word] = clear_word(text[word])
        f.write(str(text[word])+'\n')


def start_farming_data():
    global k
    for url in l_url:
        l = get_html(url)
        if l.status_code==200:
            parse_link_1(l.text)
    print("step one")
    #Now we parse next sloi

    for url in new_url:
        link = get_html(url)
        if link.status_code == 200:
            parse_link_2(link.text)
    print("All complete")

    #Now we write se
    #print(nn_url)
    for url in nn_url:
        link = get_html(url)
        if link.status_code == 200:
            parse_link_3(link.text)
    #print(last_url)
    print('step 3')
    #now we parse text

    for url in last_url:
        link = get_html(url)
        if link.status_code == 200:
            parse_content(link.text)
        k+=1


start_farming_data()