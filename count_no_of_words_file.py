from collections import Counter
import pprint

with open('sample_file.txt','r') as data:
    #print(data.read().upper())
    count_data = Counter(data.read().upper())
    print(count_data)
    count_value = pprint.pformat(count_data)
print(count_data)
