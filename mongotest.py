import pymongo

client = pymongo.MongoClient("mongodb+srv://hemin59567:jecky123456@jecky59567.1fw3e.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "Name" : "Jecky",
    "email" : "hemin59567@gmail.com",
    "surname" : "Master"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

d = {
    "Name" : "Jecky",
    "email" : "hemin59567@gmail.com",
    "surname" : "Master"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

d = {
    "Name" : "Jecky",
    "email" : "hemin59567@gmail.com",
    "surname" : "Master"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )