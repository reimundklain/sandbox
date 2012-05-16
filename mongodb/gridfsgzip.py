#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Reimund Klain
import pymongo
import gridfs
import zlib
import os.path

def test(level=9):
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
            gf.write(zlib.compress(fd.read(), level))
        finally:
            gf.close()
    gf = fs.get_last_version(os.path.basename(__file__))
    print('level:%d -> size=%d; md5=%s'%(level, gf.length, gf.md5)) 
    

if __name__ == '__main__':
    for i in range(1,10):
        test(i)

