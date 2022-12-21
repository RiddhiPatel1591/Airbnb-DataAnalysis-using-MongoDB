import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
print(client.list_database_names())
mydb = client['Airbnb2']
print(mydb.list_collection_names())
MyCollection = mydb["sample2"]

name = [{ "$group" :{"_id" : "$host_name"}}]
MyDoc = MyCollection.aggregate(name)
host = []
for j in MyDoc:
    host.append(j.get('_id'))

location = [{ "$group" :{"_id" : "$neighbourhood"}}]
MyDoc = MyCollection.aggregate(location)
loc = []
for j in MyDoc:
    loc.append(j.get('_id'))

for i in range(len(host)):
    sum = MyCollection.count_documents({"host_name": host[i]})
    if sum > 300:
        print("Host Name : " + (host[i]))
        for j in range(len(loc)):
            my_variable = MyCollection.count_documents({'$and': [{"host_name": host[i]}, {"neighbourhood": loc[j]}]})
            if my_variable > 0:
                print("->Location: "+(loc[j])+"  ->Number of houses: "+str(my_variable))
        print("Total Number of houses: "+str(sum))
        print("\n")








