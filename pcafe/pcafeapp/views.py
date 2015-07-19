from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from models import *
from django.db.models import Q
from django.shortcuts import render_to_response, HttpResponseRedirect
from datetime import *
# from forms import *
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from .models import *
from django.template import RequestContext
from django.db import connection
from datetime import datetime, timedelta, date
from django.conf import settings as conf_settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.mail import send_mail, EmailMultiAlternatives
import time
import random
import string

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def user_login_required(f):
		def wrap(request, *args, **kwargs):
		#this check the session if userid key exist, if not it will redirect to login page
			if 'userid' not in request.session.keys():
				content={}
				content['message']="You are already Logout"
				return HttpResponseRedirect("/",content)
			return f(request, *args, **kwargs)
		wrap.__doc__=f.__doc__
		wrap.__name__=f.__name__
		return wrap

#Home Page
def HomePage(request):
	content={}
	content.update(csrf(request))
	fruitgrainlist = Items_Menu.objects.filter(cat_id=1, sub_cat_id=1)
	sandwitchlist = Items_Menu.objects.filter(cat_id=1, sub_cat_id=2)
	mealslist = Items_Menu.objects.filter(cat_id=1, sub_cat_id=3)
	eggslist = Items_Menu.objects.filter(cat_id=1, sub_cat_id=4)
	sweetslist = Items_Menu.objects.filter(cat_id=1, sub_cat_id=5)
	sideslist = Items_Menu.objects.filter(cat_id=1, sub_cat_id=6)
	l_saladslist = Items_Menu.objects.filter(cat_id=2, sub_cat_id=7)
	lm_shareablelist = Items_Menu.objects.filter(cat_id=2, sub_cat_id=8)
	lm_sand_burgerlist = Items_Menu.objects.filter(cat_id=2, sub_cat_id=9)
	mains_list = Items_Menu.objects.filter(cat_id=3, sub_cat_id=10)
	grill_list = Items_Menu.objects.filter(cat_id=3, sub_cat_id=11)
	main_sides_list = Items_Menu.objects.filter(cat_id=3, sub_cat_id=12)
	pizzalist = Items_Menu.objects.filter(cat_id=4, sub_cat_id=13)
	kids_bf_list = Items_Menu.objects.filter(cat_id=5, sub_cat_id=15)
	kids_main_list = Items_Menu.objects.filter(cat_id=5, sub_cat_id=16)
	dessertslist = Items_Menu.objects.filter(cat_id=6, sub_cat_id=17)
	hotcoffeelist = Items_Menu.objects.filter(cat_id=7, sub_cat_id=18)
	coldcoffeelist = Items_Menu.objects.filter(cat_id=7, sub_cat_id=19)
	tealist = Items_Menu.objects.filter(cat_id=7, sub_cat_id=20)
	smoothie_list = Items_Menu.objects.filter(cat_id=8, sub_cat_id=21)
	milkshake_list = Items_Menu.objects.filter(cat_id=8, sub_cat_id=22)
	sparklers_list = Items_Menu.objects.filter(cat_id=8, sub_cat_id=23)
	juicelist = Items_Menu.objects.filter(cat_id=8, sub_cat_id=24)
	bottle_list = Items_Menu.objects.filter(cat_id=8, sub_cat_id=25)
	content['bottle_list'] = bottle_list
	content['juicelist'] = juicelist
	content['sparklers_list'] = sparklers_list
	content['milkshake_list'] = milkshake_list
	content['smoothie_list'] = smoothie_list
	content['tealist'] = tealist
	content['coldcoffeelist'] = coldcoffeelist
	content['hotcoffeelist'] = hotcoffeelist
	content['dessertslist'] = dessertslist
	content['kids_main_list'] = kids_main_list
	content['kids_bf_list'] = kids_bf_list
	content['pizzalist'] = pizzalist
	content['main_sides_list'] = main_sides_list
	content['grill_list'] = grill_list
	content['mains_list'] = mains_list
	content['lm_sand_burgerlist'] = lm_sand_burgerlist
	content['lm_shareablelist'] = lm_shareablelist
	content['FruitGrain_list'] = fruitgrainlist
	content['Sandwitch_list'] = sandwitchlist
	content['Meals_list'] = mealslist
	content['Eggs_list'] = eggslist
	content['l_saladslist'] = l_saladslist
	content['Sides_list'] = sideslist
	content['Sweets_list'] = sweetslist
	content['l_saladslist'] = l_saladslist
	if "emsg" in request.session:
		errormsg = request.session['emsg']
		content["errormsg"] = errormsg
		del request.session['emsg']
	if 'userid' in request.session.keys():
		print "in user"
		userid = request.session['userid']
		content['user_details'] = userid
		orderdate = time.strftime("%Y-%m-%d")
		if "orderid" in request.session:
			print "in order section"
			orderid = request.session['orderid']
			orderobj = OrderTrackingTable.objects.filter(userid=userid.userid, order_date = orderdate, order_id= orderid, order_type="yet_to_confirm")
		else:
			print "out of order section"
			orderobj = OrderTrackingTable.objects.filter(userid=userid.userid, order_date = orderdate, order_type="yet_to_confirm")
		total = 0
		for item in orderobj:
			total+=item.price
		content['total'] = total
		content['orderitems'] = orderobj
		return render_to_response(['index2.html','base2.html'], content, context_instance=RequestContext(request))	
	if "guestid" in request.session:
		guestid = request.session['guestid']
		orderdate = time.strftime("%Y-%m-%d")
		orderobj = OrderTrackingTable.objects.filter(userid=guestid,order_date = orderdate)
		total = 0
		for item in orderobj:
			total+=item.price
		content['total'] = total
		content['orderitems'] = orderobj
		return render_to_response("index.html", content, context_instance=RequestContext(request))
	else:
		return render_to_response("index.html", content, context_instance=RequestContext(request))

