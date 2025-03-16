from flask import Flask, render_template
import time
import csv

msgList=[]
userList=[]

def readMsgList():
	msgList=[]
	with open("static/msg.csv") as f:
		reader=csv.reader(f)
		for row in reader:
			msgList.append([row[0],row[1],row[2]])
	return msgList

def readUserList():
	UserList=[]
	with open("static/user.csv") as f:
		reader=csv.reader(f)
		for row in reader:
			userList.append([int(row[0]),row[1],row[2]])
	return userList

def writeMsgList(msgList):
	with open("static/msg.csv",'w',newline='',encoding='utf') as f:
		writer=csv.writer(f)
		for i in msgList:
			writer.writerow(i)

def writeUserList(userList):
	with open("static/user.csv",'w',newline='',encoding='utf') as f:
		writer=csv.writer(f)
		for i in userList:
			writer.writerow(i)


app = Flask(__name__)

@app.route('/api')
def index():
    return render_template('index.html')

@app.route('/api/postMsg/uid=<int:uid>&key=<key>&txt=<txt>')
def postMsg(uid,key,txt):
	print("[postMsg]",uid,key,txt)
	for i in userList:
		if i[0]==uid and i[2]==key:
			ti=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
			msgList.append([i[1],ti,txt])
			writeMsgList(msgList)
			return "OK"
	return "Fail"

@app.route('/api/getNum')
def getNum():
	return str(len(msgList))

@app.route('/api/getMsg/mid=<int:mid>')
def getMsg(mid):
	print("[getMsg]",mid)
	if(mid>=len(msgList)):
		return "Fail"
	return str(msgList[mid])

@app.route('/api/getAllMsg')
def getAllMsg():
	print("[getAllMsg]")
	return str(msgList)

@app.route('/api/addUser/name=<name>&key=<key>')
def addUser(name,key):
	uidMx=0
	for i in userList:
		uidMx=max(uidMx,i[0])
		if i[1]==name:
			return "Fail"
	userList.append([uidMx+1,name,key])
	writeUserList(userList)
	return "OK"

@app.route('/api/findUser/name=<name>')
def findUser(name):
	for i in userList:
		if i[1]==name:
			return str(i[0])
	return '-1'

@app.route('/api/checkUser/uid=<int:uid>&key=<key>')
def checkUser(uid,key):
	for i in userList:
		if i[0]==uid and i[2]==key:
			return "OK"
	return "Fail"

"""
#清理消息，仅调试
@app.route('/api/clearMsg')
def clearMsg():
	writeMsgList([])
	return 'OK'

#用户信息，仅调试
@app.route('/api/getUserData')
def getUserData():
	return str(userList)
"""

@app.route('/api/changeKey/uid=<int:uid>&ok=<ok>&nk=<nk>')
def changeKey(uid,ok,nk):
	for _ in range(len(userList)):
		i=userList[_]
		if i[0]==uid and i[2]==ok:
			userList[_][2]=nk
			return 'OK'
	return 'Fail'

#app.run(debug=True)

msgList=readMsgList()
userList=readUserList()
print(msgList)
print(userList)

app.run(debug=True)
