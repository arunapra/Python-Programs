from collections import Counter
dict1 = {'key1':100,'key2':200,'key4':400}
dict2 = {'key1':10,'key2':20,'key3':300}
new_dict = dict(Counter(dict2) + Counter(dict1))
print(new_dict)
