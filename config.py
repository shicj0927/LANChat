import requests as req
print("LANChat config V1.0 by shicj")
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
while True:
    print("Input '1' to add user")
    print("Input '2' to change password")
    print()
    x=int(input(">"))
    if x==1:
        name=input("username: ")
        key=input("password: ")
        r=req.get(server+"api/findUser/name="+name)
#	    print(server+"api/findUser/name="+name)
        if r.status_code!=200:
            print("Fail: Server error!")
            continue
        elif r.text!="-1":
            print("Fail: This user is already here!")
            continue
        r=req.get(server+"api/addUser/name="+name+"&key="+key)
        if r.status_code!=200:
            print("Fail: Server error!")
            continue
        elif r.text!="OK":
            print("Fail: Unknow error!")
            continue
        else:
            print("Add user success!")
    elif x==2:
        name=input("username: ")
        ok=input("old password: ")
        nk=input("new password: ")
        uid=""
        r=req.get(server+"api/findUser/name="+name)
#	    print(server+"api/findUser/name="+name)
        if r.status_code!=200:
            print("Fail: Server error!")
            continue
        elif r.text==-1:
            print("Fail: Could not find user!")
            continue
        else:
            uid=r.text
        r=req.get(server+"/api/changeKey/uid="+uid+"&ok="+ok+"&nk="+nk)
        if r.status_code!=200:
            print("Fail: Server error!")
            continue
        elif r.text=="Fail":
            print("Fail: old password wrong!")
            continue
        else:
            print("Change password success!")
    else:
        print("Fail: Input error!")
