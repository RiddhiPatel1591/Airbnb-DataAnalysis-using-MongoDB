import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
print(client.list_database_names())
mydb = client['Airbnb2']
print(mydb.list_collection_names())
MyCollection = mydb["sample2"]

print("\n")
print("Popular Airbnb locations to visit under high rated host:")
query=[
  {"$group" :
  {
          "_id" : "$neighbourhood",
          "Total_Nights_Spent_by_tourist": {"$sum": {"$sum": ["$minimum_nights"]}}
  }
},{"$sort": {"Total_Nights_Spent_by_tourist" : -1}},{"$limit":5}]

mydoc = MyCollection.aggregate(query)
neig=[]
for i in mydoc:
    print("->"+i.get('_id')+"    ->Total Nights Spent at "+i.get('_id')+" by Tourist: "+str(i.get('Total_Nights_Spent_by_tourist')))
    neig.append(i.get('_id'))
print("\n")
print("Popular Host at this locations:")

for i in range(len(neig)):
    find=[{
        "$match": {
            "$and":[
                    {"neighbourhood": neig[i]},
                    {"number_of_reviews": {"$gt": 20}},
                    {"price": {"$lt": 400}}
                   ]
        }
    },{"$limit":2}]
    doc = MyCollection.aggregate(find)
    print("Popular Host at "+neig[i]+": ")
    for k in doc:
        print("->Host Name:  "+k.get('host_name'))








