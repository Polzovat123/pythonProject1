from ai import use_mango_connector

old_title = []
old_link = []
old_url_source = []
counter = 1


def check_in_old(element):
    for i in range(len(old_title)):
        if old_title[i]==element:
            return False
    return True

def add_dictionary(number_start, new_title, new_link, url_sourse):
    global counter
    s = number_start
    push_title = []
    push_link = []
    push_source = []
    for i in range(len(new_link)):
        if check_in_old(new_title[i]):
            push_title.append(new_title[i])
            push_link.append(new_link[i])
            push_source.append(url_sourse)
            old_title.append(new_title[i])
            old_link.append(new_link[i])
            old_url_source.append(url_sourse)
            number_start+=1

    print('1111')
    print(generate_id(s, number_start))
    use_mango_connector(push_title, push_link, push_source, id=generate_id(s, number_start))
    if counter%9==0:
        del old_link[:len(old_link)/2]
        del old_title[:len(old_title)/2]
        del old_url_source[:len(old_url_source) / 2]
    counter+=1
    return number_start+2

def generate_id(first, last):
    id = []
    for i in range(first, last):
        id.append(i)
    return id