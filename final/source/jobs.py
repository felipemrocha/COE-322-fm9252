import uuid
from hotqueue import HotQueue
import redis
import os

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()

job = redis.StrictRedis(host=redis_ip, port=6379, db=1, decode_responses=True)
q = HotQueue("queue", host=redis_ip, port=6379, db=2)
rd = redis.StrictRedis(host=redis_ip, port=6379, db=0, decode_responses=True)
im = redis.StrictRedis(host=redis_ip, port=6379,db=1)
def _generate_jid():
	return str(uuid.uuid4())

def generate_job_key(jid):
	return 'job.{}'.format(jid)

def _instantiate_job(jid, status, start, end):
	if type(jid) == str:
		return {'id': jid,
			'status': status,
			'start': start,
			'end': end
		}
	return {'id': jid.decode('utf-8'),
		'status': status.decode('utf-8'),
		'start': start.decode('utf-8'),
		'end': end.decode('utf-8')
		}

def _save_job(job_key, job_dict):
	job.hmset(job_key,job_dict)

def _queue_job(jid):
	q.put(jid)

def add_job(start, end, status="submitted"):
	jid = _generate_jid()
	job_dict = _instantiate_job(jid, status, start, end)
	_save_job(generate_job_key(jid),job_dict)
	_queue_job(jid)
	return job_dict

def update_job_status(jid, new_status):
	jid, status, start, end = job.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end')
	job_dict = _instantiate_job(jid, status, start, end)
	worker_ip = os.environ.get('WORKER_IP')
	if job_dict:
		job_dict['status'] = new_status
		if new_status == 'in progress':
            		job_dict['worker IP'] = worker_ip
		_save_job(generate_job_key(job_dict['id']), job_dict)
	else:
		raise Exception()
