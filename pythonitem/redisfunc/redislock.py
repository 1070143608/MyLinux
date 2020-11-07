#!/usr/bin/python3
# -*- coding=utf8 -*-


import time
import redis
import random
from redisfunc.rediscon import RedisPool


def redis_lock(func):
    def wrapper(*args, **kwargs):
        tag = random.randint(1, 1000)  # define a random num
        conn = RedisPool().conn
        if conn.set("conn.lock", str(tag), nx=True, ex=5):
            func(*args, **kwargs)
            if conn.get("conn.lock") == str(tag):
                conn.delete("conn.lock")
    return wrapper


