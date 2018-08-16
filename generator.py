#!/usr/bin/env python
import uniqueid as uid

PRIVATE_KEY_LOC = 'data/privatekey.p8'


while True:
    print('Enter anything to generate a new key or Q to quit')
    entry = input()
    if entry.lower() == 'q':
        break
    print(uid.generateID(PRIVATE_KEY_LOC))
