#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Asl forgiveness than permission
# (É mais facil pedir perdão do que permissão)

try:
    names = open('names.txt').readlines()
    1 / 0
except:
    print('[Error] File names.txt not Found.')
    sys.exit(1)
    # TODO: USAR RETRY

else:
    print('Sucesso')
finally:
    print('Sempre execute isso!')


try:
    print(names[2])
except:
    print('[Error] Missing name in the list')
    sys.exit(1)




