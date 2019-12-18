#return 64 as charracter encoded output
#hexdigest() make the output readable(in charracters)
#json.dumps() make string output from json file(like dictionary)

import hashlib
import json

block = {
    'max':20,
    'manual':10
}
print(hashlib.sha256(json.dumps(block).encode()).hexdigest())
