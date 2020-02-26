from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.errors import WriteError
import pprint
class load_data:
    def connect_db(self):
        try:
            client = MongoClient('mongodb://archLogUser:bracnet123@127.0.0.1:27017/bracnetWirelessLog')
            # client.admin.command('ismaster')
            archDB = client["bracnetWirelessLog"]
            return archDB
        except ConnectionFailure as failed:
            print(failed)
            return False
    
    def load_to_database(self, log):
        archDB = self.connect_db()
        if archDB == False:
            return 0
        else:
            collist = archDB.list_collection_names()
            if "archLog" in collist:
                archCollection = archDB["archLog"]
            try:
                log_id = archCollection.insert_one(log).inserted_id
                print(log_id)
            except WriteError as e:
                print(e)
        
            