# User Registration
def UserRegister(request):
	content={}
	content.update(csrf(request))
	if request.method=="GET":
		return render_to_response("register.html", content, context_instance=RequestContext(request))	
	
	if request.method=="POST":
		fname = request.POST['first_name']
		lname = request.POST['last_name']
		password = request.POST['password']
		email = request.POST['email']
		# dob = request.POST['month']
		day = request.POST['day']
		month = request.POST['month']
		dob = str(day) +"-"+str(month)
		address1 = request.POST['Address']
		address2 = request.POST['Address2']
		address = address1 + address2
		area =  request.POST['Area']
		city = request.POST['city']
		# pcode = request.POST['post']
		phone = request.POST['phone']
		mobile = request.POST['mobile']
		hear = request.POST['Hear']
		emailobj = UserDetails.objects.filter(email = email)
		if emailobj:
			msg =  "User already exists with the given email id"
			content['errormsg'] = msg
			return render_to_response("register.html", content, context_instance=RequestContext(request))
		else:
			userobj = UserDetails()
			userobj.first_name = str(fname)
			userobj.last_name = str(lname)
			userobj.password = str(password)
			userobj.phone_no = str(phone)
			userobj.mobile = str(mobile)
			userobj.email = email
			day = request.POST['day']
			month = request.POST['month']
			# year = request.POST['year']
			userobj.dob = str(day) +"-"+str(month)
			# userobj.dob = str(dob)
			userobj.how_abt_us =hear
			userobj.save()
			userdetails = UserDetails.objects.get(email = email)
			addobj = UserAddress()
			addobj.userid = int(userdetails.userid)
			addobj.address =  address
			addobj.area =  area
			# addobj.po_box = pcode
			addobj.city = city
			uid = addobj.save()
			print "uid",uid
			subject="Account Confirmation"
			content=Context({"firstname":fname,"email":email,"password":password})
			htmltemplate=get_template("htmlmessage.html")
			htmlt=htmltemplate.render(content)
			to=[email]
			by="info@anipr.in"
			msg=EmailMultiAlternatives(subject,"",by,to)
			msg.attach_alternative(htmlt, "text/html") 
			msg.send() 
			content['success_msg'] = "Thank you for registering. Please check your email to activate your account."
			return HttpResponseRedirect("/success")
# SuccessMessage
def SuccessMessage(request):
	content={}
	if request.method=="GET":
		content['success'] = "Thank you for registering. Please check your email to activate your account."
		return render_to_response("register.html", content, context_instance=RequestContext(request))


# User Verification

def UserVerification(request):
	if request.method== "GET":
		email = request.GET['email']
		code = request.GET['vcode']
		userobj = UserDetails.objects.filter(email=str(email), verification_code =str(code))
		print type(userobj)
		if userobj:
			userobj[0].is_active = int(1)
			userobj[0].save()
			return HttpResponseRedirect("/userverified")
		else:
			return HttpResponseRedirect("/falseverfication")

