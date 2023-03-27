book = {}
book['tom'] = {
    'name':'tom',
    'address':'1 red street, NY',
    'phone': 98989898
}

book['bob'] = {
    'name':'bob',
    'address':'1 green street, NY',
    'phone': 23424234
}

import json
#takes dictionary as input and dumping it as a string (in JSON format)
s = json.dumps(book) 
with open("book.txt", 'w') as f:
    f.write(s) #writes JSON string to a file
#JSON is a data exchange format (exchanging from python program -> javascript program)