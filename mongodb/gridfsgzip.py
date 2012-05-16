#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Reimund Klain
import pymongo
import gridfs
import zlib
import os.path

def test():
    ''' 
    test compress gridfs data 
    TODO: Is there a more file like method?
    '''
    conn = pymongo.Connection()
    db = conn.test
    fs = gridfs.GridFS(db)
    
    with open(__file__, 'r') as fd:
        gf=fs.new_file(filename=os.path.basename(__file__))   
        try:
            gf.write(zlib.compress(fd.read(), 9))
        finally:
            gf.close()
    gf = fs.get_last_version(os.path.basename(__file__))
    print zlib.decompressobj().decompress(gf.read())
    

if __name__ == '__main__':
    test()



