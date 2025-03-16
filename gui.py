import requests as req
from tkinter import*
import time
server=""
name=""
key=""
uid=0
login=Tk()
login.title("LANChat-登录")
login.resizable(False,False)
login.attributes('-topmost',True)
def onClosing():
	exit(0)
login.protocol("WM_DELETE_WINDOW",onClosing)
main_frame=Frame(login)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)
server_frame=Frame(main_frame)
server_frame.pack(fill="x", pady=5)
Label(server_frame, text="服务器：", width=8).pack(side="left")
server_entry=Entry(server_frame)
server_entry.pack(side="left", expand=True, fill="x")
username_frame=Frame(main_frame)
username_frame.pack(fill="x", pady=5)
Label(username_frame, text="用户名：", width=8).pack(side="left")
username_entry=Entry(username_frame)
username_entry.pack(side="left", expand=True, fill="x")
password_frame=Frame(main_frame)
password_frame.pack(fill="x", pady=5)
Label(password_frame, text="密码：",width=8).pack(side="left")
password_entry=Entry(password_frame, show="*")
password_entry.pack(side="left", expand=True, fill="x")
button_frame=Frame(main_frame)
button_frame.pack(fill="x")
login_text=StringVar()
login_text.set("服务器用\"ip:port\"格式输入")
Label(main_frame,textvariable=login_text).pack(side="left")
def onClickL():
	global server,name,key,uid
	server=server_entry.get()
	server="http://"+server+"/"
	name=username_entry.get()
	key=password_entry.get()
	try:
		r=req.get(server+"api/findUser/name="+name)
	except:
		login_text.set("网络错误")
		return
	if r.status_code!=200:
		login_text.set("网络错误")
		return
	elif r.text=="-1":
		login_text.set("未找到用户")
		return
	else:
		login_text.set(r.text)
		uid=int(r.text)
	r=req.get(server+"api/checkUser/uid="+str(uid)+"&key="+key)
	print(server+"api/checkUser/uid="+str(uid)+"&key="+key)
	if r.status_code!=200:
		login_text.set("网络错误")
	elif r.text=="Fail":
		login_text.set("密码错误")
	else:
		login_text.set("登录成功 uid="+str(uid))
		login.destroy()
def onClickR():
	register=Toplevel()
	register.title("LANChat-注册")
	register.resizable(False,False)
	register.attributes('-topmost',True)
	main_frame=Frame(register)
	main_frame.pack(expand=True, fill="both", padx=20, pady=20)
	server_frame=Frame(main_frame)
	server_frame.pack(fill="x", pady=5)
	Label(server_frame, text="服务器：", width=8).pack(side="left")
	server_entry=Entry(server_frame)
	server_entry.pack(side="left", expand=True, fill="x")
	username_frame=Frame(main_frame)
	username_frame.pack(fill="x", pady=5)
	Label(username_frame, text="用户名：", width=8).pack(side="left")
	username_entry=Entry(username_frame)
	username_entry.pack(side="left", expand=True, fill="x")
	password_frame=Frame(main_frame)
	password_frame.pack(fill="x", pady=5)
	Label(password_frame, text="密码：",width=8).pack(side="left")
	password_entry=Entry(password_frame, show="*")
	password_entry.pack(side="left", expand=True, fill="x")
	password2_frame=Frame(main_frame)
	password2_frame.pack(fill="x", pady=5)
	Label(password2_frame, text="确认密码：",width=8).pack(side="left")
	password2_entry=Entry(password2_frame, show="*")
	password2_entry.pack(side="left", expand=True, fill="x")
	button_frame=Frame(main_frame)
	button_frame.pack(fill="x")
	register_text=StringVar()
	register_text.set("服务器用\"ip:port\"格式输入")
	Label(main_frame,textvariable=register_text).pack(side="left")
	def onClickR2():
		server=server_entry.get()
		server="http://"+server+"/"
		name=username_entry.get()
		key=password_entry.get()
		key2=password2_entry.get()
		if(key!=key2):
			register_text.set("密码不匹配")
			return
		try:
			r=req.get(server+"api/findUser/name="+name)
		except:
			register_text.set("网络错误")
			return
		if r.status_code!=200:
			register_text.set("网络错误")
			return
		elif r.text!="-1":
			register_text.set("用户已存在")
			return
		r=req.get(server+"api/addUser/name="+name+"&key="+key)
		if r.status_code!=200:
			register_text.set("网络错误")
		elif r.text!="OK":
			register_text.set("未知错误")
		else:
			register_text.set("注册成功，请登录")
			register.destroy()
	Button(button_frame,text="注册",width=12,command=onClickR2).pack(pady=15,fill="x")
	register.mainloop()