def UserVerified(request):
	content={}
	if request.method == "GET":
		return render_to_response("usersuccess.html")

def Verification_Failed(request):
	if request.method=="GET":
		return render_to_response("Failed.html")
#User login
def UserLogin(request):
	content={}
	if request.method =="GET":
		return HttpResponseRedirect("/")
	if request.method == "POST":
		username = request.POST['UserName']
		password = request.POST['Password']
		userobj = UserDetails.objects.filter(email=str(username), password=str(password))
		if userobj:
			request.session['userid'] = userobj[0]
			if "guestid" in request.session:
				guestid = request.session['guestid']
				orderdate = time.strftime("%Y-%m-%d")
				orderlist  = OrderTrackingTable.objects.filter(userid=guestid, order_date=orderdate, order_type="yet_to_confirm")
				for item in orderlist:
					item.userid=userobj[0].userid
					item.save()
			return HttpResponseRedirect("/")
		else:
			errormsg = "Invalid user credentials"
			request.session['emsg'] = errormsg
			return HttpResponseRedirect("/")

#user logout
def Logout(request):
	if request.method=="GET":
		for key in request.session.keys():
			del request.session[key]
		return HttpResponseRedirect("/")

#User Profile
@user_login_required
def UserProfile(request):
	content = {}
	if request.method == "GET":
		userobj = request.session['userid']
		userdetails = UserDetails.objects.get(userid=userobj.userid)
		address = UserAddress.objects.filter(userid=userobj.userid)
		content['addressobj'] = address
		content['user_details'] = userdetails
		return render_to_response(['myprofile.html'], content, context_instance=RequestContext(request))

	if request.method == "POST":
		if 'userid' in request.POST:
			print request.POST['userid']
			userid = request.POST['userid']
			userobj = UserDetails.objects.get(userid=int(userid))
			userobj.first_name = request.POST['firstname']
			userobj.last_name = request.POST['lastname']
			oldpwd = request.POST['oldpwd']
			userobj = request.session['userid']
			if oldpwd != userobj.password:
				content['invalid_oldpwd'] = 'Invalid Old Password Please Try Again'
				return render_to_response("myprofile.html", content, context_instance=RequestContext(request))
			userobj.password = request.POST['password']
			userobj.phone_no = request.POST['phone']
			userobj.mobile = request.POST['mobile']
			userobj.email = request.POST['email']
			month = request.POST['month']
			day = request.POST['day']
			dob = day+'/'+month
			userobj.dob = dob
			userobj.company = request.POST['company']
			userobj.save()
			content['edit_success'] = 'Your Data Successfully Updated'
			return render_to_response("myprofile.html", content, context_instance=RequestContext(request))
# Displaying list of addresses
@user_login_required
def ShowAddress(request):
	content = {}
	if request.method == "GET":
		userobj = request.session['userid']
		userdetails = UserDetails.objects.get(userid=userobj.userid)
		address = UserAddress.objects.filter(userid=userobj.userid)
		content['addressobj'] = address
		content['user_details'] = userdetails
		return  render_to_response("Address_List.html", content ,context_instance=RequestContext(request))

@user_login_required
#Adding new address of a user
def AddNewAddress(request):
	content={}
	content.update(csrf(request))
	if request.method=="GET":
		userobj = request.session['userid']
		userdetails = UserDetails.objects.get(userid=userobj.userid)
		address = UserAddress.objects.filter(userid=userobj.userid)
		content['user_details'] = userdetails
		return render_to_response("AddNewAddress.html", content, context_instance=RequestContext(request))

	if request.method=="POST":
		userobj = request.session['userid']
		street = request.POST['street']
		add = request.POST['address']
		address = street +','+ add
		phone_no = request.POST['phone']
		area =  request.POST['Area']
		if 'primary' in request.POST:
			is_primary = request.POST['primary']
		else:
			is_primary = "false"
		addressobj = UserAddress()
		addressobj.userid = userobj.userid
		addressobj.address = address
		addressobj.phone = phone_no
		addressobj.area = area
		addressobj.is_primary = is_primary
		addressobj.save()
		return HttpResponseRedirect("/myprofile")

