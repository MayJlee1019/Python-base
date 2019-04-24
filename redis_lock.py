#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time   : 2019/1/10 15:07
#@Author : yun

import time 
import redis 

#创建一个Redis锁，
class  RedisLock(object):
        def __init__(self, key):
                #创建一个redis连接，主机，端口，密码和数据库名
                self.rdcon = redis.Redis(host='10.16.22.100', port='6379', password='', db=1)
                #初始化的私有锁为0
                self._lock = 0
                self.lock_key = "%s_dynamic_test" % key
        
        @staticmethod
        #创建一个得到锁的方法，设置超时时间为10s
        def get_lock(cls, timeout=10):
                #当自己的锁不是1时 ，记录时间戳
                while cls._lock !=1 : 
                        timestamp = time.time() + timeout +1
                        cls._lock = cls.rdcon.setnx(cls.lock_key, timestamp)
                        #当锁是1时，或者当时的时间大于数据库的连接时间
                        if cls._lock == 1 or (time.time() > cls.rdcon.get(cls.lock_key) and time.time() > cls.rdcon.getset(cls.lock_key, timestamp)):
                                print ("get lock")
                                break
                        else:
                                time.sleep(0.3)
        @staticmethod
        #释放锁，当现在时间小于连接得到锁的时间
        def release(cls):
                if time.time() < cls.rdcon.get(cls.lock_key):
                        print ("release lock")
                        cls.rdcon.delete(cls.lock_key)

def deco(cls):
        def _deco(func):
                def __deco(*args, **kwargs):
                        print ("before %s called [%s]." %(func.__name__, cls))
                        cls.get_lock(cls)
                        try:
                                return func(*args, **kwargs)
                        finally:
                                cls.release(cls)
                return __deco
        return _deco

@deco(RedisLock("112233"))        
def myfunc():
        print ("myfunc() called.")
        time.sleep(20)

if __name__ == "__main__":  
        myfunc()


           
