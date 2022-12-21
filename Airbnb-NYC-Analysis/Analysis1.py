import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
print(myclient.list_database_names())
mydb = myclient['Airbnb2']
print(mydb.list_collection_names())
MyCollection = mydb["sample2"]

print("Different Types of Room are: ")
new = [{"$group":
            {"_id": "$room_type"}}]
mydoc = MyCollection.aggregate(new)
for i in mydoc:
    print("->"+i.get('_id'))
print("---------------------------------------------------------------------------------------------------------------------------------")

private = [{'$match':{
       '$and':[{"room_type": "Private room"},{"availability_365": {"$gt": 300}},{"price":{"$lt": 100}}]}
       }, {"$sort": {"number_of_reviews": -1}}, {"$limit": 3}]
my_variable = MyCollection.aggregate(private)
print("TOP 3 Private room with minimum price, 300+ days availability and maximum number of review is available at:")
for i in my_variable:
    x=i.get('availability_365')
    y=x/365
    percentage=round(y*100,2)
    print("->Host_Name:"+i.get('host_name')+" ->Location: " +i.get('neighbourhood')+" ->Near_By_Location: "+i.get('neighbourhood_group')+" ->Price: "+str(i.get('price'))+" ->Availability: "+str(percentage)+"%"+" ->Review: "+str(i.get('number_of_reviews')))
print("---------------------------------------------------------------------------------------------------------------------------------")

entire = [{'$match':{
       '$and':[{"room_type": "Entire home/apt"},{ "availability_365":{"$gt": 300}},{"price":{"$lt": 100}}]}
       }, {"$sort": {"number_of_reviews": -1}}, {"$limit": 3}]
my_variable = MyCollection.aggregate(entire)
print("TOP 3 Entire home/apt with minimum price, 300+ days availability and maximum number of review is available at:")
for i in my_variable:
    x = i.get('availability_365')
    y = x / 365
    percentage = round(y * 100, 2)
    print("->Host_Name:" + i.get('host_name') + " ->Location: " + i.get('neighbourhood') + " ->Near_By_Location: " + i.get('neighbourhood_group') + " ->Price: " + str(i.get('price')) + " ->Availability: "+str(percentage)+"%"+" ->Review: " + str(i.get('number_of_reviews')))
print("---------------------------------------------------------------------------------------------------------------------------------")

shared = [{'$match':{
       '$and':[{"room_type": "Shared room"},{ "availability_365":{"$gt": 300}},{"price":{"$lt": 100}}]}
       }, {"$sort": {"number_of_reviews": -1}}, {"$limit": 3}]
my_variable = MyCollection.aggregate(shared)
print("TOP 3 Shared room with minimum price, 300+ days availability and maximum number of review is available at:")
for i in my_variable:
    x = i.get('availability_365')
    y = x / 365
    percentage = round(y * 100, 2)
    print("->Host_Name:" + i.get('host_name') + " ->Location: " + i.get('neighbourhood') + " ->Near_By_Location: " + i.get('neighbourhood_group') + " ->Price: " + str(i.get('price')) + " ->Availability: "+str(percentage)+"%"+" ->Review: " + str(i.get('number_of_reviews')))


