from pymongo import MongoClient

client = MongoClient()
db = client.testDB

new_item = db.examples.insert_one({
	'type': 'Example',
	'content': 'Hello World',
	'extra': 'Extra Stuff',
})
print(new_item.inserted_id)

examples = db.examples.find()
print('\n Examples so far: ')
for item in examples:
    print(type(item))
    print(item)

print(">>> Routine End")
