import json
with open("filmdata.json", "r") as json_file:
	filmjson = json.load(json_file)

for film in filmjson:
	if "MEDAL" in film['category']:
		print (film['year'])
		filmjson.remove(film)
		

with open("filmdata.json", "w") as outfile:
	json.dump(filmjson, outfile)

