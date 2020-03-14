Dict = { } 
print("Initial nested dictionary:-") 
print(Dict) 

Dict['Dict1'] = {} 

# Adding elements one at a time 
Dict['Dict1']['name'] = 'Bob'
Dict['Dict1']['age'] = 21
print("\nAfter adding dictionary Dict1") 
print(Dict) 

# Adding whole dictionary 
Dict['Dict2'] = {'name': 'Cara', 'age': 25} 
print("\nAfter adding dictionary Dict1") 
print(Dict) 
