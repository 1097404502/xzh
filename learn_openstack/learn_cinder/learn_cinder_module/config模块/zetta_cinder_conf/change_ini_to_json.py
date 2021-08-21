'''

'''
from configparser import RawConfigParser
import  pathlib
import json

ini_file = 'cinder.conf'
json_file = 'test.json'


cfg = RawConfigParser()
cfg.read(ini_file)

dest = {}

for sect in cfg.sections():
    # print(cfg.items(sect)) # [('a', '1000'), ('default-character-set', 'utf-8')]
    dest[sect] = dict(cfg.items(sect))

json.dump(dest, open(json_file, 'w'))