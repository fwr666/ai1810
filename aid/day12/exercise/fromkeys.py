v = dict.fromkeys(['k1','k2'],[])
print(v)#{'k2': [], 'k1': []}
print('k1',id(v['k1']))
print('k2',id(v['k2']))
v['k1'].append(666)
print(v)
v['k1']=(777)#{'k1': 777, 'k2': [666]}
print(v)
print('k1',id(v['k1']))
print('k2',id(v['k2']))