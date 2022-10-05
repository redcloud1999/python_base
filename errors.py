#!/usr/bin/env python3

import os
import sys
import time
import logging

log = logging.Logger('errors')

# EAFP - Easy to Asl forgiveness than permission
# (É mais facil pedir perdão do que permissão)

def try_to_open_a_file(filepath, retry=1) -> list:
    """ Tries to open file, if error, retries n times"""
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines()
        except FileNotFoundError as e:
            log.error('ERRO: %s', e)
            time.sleep(2)
        else:
            print('Sucesso')
        finally:
            print('Sempre execute isso!')
    return []

for line in try_to_open_a_file('names.txt', retry=5):
    print(line)





