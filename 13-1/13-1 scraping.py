import  xml.etree.cElementTree as et
tree = et.ElementTree(file='C:\\Users\\tk1051984\\OneDrive - Bose Corporation\\Desktop\\menu.xml')
root = tree.getroot()

print(root.tag)
for child in root:
    print('tag:',child.tag,'attributes:',child.attrib)
    for grandchild in child:
        print('tag:',grandchild.tag,'attributes:',grandchild.attrib)

print(len(root))
print(len(root[0]))
print(root[0])
print(root[0].get("hours"))
print(root[0].keys())
print(root[0].items())

lunch = root.find("lunch")
print(lunch)
print(lunch.get("hours"))
print(lunch.keys())
print(lunch.items())

print(root[0].findall('item'))
for item in root[0].findall('item'):
    print(item.get('price'))
    print(item.text)

import json
j1 = {"name":"홍길동", "birth":"0525", "age": 30}
print(j1)
print(json.dumps(j1))
print(json.dumps(j1, indent = 2))
print(json.dumps([1,2,3]))
print(json.dumps([4,5,6]))

j1 = {"name":"홍길동", "birth":"0525", "age": 30}
d1 = json.dumps(j1)
print(json.loads(d1))

file_path = 'C:\\Users\\tk1051984\\OneDrive - Bose Corporation\\Desktop\\myinfo.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
print(type(data))
print(data)