Button(button_frame,text="登录",width=12,command=onClickL).pack(side="left",pady=15,fill="x")
Button(button_frame,text="注册",width=12,command=onClickR).pack(side="right",pady=15)
login.mainloop()
cur=0
root=Tk()
root.title("LANChat")
main_frame=Frame(root)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)
Label(main_frame,text="Hi "+name+", welcome to LANChat!",font=("",20)).pack(anchor="nw")
toolbar=Frame(main_frame)
Button(toolbar,text="登出",command=exit,width=10).pack(side="left",padx=5)
Button(toolbar,text="修改密码",width=10).pack(side="left",padx=5)
Button(toolbar,text="用户信息",width=10).pack(side="left",padx=5)
Button(toolbar,text="管理",width=10).pack(side="left",padx=5)
toolbar.pack(anchor="nw",pady=5,fill="x")
receiver=LabelFrame(main_frame,text="接收消息")
rt=Text(receiver)
rt.config(state='disabled')
rt.pack(expand=True, fill="both", padx=5, pady=5)
rs=StringVar()
Label(receiver,textvariable=rs).pack(anchor="sw",fill="x",expand=True,padx=5)
receiver.pack(side="top",fill="both",expand=True)
sender=LabelFrame(main_frame,text="发送消息")
msg_entry=Entry(sender)
msg_entry.pack(side="left",fill="x",expand=True,padx=5)
ss=StringVar()
def sendData():
	msg=msg_entry.get()
	r=req.get(server+"api/postMsg/uid="+str(uid)+"&key="+key+"&txt="+msg)
	if r.status_code!=200:
		ss.set("网络错误")
	elif r.text!="OK":
		ss.set("未知错误")
	else:
		msg_entry.delete(0,END)
		ss.set("发送成功")
Button(sender,text="发送",command=sendData,width=10).pack(side="left",padx=5,pady=5)
Label(sender,textvariable=ss).pack(side="right",fill="x",padx=5)
sender.pack(side="top",fill="x")
msgList=[]
def getData():
	global cur,rt,msgList
	if cur==0:
		r=req.get(server+"/api/getAllMsg")
		if r.status_code!=200:
			rs.set("网络错误")
		else:
			rs.set("连接正常")
			print("msgList="+r.text)
			global_vars={}
			exec("msgList="+r.text,global_vars)
			msgList=global_vars["msgList"]
		print(r.text)
		print(msgList)
		for i in msgList:
			rt.config(state='normal')
			rt.insert(END,str(str(i[1])+" | "+str(i[0])+"\n"))
			rt.insert(END,i[2]+"\n")
			rt.insert(END,"\n")
			rt.config(state='disabled')
		cur=len(msgList)
	else:
		num=0
		r=req.get(server+"/api/getNum")
		if r.status_code!=200:
			rs.set("网络错误")
		else:
			rs.set("连接正常")
			num=int(r.text)
		if num>cur:
			cur+=1
			r=req.get(server+"/api/getMsg/mid="+str(cur-1))
			if r.status_code!=200:
				rs.set("网络错误")
			else:
				rs.set("连接正常")
				global_vars={}
				exec("i="+r.text,global_vars)
				i=global_vars["i"]
				rt.config(state='normal')
				rt.insert(END,str(str(i[1])+" | "+str(i[0])+"\n"))
				rt.insert(END,i[2]+"\n")
				rt.insert(END,"\n")
				rt.config(state='disabled')
	root.after(300,getData)
root.after(300,getData)
root.mainloop()