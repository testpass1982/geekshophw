import os
import json
if os.path.isfile('new_products.json'):
    print('it is here')
    with open('new_products.json', 'r', encoding='UTF-8') as p:
        new_prod_json = p.read()
        new_products = json.JSONDecoder().decode(new_prod_json)
        print(new_products)
else:
    print('nope')
for key in new_products['new_products']:
    print (key, new_products['new_products'][key])

print('json dumps')

json_data = json.dumps(new_products)
print(json_data)
