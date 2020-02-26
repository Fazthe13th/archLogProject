import bcrypt
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


valid_input = False
while not valid_input:
    # Take user input
    username = input('Enter username for registration: ')
    password = input('Enter passward for that user: ')
    # check password
    if len(password) < 6:
        print('Pasword needs to be more than or equal to 6 char')
        valid_input = False
    else:
        valid_input = True
convert_pass_to_string = str(password)
# string with encoding 'utf-8'
byte_str_password = str.encode(convert_pass_to_string)

hashed_password = bcrypt.hashpw(byte_str_password, bcrypt.gensalt(10))

try:
    client = MongoClient('mongodb://archLogUser:bracnet123@127.0.0.1:27017/bracnetWirelessLog')
    # client.admin.command('ismaster')
    archDB = client["bracnetWirelessLog"]
    collist = archDB.list_collection_names()
    if "users" in collist:
        archCollection = archDB["users"]
        user = {
            'username': username,
            'password': hashed_password
        }
        try:
            inserted_id = archCollection.insert_one(user).inserted_id
            print(inserted_id)
        except Exception as e:
            print(e)
    else:
        print("Collection not found in database")
        exit()
except ConnectionFailure as failed:
    print(failed)
    exit()





