# -*- coding: utf-8 -*-
import bmemcached
import time
import random

# Tested at python27

client = bmemcached.Client(('10.235.65.18:11211'), 'bmemcached', 'bmemcached')

i=0
while(i<10000):
    print(i)

    t = time.time()
    #print(type(t), t)
    s = lambda:int(round(t * 1000000))
    s = s()
    print(type(s), s)

    k = 'ck_t_mc_' + str(s)
    print(type(k), k)

    res_set = client.set(k, s, 86400)
    print(res_set)

    res_get = client.get(k)
    print(res_get)

    i+=1;
