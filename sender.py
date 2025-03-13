import requests as req
print("LANChat sender V1.0 by shicj")
print("Tip: Sever must be \"http://.../\"")
print("Have a good time!")
print()
server=""
while True:
	server=input("server: ")
	r=req.get(server+"/api")
	if r.status_code!=200:
		print("Fail: Server error!")
	else:
		break
name=""
uid=-1
key=""
while True:
	name=input("username: ")
	key=input("password: ")
	r=req.get(server+"api/findUser/name="+name)
#	print(server+"api/findUser/name="+name)
	if r.status_code!=200:
		print("Fail: Server error!")
		continue
	elif r.text=="-1":
		print("Fail: Could not find user!")
		continue
	else:
		print(r.text)
		uid=int(r.text)
	r=req.get(server+"api/checkUser/uid="+str(uid)+"&key="+key)
	print(server+"api/checkUser/uid="+str(uid)+"&key="+key)
	if r.status_code!=200:
		print("Fail: Server error!")
		continue
	elif r.text=="Fail":
		print("Fail: Key error!")
		continue
	else:
		print("Login OK with uid="+str(uid)+"!")
		break
while True:
	msg=input("Send message: ")
	r=req.get(server+"api/postMsg/uid="+str(uid)+"&key="+key+"&txt="+msg)
	if r.status_code!=200:
		print("Fail: Server error!")
	elif r.text!="OK":
		print("Fail: Unknow error!")
	else:
		print("OK!")