@user_login_required
#Editing existing address
def EditAddress(request):	
	content={}
	if request.method=="GET":
		addressid =  request.GET['add_id']
		addressobj =  UserAddress.objects.get(id=addressid)
		content['add_details'] = addressobj
		return render_to_response("EditAddress.html", content, context_instance=RequestContext(request))
	if request.method=="POST":
		add_id = request.POST['id']
		address = request.POST['address']
		phone = request.POST['phone']
		area =  request.POST['Area']
		if "primary" in request.POST:
			primary = request.POST['primary']
		else:
			primary = "false"
		addressobj =  UserAddress.objects.get(id=add_id)
		addressobj.address = address
		addressobj.area = area
		addressobj.phone = phone
		addressobj.is_primary = primary
		addressobj.save()
		return HttpResponseRedirect("/address")

@user_login_required
#Deleting the existing address
def DeleteAddress(request):
	if request.method=="GET":
		addressid =  request.GET['add_id']
		addressobj = UserAddress.objects.get(id=addressid)
		addressobj.delete()
		return HttpResponseRedirect("/address")

#User Forgot password
def ForgotPwd(request):
	content = {}
	content.update(csrf(request))
	if request.method=="POST":
		email=request.POST['email']
		user_obj=UserDetails.objects.filter(email=email)
		subject="Password Recovery"
		# message="Hi "+user_obj[0].first_name +" How's the day Your Password : "+user_obj[0].password
		# send_mail(subject,message,"info@anipr.in",[user_obj[0].email])
		content=Context({"firstname":user_obj[0].first_name,"email":email,"password":user_obj[0].password})
		pwdtemplate=get_template('forgot_pwd.html')
		htmlt=pwdtemplate.render(content)
		to=[email]
		by="info@pantrycafe.me"
		msg=EmailMultiAlternatives(subject,"",by,to)
		msg.attach_alternative(htmlt, "text/html") 
		msg.send() 
		return HttpResponseRedirect("/sentpwd")
	return render_to_response('forgotpwd.html',content, context_instance=RequestContext(request))


#Sending password to the user
def SentPwd(request):
	content = {}
	content.update(csrf(request))
	content['success_msg'] = 'Please check you mail password has been sent to your registered email id.'
	return render_to_response('forgotpwd.html',content, context_instance=RequestContext(request))




def UserFeedBack(request):
	content={}
	if request.method=="GET":
		if "userid" in request.session:
			userid = request.session['userid']
			userobj = UserDetails.objects.get(userid=userid.userid)
			content['user_details'] = userobj
			return render_to_response("customer/feedback.html", content, context_instance=RequestContext(request))
		else:
			return render_to_response("feedback.html", content, context_instance=RequestContext(request))
	
	if request.method=="POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		message = request.POST['message']
		if "userid" in request.session:
			userid = request.session['userid']
			fbobj =  FeedBack()
			fbobj.userid= userid.userid
			fbobj.first_name = firstname
			fbobj.last_name = lastname
			fbobj.email =  email
			fbobj.message = message
			fbobj.save()
			return  HttpResponseRedirect("/guestsuccess")
		else:
			fbobj =  FeedBack()
			fbobj.first_name = firstname
			fbobj.last_name = lastname
			fbobj.email =  email
			fbobj.message = message
			fbobj.save()
			return  HttpResponseRedirect("/guestsuccess")

def GuestSuccess(request):
	content ={}
	if request.method=="GET":
		if "userid" in request.session:
			userdetails = request.session['userid']
			content['user_details']=userdetails
			return render_to_response("customer/guestsuccess.html",content, context_instance=RequestContext(request))
		else:
			return render_to_response("guestsuccess.html", content, context_instance=RequestContext(request))

def UserContactUs(request):
	content = {}
	content.update(csrf(request))
	if request.method=="GET":
		if "userid" in request.session:
			userdetails = request.session['userid']
			content['user_details']=userdetails
			return render_to_response("customer/contactus.html", content, context_instance=RequestContext(request))
		else:
			return render_to_response("contactus.html", content, context_instance=RequestContext(request))
	if request.method=="POST":
		if "userid" in request.session:
			userobj = request.session["userid"]
			conobj = ContactUs()
			conobj.user_id = userobj.userid
			conobj.first_name = request.POST['firstname']
			conobj.last_name = request.POST['lastname']
			conobj.company = request.POST['company']
			conobj.email = request.POST['email']
			conobj.pobox = request.POST['pobox']
			conobj.mobile = request.POST['phone']
			conobj.comments = request.POST['comments']
			conobj.save()
			return HttpResponseRedirect("/consucces")

		else:
			conobj = ContactUs()
			conobj.first_name = request.POST['firstname']
			conobj.last_name = request.POST['lastname']
			conobj.company = request.POST['company']
			conobj.email = request.POST['email']
			conobj.pobox = request.POST['pobox']
			conobj.mobile = request.POST['phone']
			conobj.comments = request.POST['comments']
			conobj.save()
			return HttpResponseRedirect("/consucces")

