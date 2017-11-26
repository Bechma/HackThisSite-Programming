import requests
import re

url_login = "https://www.hackthissite.org/user/login"
url_objective = "https://www.hackthissite.org/missions/prog/11/"

# Fill here, don't need to modify anything else
payload = {
	"password": "yourpass",
	"username": "youruser"
}

# Need this extra header to work
headers = {"Referer": "https://www.hackthissite.org/"}


# Open session and login
session = requests.Session()
session.post(url=url_login, data=payload, headers=headers)
result = session.get(url_objective)

# Take both string and shift from the html
characters = re.findall("<br />Generated String: (.+)<br />", result.text)[0]
shift = int(re.findall("<br />Shift: (.+)<br />", result.text)[0])

# Algorithm math
result = ""
aux = ""
for i in characters:
	if i.isdigit():
		aux += i
	else:
		result += chr(int(aux)-shift)
		aux = ""

# Send solution
payload = {"solution": result}
session.post(url=url_objective, data=payload, headers=headers)
