import json

with open('source_file_2.json') as f:
    data = json.load(f)

print('------------------')

managers = {}
watchers = {}

for key in data:
    # print(key['managers'])
    for mngr in key['managers']:
        if mngr not in managers:
            managers[mngr] = [(key['name'], key['priority'])]
        else:
            managers[mngr].append((key['name'], key['priority']))
            
        
    for wtchr in key['watchers']:
        if wtchr not in watchers:
            watchers[wtchr] = [(key['name'], key['priority'])]
        else:
            watchers[wtchr].append((key['name'], key['priority']))
    
for name in managers:
    managers[name].sort(key=lambda row: row[1], reverse=False)

for name in watchers:
    watchers[name].sort(key=lambda row: row[1], reverse=False)    


# print(managers)
# print(watchers)


out_managers = {}
out_watchers = {}

for key in managers:
    out_managers[key]=[]
    for project in managers[key]:
        out_managers[key].append(project[0])
for key in watchers:
    out_watchers[key]=[]
    for project in watchers[key]:
        out_watchers[key].append(project[0])
        
print(out_managers)
print(out_watchers)

with open('managers.json', 'w') as json_file:
    json.dump(out_managers, json_file, indent = 4)
with open('watchers.json', 'w') as json_file:
    json.dump(out_watchers, json_file, indent = 4)