import pymongo
from pymongo import MongoClient
import time
import psutil
import logging

logger = logging.getLogger(__name__)
# for doc in mydoc:
#     print(doc)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["pets"]
pet_collection = mydb["petrecords"]
clinic_collection = mydb["clinics"]
owners_collection = mydb["owners"]

query_counter = 1

def time_query(collection, query, query_type = None):
    start_time = time.perf_counter_ns()

    mydoc = query()

    query_time = time.perf_counter_ns() - start_time

    global query_counter
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    # print("Query #:      ", query_counter)

    # if query_type == "sum":
    #     for doc in mydoc:
    #         print("Sum of Results:", doc["total_fees_paid"])
    # elif query_type == "avg":
    #     for doc in mydoc:
    #         print("Avg of Results:", doc["mean_age"])
    # elif query_type == "ins" or "update":
    #     print("Successful Change!")
    # else:
    #     num_results = sum(1 for _ in mydoc)
    #     print("# of Results:  ", num_results)

    # print("Query Time:    ", query_time)
    seconds = query_time / 1e9
    formatted_seconds = "{:.20f}".format(seconds)
    print(formatted_seconds, "\n")

    # print(f"CPU usage:      {cpu_percent}%")
    # print(f"Memory usage:   {memory_percent}%", "\n")
    # query_counter += 1

time_query(clinic_collection, lambda: clinic_collection.find().limit(1))

time_query(clinic_collection, lambda: clinic_collection.find())

time_query(owners_collection, lambda: owners_collection.find().limit(1))

time_query(owners_collection, lambda: owners_collection.find())

time_query(pet_collection, lambda: pet_collection.find().limit(1))

time_query(pet_collection, lambda: pet_collection.find().limit(500))

time_query(pet_collection, lambda: pet_collection.find())

time_query(pet_collection, lambda: pet_collection.find({ "petID": 777 }))

# Time to retrieve the address of the clinic associated with the pet record with PetID=777, by joining on ClinicID (1 result)
start_time = time.perf_counter_ns()
result = pet_collection.aggregate([
    {
        "$match": { "PetID": 777 }  # Match documents with the desired PetID
    },
    {
        "$lookup": {
            "from": "clinics",  # Name of the collection to join
            "localField": "ClinicID",  # Field in the petrecords collection
            "foreignField": "ClinicID",  # Field in the clinics collection
            "as": "clinic_info"  # Name for the joined data
        }
    },
    {
        "$unwind": "$clinic_info"  # Unwind the array created by $lookup
    },
    {
        "$project": {
            "_id": 0,  # Exclude the _id field from the output
            "ClinicAddress": "$clinic_info.Address"  # Include the address from the clinics collection
        }
    }
])
query_time = time.perf_counter_ns() - start_time
seconds = query_time / 1e9
formatted_seconds = "{:.20f}".format(seconds)
print(formatted_seconds, "\n")
cpu_percent = psutil.cpu_percent()
memory_percent = psutil.virtual_memory().percent
# print("Query #:      ", query_counter)
# print("Query Time:    ", query_time)


# print(f"CPU usage:      {cpu_percent}%")
# print(f"Memory usage:   {memory_percent}%", "\n")
query_counter += 1

# for doc in result:
#     print(doc)

# Time to retrieve the surname of the owner associated with the pet record with PetID=777, by joining on OwnerID (1 result)
start_time = time.perf_counter_ns()
result = pet_collection.aggregate([
    {
        "$match": { "PetID": 777 }  # Match documents with the desired PetID
    },
    {
        "$lookup": {
            "from": "owners",  # Name of the collection to join
            "localField": "OwnerID",  # Field in the petrecords collection
            "foreignField": "OwnerID",  # Field in the owners collection
            "as": "owner_info"  # Name for the joined data
        }
    },
    {
        "$unwind": "$owner_info"  # Unwind the array created by $lookup
    },
    {
        "$project": {
            "_id": 0,  # Exclude the _id field from the output
            "OwnerSurname": "$owner_info.Surname"  # Include the surname from the owners collection
        }
    }
])
query_time = time.perf_counter_ns() - start_time
seconds = query_time / 1e9
formatted_seconds = "{:.20f}".format(seconds)
print(formatted_seconds, "\n")
cpu_percent = psutil.cpu_percent()
memory_percent = psutil.virtual_memory().percent
# print("Query #:      ", query_counter)
# print("Query Time:    ", query_time)

# print(f"CPU usage:      {cpu_percent}%")
# print(f"Memory usage:   {memory_percent}%", "\n")
query_counter += 1

# for doc in result:
#     print(doc)

time_query(pet_collection, lambda: pet_collection.find( {"SpayedOrNeutered": "No"} ))

time_query(pet_collection, lambda: pet_collection.find( {"Animal": "Cat"} ))

time_query(owners_collection, lambda: owners_collection.aggregate([
    {
        "$group": {
            "_id": None,
            "total_fees_paid": { "$sum": "$TotalFeesPaid" }        
            }
    }
]), "sum")

time_query(pet_collection, lambda: pet_collection.aggregate([
    {
        "$group": {
            "_id": None,
            "mean_age": { "$avg": "$Age" }        
            }
    }
]), "avg")

time_query(clinic_collection, lambda: clinic_collection.insert_one({
    "ClinicID": 6
}), "ins")
clinic_collection.delete_one({"ClinicID": 6})

time_query(owners_collection, lambda: owners_collection.insert_one({
    "OwnerID": 201
}), "ins")
owners_collection.delete_one({"OwnerID": 201})

time_query(pet_collection, lambda: pet_collection.insert_one({
    "PetID": 1001
}), "ins")
pet_collection.delete_one({"PetID": 1001})

time_query(clinic_collection, lambda: clinic_collection.update_one({"ClinicID": 5}, { "$set": {"NumberOfVets": 9}}), "update")
clinic_collection.update_one({"ClinicID": 5}, { "$set": {"NumberOfVets": 5}})

time_query(owners_collection, lambda: owners_collection.update_one({"OwnerID": 5}, { "$set": {"Surname": "SMITH"}}), "update")
owners_collection.update_one({"OwnerID": 5}, { "$set": {"Surname": "BRADLEY"}})

time_query(pet_collection, lambda: pet_collection.update_one({"PetID": 5}, { "$set": {"Name": "Finnegan"}}), "update")
owners_collection.update_one({"PetID": 5}, { "$set": {"Name": "Gretel"}})