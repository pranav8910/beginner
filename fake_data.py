from faker import Faker
import json

fake_DB = []

demo = Faker()

for i in range(100000):
    data = {
        "name": demo.name(),
        "email": demo.email(),
        "country": demo.country(),
    }

    fake_DB.append(data)

json_dict = {
    "fake_DB": fake_DB
}

json_file = open("fake_database.json", "w")

json.dump(json_dict, json_file)
