from collections import OrderedDict

# init an example to demonstrate the difference between the two!
print("This is a Dict:")  
d = {}  
d['First'] = 1
d['Dos'] = 2
d['Dritte'] = 3
d['Quatre'] = 4
    
for key, value in d.items():  
    print(key, value)  
    
print("\nThis is an Ordered Dict:")  
od = OrderedDict()  
od['First'] = 1
od['Quatre'] = 4
od['Dos'] = 2
od['Dritte'] = 3

    
for key, value in od.items():  
    print(key, value)
