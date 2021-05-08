from jobs import update_job_status, rd, q, job, generate_job_key
import matplotlib.pyplot as plt

@q.worker
def execute_job(jid):
	#update_job_status(jid, 'in progress')
	start, end = job.hmget(generate_job_key(jid),'start','end')
	start = int(start)
	end = int(end)
	years = list(range(start,end+1))
	numpoints = (end+1-start)
	total = [0] * numpoints
	count = [0] * numpoints
	wintotal = [0] * numpoints
	wincount = [0] * numpoints

	for key in rd.keys():
		year = int(rd.hget(key,'year'))
		if year >= start and year <= end:
			index = year - start
			lettertotal = len(str(rd.hget(key,'entity')))
			total[index] = total[index] +	lettertotal	
			count[index] = count[index] + 1
			if str(rd.hget(key,'winner')) == "True":
				wintotal[index] = wintotal[index] + lettertotal
				wincount[index] = wincount[index] + 1
	
	avgwin = [i / j for i, j in zip(wintotal, wincount)]
	avg = [i / j for i, j in zip(total, count)]
	title = "Average length of names in Oscar films between " + str(start) + " and " + str(end)
	
	plt.plot(years, avg, 'b-.',label="Nominees")
	plt.plot(years, wintotal, 'g-o', label= "Winners")
	plt.xlabel("Years")
	plt.title(title)

	plt.savefig('/oscarlength.png')
	
	with open('/oscarlength.png', 'rb') as f:
		img = f.read()

	job.hset(generate_job_key(jid),'image',img)

	update_job_status(jid, 'complete')


execute_job()