def ContactSuccess(request):
	content={}
	if request.method=="GET":
		if "userid" in request.session:
			userobj = request.session['userid']
			content['user_details'] = userobj
			return render_to_response("customer/consuccess.html", content, context_instance=RequestContext(request))
		else:
			return render_to_response("consuccess.html", content, context_instance=RequestContext(request))

def OrderItem(request):
	content={}
	content.update(csrf(request))
	itemid = request.POST['itemid']
	sub_cat_id = request.POST['subcatid']
	cat_id = request.POST['cat_id']
	quantity = request.POST['quantity']
	print itemid, sub_cat_id, cat_id 
	if request.method == 'POST':
		if 'userid' in request.session:
			print "in user"
			user_obj = request.session['userid']
			bf_ids_list = OrderTrackingTable.objects.filter(userid = user_obj.userid,cat_id= int(cat_id), sub_cat_id= int(sub_cat_id), item_id=int(itemid), order_type='yet_to_confirm')
			if bf_ids_list:
				print "blist"
				bf_ids_list[0].quantity = int(bf_ids_list[0].quantity) + int(quantity)
				bfobj = itemobj = Items_Menu.objects.get(cat_id=int(cat_id), sub_cat_id=int(sub_cat_id), item_id=itemid)
				bf_ids_list[0].price = int(bfobj.price) * bf_ids_list[0].quantity
				bf_ids_list[0].save()
			else:	
				print "in else"
				orderobj = OrderTrackingTable()
				itemobj = Items_Menu.objects.get(cat_id=int(cat_id), sub_cat_id=int(sub_cat_id), item_id=itemid)
				orderobj.cat_id = itemobj.cat_id
				orderobj.sub_cat_id = itemobj.sub_cat_id
				orderobj.item_id = itemobj.item_id
				orderobj.extras = itemobj.ingrediants
				orderobj.name = itemobj.item_name
				orderobj.price = itemobj.price
				if "orderid" in request.session:
					orderobj.order_id = request.session['orderid']
				else:
					orderid  =  random.randint(1000, 10000)
					request.session['orderid'] = orderid
					orderobj.order_id = orderid
				orderobj.quantity = int(quantity)
				orderobj.userid = int(user_obj.userid)
				orderobj.save()
			return HttpResponseRedirect('/')
		else:
			orderobj = OrderTrackingTable()
			orderobj.quantity = int(quantity)
			orderobj.item_id = int(itemid)
			orderobj.sub_cat_id = int(sub_cat_id)
			orderobj.cat_id = cat_id
			if "guestid" in request.session:
				print "i am in guest"
				guestid = request.session['guestid']
				bf_ids_list = OrderTrackingTable.objects.filter(userid = guestid,item_id=itemid,order_type='yet_to_confirm')
				if bf_ids_list:
					bf_ids_list[0].quantity = int(bf_ids_list[0].quantity) + int(quantity)
					bfobj = itemobj = Items_Menu.objects.get(cat_id=int(cat_id), sub_cat_id=int(sub_cat_id), item_id=itemid)
					bf_ids_list[0].price = int(bfobj.price) * bf_ids_list[0].quantity
					bf_ids_list[0].save()
					return HttpResponseRedirect("/")
				else:
					orderobj.userid = guestid
				itemobj = Items_Menu.objects.get(cat_id=int(cat_id), sub_cat_id=int(sub_cat_id), item_id=itemid)
				orderobj.cat_id = itemobj.cat_id
				orderobj.sub_cat_id = itemobj.sub_cat_id
				orderobj.item_id = itemobj.item_id
				orderobj.extras = itemobj.ingrediants
				orderobj.name = itemobj.item_name
				orderobj.price = itemobj.price
				if "orderid" in request.session:
					orderobj.order_id = request.session['orderid']
				else:
					orderid  =  random.randint(1000, 10000)
					request.session['orderid'] = orderid
					orderobj.order_id = orderid
			else:
				print "guest not created"
				itemobj = Items_Menu.objects.get(cat_id=int(cat_id), sub_cat_id=int(sub_cat_id), item_id=itemid)
				orderobj.cat_id = itemobj.cat_id
				orderobj.sub_cat_id = itemobj.sub_cat_id
				orderobj.item_id = itemobj.item_id
				orderobj.extras = itemobj.ingrediants
				orderobj.name = itemobj.item_name
				orderobj.price = itemobj.price
				if "orderid" in request.session:
					orderobj.order_id = request.session['orderid']
				else:
					orderid  =  random.randint(1000, 10000)
					request.session['orderid'] = orderid
					orderobj.order_id = orderid
				if "guestid" in request.session:
					orderobj.orderid = request.session['guestid']
				else:
					guestid = random.randint(1000, 10000)
					request.session['guestid'] = guestid
					orderobj.userid = guestid
			orderobj.save()
			return HttpResponseRedirect("/")

	return render_to_response(['index2.html','base2.html'], content, context_instance=RequestContext(request))	

