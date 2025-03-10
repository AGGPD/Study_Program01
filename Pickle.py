import pickle
'''
data = {"filename": "f1.txt", "create_time": "today", "size": 111}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

import os
print(os.listdir())

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
print(data)

'''


data = {"filename": "f1.txt", "create_time": "today", "size": 111}
serialized_data = pickle.dumps(data)
print(serialized_data)