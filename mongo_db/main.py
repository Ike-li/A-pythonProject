import time

from pymongo import MongoClient


client = MongoClient(
    host="localhost",
    port=27017,
    username="admin",
    password="secret",
    authSource="admin",
)

db = client["test"]
collection = db["my_collection"]

# document = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York'
# }
# insert_result = collection.insert_one(document)
# print(insert_result)
#
#
# result = collection.find_one({'name': 'John'})
# print(result)
#
# # # 插入多个文档
# documents = [
#     {"name": "Alice", "age": 25, "city": "Chicago"},
#     {"name": "Bob", "age": 35, "city": "Los Angeles"}
# ]
# insert_result = collection.insert_many(documents)
# print(insert_result.inserted_ids)
#
# for doc in collection.find({"age": {"$gt": 29}}):
#     print(doc)
#
# for doc in collection.find({}, {"city": 1}):
#     print(doc)
#
# update_result = collection.update_one(
#     {"name": "John"},
#     {"$set": {"age": 31}}
# )
# print(update_result.modified_count)
#
# update_result = collection.update_many(
#     {"age": {"$gt": 30}},
#     {"$inc": {"age": 1}}
# )
# print(update_result.modified_count)
#
# delete_result = collection.delete_one({"name": "John"})
# print(delete_result.deleted_count)
# delete_result = collection.delete_many({"age": {"$gt": 24}})
# print(delete_result.deleted_count)


def wrapper(fun):
    def inner():
        start_time = time.time()
        result = fun()
        end_time = time.time()
        print(end_time - start_time)
        return result

    return inner


@wrapper
def a():
    for doc in collection.find():
        print(doc)


a()