#@user_login_required
def DeleteOrder(request):
	if request.method=="POST":
		orderid= request.POST['orderid']
		itemid = request.POST['itemid']
		orderobj = OrderTrackingTable.objects.get(order_id=orderid, item_id=itemid)
		orderobj.delete()
		return HttpResponseRedirect("/")


def Checkout(request):
	content = {}
	areadict = {}
	if request.method=="GET":
		order_id = ''
		if "or_id" in request.GET:
			order_id = request.GET['or_id']
			print "order_id",order_id
		total = 0
		if "userid" in request.session:
			userobj =  request.session['userid']
			orderdate = time.strftime("%Y-%m-%d")
			if order_id:
				print "we are in order"
				orderobj = OrderTrackingTable.objects.filter(userid=userobj.userid, order_type="confirmed",order_id=order_id)
			else:
				if "orderid" in request.session:
					orderid = request.session['orderid']
					orderobj = OrderTrackingTable.objects.filter(userid=userobj.userid, order_id=orderid, order_type="yet_to_confirm")
				else:
					pass
			for item in orderobj:
				total+=item.price
			content['total'] = total
			content['grandtotal'] = total+5
			content['items'] = orderobj
			addresobj = UserAddress.objects.filter(userid=userobj.userid, is_primary=True)
			for ad in addresobj:
				adlist = []
				adlist.append(addresobj[0].address)
				adlist.append(addresobj[0].phone)
				areaobj = AreaDetails.objects.get(areacode=ad.area)
				if areaobj:
					adlist.append(areaobj.areaname)
				areadict[ad.area] = adlist
			content["addresslist"] = areadict
			content["user_details"] = userobj
			return render_to_response("customer/checkout.html", content, context_instance=RequestContext(request))
		if "guestid" in request.session:
			guestid =  request.session['guestid']
			orderdate = time.strftime("%Y-%m-%d")
			orderobj = OrderTrackingTable.objects.filter(userid=guestid, order_date=orderdate, order_type="yet_to_confirm")
			for item in orderobj:
				total+=item.price
			content['total'] = total
			content['grandtotal'] = total+5
			content['items'] = orderobj
			return render_to_response("checkout.html", content, context_instance=RequestContext(request))
	if request.method=='POST':
		if "item_id" in request.POST:
			itemid = request.POST['item_id']
			request = request.POST['request']
			orderobj = OrderTrackingTable.objects.get(id=itemid)
			orderobj.special_req = request
			orderobj.save()
			return HttpResponseRedirect('/checkout')
		return HttpResponseRedirect('/checkout')

def HowToOrder(request):
	content={}
	if request.method=="GET":
		if "userid" in request.session:
			userobj = request.session['userid']
			userdetails = UserDetails.objects.get(userid=userobj.userid)
			content['user_details'] = userdetails
			return render_to_response("customer/how-to-order.html", content, context_instance=RequestContext(request))
		else:
			return render_to_response("how-to-order.html", content, context_instance=RequestContext(request))


@user_login_required
def ConfirmOrder(request):
	content={}
	if request.method=="POST":
		if "userid" in request.session:
			userobj = request.session['userid']
			total = 0
			content['user_details'] = userobj
			orderdate = time.strftime("%Y-%m-%d")
			orderid = request.session['orderid']
			orderobj = OrderTrackingTable.objects.filter(userid=userobj.userid, order_id=orderid)
			for item in orderobj:
				total+=item.price
				item.order_type = "confirmed"
				item.save()
			content['total'] =  total
			content['grandtotal'] = total+5
			content['items'] = orderobj
			if "orderid" in request.session:
				orderid = request.session['orderid']
				content['orderid'] = orderid
				del request.session['orderid']
			return render_to_response("customer/order_placed.html", content, context_instance=RequestContext(request))


