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
    c = news.find()
    for item in c:
        print(item)
    news.insert_one({
        "_id": 0,
        "news": "War never changes",
        "link": "https://www.bbc.com/russian/news-56196846",
        "text": "",
        "politic" : 0,
        "medicine" : 1
    })

def write_in_mongodb(socket, l_1, l_2, l_3, l_4, atr):
    db = socket.dataset
    news = db.news
    for i in range(len(l_1)):
        news.insert_one({
        "_id": l_1[i],
        "news_header": l_2[i],
        "link": l_3[i],
        "text": l_4[i],
        "atribute": {atr}
        })

def connect_and_push_to_dataset_data(l_1, l_2, l_3, l_4, l_5):
    socket = pymongo.MongoClient(get_string())
    try:
        print('Start first epoch')
        print("MongoDB version is %s" %
              socket.server_info()['version'])
        write_in_mongodb(l_1, l_2, l_3, l_4, l_5)
    except pymongo.errors.OperationFailure as error:
        print(error)
        quit(1)

def connect_and_write_from_NN():
    print(get_string())
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


#
#gw%KR$V8S%#?BZS3JBhX544*8m8S^AVXd5Cp3UY@N2EbPCK*eywWFNhE^yE2K2MvuBDSjyPGd_Fv@Vk=3QkyF+Uy2VXFgtRXBwGF$r8-&TH+mk
#