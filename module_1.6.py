my_dict={'Артур': 1992,'Ильяна': 1991,'Амир': 2018,'Асель': 2020}
print(my_dict)
my_dict['Артур']
print('Existing value:',(my_dict['Артур']))
print('Not existing value:',my_dict.get('Руслан'))
my_dict.update({'Михаил':1976,'Александр':2002})
print(my_dict)
a = my_dict.pop('Александр')
print(my_dict)
print('Deleted value :',a)
print('Modified dictionary :',(my_dict))
my_set={1,1,1,3,4,5,5,3,2}
print('Set :',my_set)
my_set.update({6,7})
print('New set :',my_set)
my_set.discard(1)
print('Update set :',my_set)