def ClearOrder(request):
	content = {}
	if "userid" in request.session:
		userobj = request.session['userid']
		orderdate = time.strftime("%Y-%m-%d")
		bf_obj_list = OrderTrackingTable.objects.filter(userid = userobj.userid,order_type='yet_to_confirm', order_date=orderdate)
		for obj in bf_obj_list:
			obj.delete()
		return HttpResponseRedirect('/')

	if 'guestid' in request.session:
		guestid = request.session['guestid']
		orderdate = time.strftime("%Y-%m-%d")
		bf_obj_list = OrderTrackingTable.objects.filter(userid = guestid,order_type='yet_to_confirm', order_date=orderdate)
		for obj in bf_obj_list:
			obj.delete()
		return HttpResponseRedirect('/')

def OrderHistory(request):
	content = {}
	if "userid" in request.session:
		userobj = request.session['userid']
		orders_obj_list_duplicate = OrderTrackingTable.objects.filter(userid = userobj.userid,order_type='confirmed')
		orders_obj_list = []
		all_order_ids = []
		for order in orders_obj_list_duplicate:
			if order.order_id in all_order_ids:
				pass
			else:
				orders_obj_list.append(order)
				all_order_ids.append(int(order.order_id))
		print orders_obj_list
		content['order_list'] = orders_obj_list	
		content['user_details'] = userobj
	return render_to_response('order_history1.html', content, context_instance=RequestContext(request))

def OrderDetails(request):
	content = {}
	if 'or_id' in request.GET:
		order_id = request.GET['or_id']
		userobj = request.session['userid']
		order_obj_list = OrderTrackingTable.objects.filter(userid = userobj.userid,order_type='confirmed',order_id=order_id)
		total = 0
		for order in order_obj_list:
			total+=int(order.price)
		content['order_history'] = order_obj_list
		content['total'] = total
		content['gtotal']=total+5		
	return render_to_response('target_order.html', content, context_instance=RequestContext(request))


@user_login_required
def CheckoutAddNewAddress(request):
	content={}
	content.update(csrf(request))
	if request.method=="GET":
		userobj = request.session['userid']
		userdetails = UserDetails.objects.get(userid=userobj.userid)
		address = UserAddress.objects.filter(userid=userobj.userid)
		content['user_details'] = userdetails
		return render_to_response("checkoutaddress.html", content, context_instance=RequestContext(request))

	if request.method=="POST":
		userobj = request.session['userid']
		address = request.POST['address']
		phone_no = request.POST['phone']
		area =  request.POST['Area']
		if 'primary' in request.POST:
			is_primary = request.POST['primary']
		else:
			is_primary = "false"
		addressobj = UserAddress()
		addressobj.userid = userobj.userid
		addressobj.address = address
		addressobj.phone = phone_no
		addressobj.area = area
		addressobj.is_primary = is_primary
		addressobj.save()
		return HttpResponseRedirect("/checkout")

def ChangeItem(request):
	total_cost=0
	content.update(csrf(request))
	if request.method=="GET":
		itemid = request.GET['itemid']
		price = request.GET['price']
		quantity = request.GET['quantity']
		orderid = request.GET['orderid']
		item =  Items_Menu.objects.get(item_id=int(itemid))
		itemobj = OrderTrackingTable.objects.get(order_id= int(orderid),item_id=int(itemid))
		itemobj.price = int(item.price) * int(quantity)
		itemobj.quantity = int(quantity)
		itemobj.save()
		itemlist = OrderTrackingTable.objects.filter(order_id=orderid)
		print len(itemlist)
		for item in itemlist:
			total_cost = total_cost + int(item.price)
		
		tcost = str(total_cost)
		print tcost
		return HttpResponse(tcost)
def AddRequest(request):
	content = {}
	if 'item_id' in request.GET:
		itemid = request.GET['item_id']
		request = request.GET['text']
		orderobj = OrderTrackingTable.objects.get(id=itemid)
		orderobj.special_req =request
		orderobj.save() 
		return HttpResponse(request)

