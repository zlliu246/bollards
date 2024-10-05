import os
import json

ls = os.listdir("./src/assets/images128")
j = json.dumps(ls)

print(j.replace("\",", "\",\n"))