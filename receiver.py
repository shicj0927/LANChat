import requests as req
import time
print("LANChat receiver V1.0 by shicj")
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
msgList=[]
while True:
	r=req.get(server+"/api/getAllMsg")
	if r.status_code!=200:
		print("Fail: Server error!")
		continue
	else:
		exec("msgList="+r.text)
		break
	time.sleep(0.5)
for i in msgList:
	print(i[1],"|",i[0])
	print(i[2])
	print()
cur=len(msgList)
while True:
	num=0
	r=req.get(server+"/api/getNum")
	if r.status_code!=200:
		print("Fail: Server error!")
		continue
	else:
		num=int(r.text)
	if num>cur:
		cur+=1
		r=req.get(server+"/api/getMsg/mid="+str(cur-1))
		if r.status_code!=200:
			print("Fail: Server error!")
			continue
		else:
			exec("tmp="+r.text)
			print(tmp[1],"|",tmp[0])
			print(tmp[2])
			print()
	time.sleep(0.5)
