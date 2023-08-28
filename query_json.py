import json
import pandas as pd

json_file = open("fake_database.json", "r")
json_dict = json.load(json_file)
fake_data = json_dict["fake_DB"]

query_answer = []

query_TLD = input("Enter the TLD of the email: ")
query_country = input("Enter a country: ")


for data in fake_data:
    email = data["email"].lower()
    if query_TLD:
        if query_TLD.lower() != email[-3:]:
            continue

    if query_country:
        if query_country.lower() != data["country"].lower():
            continue


#     print(data)
#     print(query_country.lower() != data["country"].lower())
#     quit()
    query_answer.append(data)

# print(len(query_answer))
# print(query_answer[0:3])

df = pd.DataFrame(query_answer)
df.to_excel('Query_results.xlsx', index=False)
