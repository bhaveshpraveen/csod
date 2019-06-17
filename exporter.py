import json
import os
import pandas as pd

curr_dir = os.getcwd()
file_path = os.path.join(curr_dir, 'restaurants.json')

with open(file_path) as f:
    documents = f.readlines()

unique_attributes = set()
for doc in documents:
    dict_obj = json.loads(doc)
    doc_attributes = dict_obj.get('attributes', None)
    if doc_attributes:
        set_temp = set(attribute.lower() for attribute in doc_attributes)
        unique_attributes = unique_attributes.union(set_temp)

attribute_list = sorted(list(unique_attributes))

no_of_attributes = len(attribute_list)
no_of_documents = len(documents)

termfrequency = [[0 for j in range(no_of_attributes + 1)] for i in range(no_of_documents)]

attribute_memo = {}
for idx, attribute in enumerate(attribute_list):
    attribute_memo[attribute] = idx + 1

for idx, doc in enumerate(documents):
    dict_obj = json.loads(doc)
    restaurant_id = dict_obj['restaurantId']

    termfrequency[idx][0] = restaurant_id

    doc_attributes = dict_obj.get('attributes', None)

    if doc_attributes:
        for attr in doc_attributes:
            col_idx = attribute_memo[attr.lower()]
            termfrequency[idx][col_idx] = 1

output_file_path = os.path.join(curr_dir, 'data.csv')

print(termfrequency[0])

attributes_list = ['restaurant_id'] + attribute_list

df = pd.DataFrame(termfrequency, columns=attributes_list)
df.to_csv(output_file_path)







