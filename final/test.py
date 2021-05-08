import uuid
from hotqueue import HotQueue
import redis
import os

redis_ip = "10.110.194.121" 

job = redis.StrictRedis(host=redis_ip, port=6379, db=1, decode_responses=True)
q = HotQueue("queue", host=redis_ip, port=6379, db=2, decode_responses=True)
rd = redis.StrictRedis(host=redis_ip, port=6379, db=0, decode_responses=True)

print(len(q))

