import pymongo

name = ["politic", "economic", "society", "spiritual"]

def worki(socket, i ,s):
    db = socket.cat
    main= db.main
    main.insert_one({
        "_id": 5,
        "name":'Technology'
    })

def work(socket):
    for i in range(len(name)):
        worki(socket, i, name[i])

socket = pymongo.MongoClient('mongodb+srv://neural-network:DGVDyYa97m5yHUj@trainigdata.ylqgq.mongodb.net/TrainigData?retryWrites=true&w=majority')
try:
    print('Start first epoch')
    print("MongoDB version is %s" %
          socket.server_info()['version'])
    work(socket=socket)
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)
pass