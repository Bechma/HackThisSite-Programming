import requests
import re

sesion = requests.Session()
login = "https://www.hackthis.co.uk/?login"
payload = {"username": "USERNAME", "password": "PASSWORD"}
sesion.post(login, data=payload)


def solve(reto):
	url = "https://www.hackthis.co.uk/levels/coding/" + str(reto)
	texto = sesion.get(url).text
	ocurrencia = re.findall("<textarea>(.*)</textarea>", texto)[0].split(",")
	if reto == 1:
		ocurrencia = re.findall("<textarea>(.*)</textarea>", texto)[0].split(", ")
		ocurrencia.sort()
		payload = {"answer": ", ".join(ocurrencia)}
	elif reto == 2:
		ocurrencia = "".join([chr(158 - int(i)) if i.isdecimal() else i for i in ocurrencia])
		payload = {"answer": ocurrencia}
	else:
		return
	print(sesion.post(url, data=payload).text)


solve(2)
