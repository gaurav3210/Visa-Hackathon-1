def validation(mysql,mid,mname,regname,email,contact,address,password):
	flag = [0,0,0,0,0,0]
	cur = mysql.connection.cursor()
	r = [{},[],0]
	cur.execute("select * from Merchant where MerchantID = '"+mid+"';")
	result = cur.fetchone()
	r[0] = result
	if result['Name']!=mname:
		cur.execute("select * from Merchant where Name ='"+mname+"';")
		res = cur.fetchone()
		if res != None:
			flag[0] = 1
		else:
			r[0]['Name'] = mname
	if result['RegisteredName']!=regname:
		cur.execute("select * from Merchant where RegisteredName ='"+regname+"';")
		res = cur.fetchone()
		if res != None:
			flag[1]=1
		else:
			r[0]['RgisteredName'] = regname
	if result['EmailID']!=email:
		cur.execute("select * from Merchant where EmailID ='"+email+"';")
		res = cur.fetchone()
		if res != None:
			flag[2]=1
		else:
			r[0]['EmailID'] = email
	if result['ContactNumber']!=contact:
		cur.execute("select * from Merchant where ContactNumber ='"+contact+"';")
		res = cur.fetchone()
		if res != None:
			flag[3]=1
		else:
			r[0]['ContactNumber'] = contact
	if result['Address']!=address:
		cur.execute("select * from Merchant where Address ='"+address+"';")
		res = cur.fetchone()
		if res != None:
			flag[4]=1
		else:
			r[0]['Address'] = address
	if result['Password']!=password:
		cur.execute("select * from Merchant where Password ='"+password+"';")
		res = cur.fetchone()
		if res != None:
			flag[5]=1
		else:
			r[0]['Password'] = password
	for i in flag:
		if i:
			r[2] = 1
	r[1] = flag
	return r