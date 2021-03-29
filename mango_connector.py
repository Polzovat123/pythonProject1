# -*- coding: utf8 -*-
import pymongo

def get_autorizate_key():
    f = open('sys_file/connector-autorizate-data.txt')
    s = f.read()
    f.close()
    return s

def get_name_data():
    return 'TrainigData'

def get_string():
    s = get_autorizate_key()
    d = get_name_data()
    asd = 'mongodb+srv://neural-network:' + s + '@trainigdata.ylqgq.mongodb.net/'\
          + d + '?retryWrites=true&w=majority'
    return asd

def work(socket):
    db = socket.dataset
    news = db.news
    '''news.insert_one({
        "_id": 1,
        "title": '"Эвер Гивен" в Суэцком канале: владельцы надеются снять судно с мели, но на это могут уйти недели',
        "source": {
            "name": 'BBC',
            "icon": "Not found"
        },
        "link": "https://www.bbc.com/russian/news-56548050",
        "text": [0.12860646148, 1.930288097, -1.08119, 1.54445]
    })'''
    print('end')

def write_in_mongodb(socket, a_index,l_1, l_2, l_3, l_4, atr):
    db = socket.dataset
    news = db.news
    for i in range(len(l_1)):
        news.insert_one({
        "_id": a_index[i],
        "title": str(l_1[i]['title']),
        "link": str(l_2[i]['link']),
        "source": {
            "name": l_3[i],
            "icon":"Nan"
        },
        "image": str(l_4),
        "atribute": atr[i]
        })

def connect_and_push_to_dataset_data(title, id, link, source, image, dict_atr):
    socket = pymongo.MongoClient(get_string())
    try:
        print('Start first epoch')
        print("MongoDB version is %s" %
              socket.server_info()['version'])
        write_in_mongodb(socket, id, title, link, source, image, dict_atr)
    except pymongo.errors.OperationFailure as error:
        print(error)
        quit(1)

def connect_and_write_from_NN():
    socket = pymongo.MongoClient(get_string())
    try:
        print('Start first epoch')
        print("MongoDB version is %s" %
              socket.server_info()['version'])
        work(socket=socket)
    except pymongo.errors.OperationFailure as error:
        print(error)
        quit(1)
    pass

connect_and_write_from_NN()
#
#gw%KR$V8S%#?BZS3JBhX544*8m8S^AVXd5Cp3UY@N2EbPCK*eywWFNhE^yE2K2MvuBDSjyPGd_Fv@Vk=3QkyF+Uy2VXFgtRXBwGF$r8-&TH+mk
#