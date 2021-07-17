from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration, Registratione
from .forms import RegistrationForm, LoginForm ,RegistrationForme
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
	name = "renoj"
	return render(request,'index.html',{'name':name})

def registration(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST or None,request.FILES or None)
		if form.is_valid():
			fname = form.cleaned_data['Firstname']
			lname = form.cleaned_data['Lastname']
			age = form.cleaned_data['Age']
			email = form.cleaned_data['Email']
			photo = form.cleaned_data['Photo']
			password = form.cleaned_data['Password']
			ur = Registration.objects.filter(Email=email).exists()
			if ur:
				msg = "Email already exists"
				return render(request,'registration.html',{'message':msg})
			else:
				tab = Registration(Firstname=fname,Lastname=lname,Age=age,Email=email,Photo=photo,Password=password)
				tab.save()
				return redirect('/login')
	else:
		form = RegistrationForm()
	return render(request,'registration.html',{'form':form})


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['Email']
			password = form.cleaned_data['Password']
			ur = Registration.objects.get(Email=email)
			if not ur:
				msg = "email id does not exist"
				return render(request,'login.html',{'message':msg})
			elif password != ur.Password:
				msg = "Password mismatched"
				return render(request,'login.html',{'message':msg})
			else:
				request.session['sid']=ur.id
				return redirect('/userhome/% s' %ur.id)
	else:
		data = LoginForm()
		return render(request,'login.html',{'data':data})



def userhome(request,id):
	if request.session.has_key:
		uid = request.session['sid']
		user = Registration.objects.get(id=id)
		return render (request,'homepage.html',{'user':user})


def edit_profile(request,id):
	uid = request.session['sid']
	user = Registration.objects.get(id=id)
	form = UpdateForm(request.POST or None,instance = user)


	if form.is_valid():
		firstname = form.cleaned_data['Firstname']
		lastname = form.cleaned_data['Lastname']
		email = form.cleaned_data['Email']
		age = form.cleaned_data['Age']
		ur = user(id=id,Firstname=firstname,Lastname=lastname,Email=email,Age=age)
		ur.save()
		message.success(request,"Updated sucessfully")
		return redirect('/user_home/%s'%id)
		return render(request,'update.html',{'form':form,'user':user})

def Destroy(request,id):
	ur = Registration.objects.get(id=id)
	ur.delete()
	return redirect('/login')


def change_password(request,id):
	user = Registration.objects.get(id=id)
	uid = request.session['id']
	if request.method == 'POST':
		form = ChangePass(request.POST)
		if form.is_valid():
			oldpassword = form.cleaned_data['oldpassword']
			newpassword = form.cleaned_data['newpassword']
			confirm_password = form.cleaned_data['confirm_password']
			if oldpassword != user.password:
				msg = "enter correct password"
				return render (request,'change_password.html',{'form':form,'error':msg,'use':use})
			elif newpassword !=confirm_password:
				msg = "entered password don't match"
				return render (request,'changepassword.html',{'form':form,'error':msg,'user':user})
			else:
				user.password = newpassword
				user.Confirmpassword = confirm_password
				user.save()
				return redirect('/home/%s' % user.id)
				return render(request,'changepassword.html',{'form':form,'error':msg,'user':user})
	else:
		form = ChangePass()
	return render(request,'changepassword.html',{'form':form,'user':user})



# def AddGalleryDetails(request):
# 	if request.method == "POST":
# 		form = ImageGallery(request.POST or None,request.FILES or None)
# 		if form.is_valid():
# 			pname = form.cleaned_data['Picname']
# 			photo = form.cleaned_data['Photo']
# 			desc = form.cleaned_data['Description']
# 			price = form.cleaned_data['Price']
# 			tab = GalleryDetails(Picname = pname, Photo = photo, Description = desc, Price = price)
# 			tab.save()
# 			return redirect('/login')
# 	else:
# 		form = ImageGallery()
# 	return render(request,'gallery.html',{'form':form})


def registratione(request):
	if request.method == "POST":
		form = RegistrationForme(request.POST or None,request.FILES or None)
		if form.is_valid():
			pname = form.cleaned_data['Picturename']
			desc = form.cleaned_data['Description']
			price = form.cleaned_data['Price']
			photo = form.cleaned_data['Photo']
			ur = Registratione.objects.filter(Description=desc).exists()
			if ur:
				msg = "Email already exists"
				return render(request,'registratione.html',{'message':msg})
			else:
				tab = Registratione(Picturename=pname,Description=desc,Price=price,Photo=photo)
				tab.save()
				return redirect('/login')
	else:
		form = RegistrationForme()
	return render(request,'registratione.html',{'form':form})


def printimages(request):
		user = Registratione.objects.all()
		return render (request,'gallery.html',{'user':user})


