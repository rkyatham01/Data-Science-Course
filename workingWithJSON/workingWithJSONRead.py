
f = open("book.txt", "r") #opening in read mode
s = f.read() #reads whole file into s
import json
book = json.loads(s) #converts string in JSON format back to dictionary
bobsInfo = book['bob']
bobsAddress = bobsInfo['address'] #can extract information using keys
bobsPhone = bobsInfo['phone']

for person in book:
    print(book[person]) #prints all the records one by one