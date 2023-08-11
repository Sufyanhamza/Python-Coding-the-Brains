import json

x = '{"Name": "Sufiyan", "Age" : 22, "Country" : "Pakistan"}'

y = json.loads(x)

print(y["Age"])