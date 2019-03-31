# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:38:56 2019

@author: nickbear
"""
"""
为了在文件里储存一个对象，首先以写，二进制模式打开一个 file 对象，然后调
用 pickle 模块的 dump 函数，这个过程称为 pickling 。
接下来，我们用 pickle 模块的返回对象的 load 函数重新取回对象。这个过程称之
为 unpickling 
"""

import pickle
# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple','mango','carrot']

#write to the file
f = open(shoplistfile,'wb')
pickle.dump(shoplist,f) #dump the object to a file
f.close()

del shoplist # detroy the shoplist variable

#Read back from the storage
f = open(shoplistfile,'rb')
storedlist = pickle.load(f) #load the object from the file
print(storedlist)


