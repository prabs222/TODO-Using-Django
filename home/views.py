from django.shortcuts import render
from email.mime import image
from django.contrib.auth import authenticate, login , logout
from django.http import JsonResponse
import json,re
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import datetime
from datetime import date
from .models import *
# from Clouddemo.models import file/s, formats, images, userdp, users_dbs


# Create your views here.
def RegisterUser(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        Fname = body["fname"]
        Lname = body["lname"]
        Gender = body["gender"]
        Phone = body["phone_number"]
        Dob = body["dob"]
        User_name=body["username"]
        Email_Id=body["email"]
        Pass_word=body["pass"]
        C_Password = body["cpass"]
        emailformat = "^[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$"
        Phoneformat = "^[0-9]{10,10}$"
        if (not Fname):
            res = {'success': False,'message': 'First name is required'}
            return JsonResponse(res, status = 403)
        
        elif (not Gender):
            res = {'success': False,'message': 'Gender is required'}
            return JsonResponse(res, status = 403)
        
        elif (not Lname):
            res = {'success': False,'message': 'Last name is required'}
            return JsonResponse(res, status = 403)
        
        elif (not Dob):
            res = {'success': False,'message': 'DOB is required'}
            return JsonResponse(res, status = 403)
        
        elif (not Phone):
            res = {'success': False,'message': 'Phone Number is required'}
            return JsonResponse(res, status = 403)
        
        elif (not Email_Id):
            res = {'success': False,'message': 'Email Id is required'}
            return JsonResponse(res, status = 403)
        
        elif (not User_name):
            res = {'success': False,'message': 'Username is required'}
            return JsonResponse(res, status = 403)
        
        elif (not Pass_word):
            res = {'success': False,'message': 'Password is required'}
            return JsonResponse(res, status = 403)
        
        elif (not C_Password):
            res = {'success': False,'message': 'Confirm Password is required'}
            return JsonResponse(res, status = 403)
        
        elif (len(Pass_word)<6):
            res = {'success': False,'message': 'Password cannot be less then 6 characters'}
            return JsonResponse(res, status = 403)
        
        elif (len(Pass_word) >16):
            res = {'success': False,'message': 'Password cannot be more than 16 characters'}
            return JsonResponse(res, status = 403)
        
        elif (User.objects.filter(username = User_name)):
            res = {'success': False,'message': 'Username Already Exists'}
            return JsonResponse(res, status = 403)
        
        elif (users_db.objects.filter(phone_num  = Phone)):
            res = {'success': False,'message': 'Phone number already used'}
            return JsonResponse(res, status = 403)
        
        elif (User  .objects.filter(email = Email_Id)):
            res = {'success': False,'message': 'Email id Already Exists'}
            return JsonResponse(res, status = 403)
        
        emailvalidator = re.search(emailformat, Email_Id)
        if(not emailvalidator):
                res = {'success': False,'message': 'Email Format does not Match'}     
                return JsonResponse(res,status = 403)
        Phonevalidator = re.search(Phoneformat, str(Phone))
        
        if(not Phonevalidator):
                res = {'success': False,'message': 'Phone Munber Format does not Match'}           
                return JsonResponse(res , status = 403)
        DobO = datetime.datetime.strptime(Dob, '%Y-%m-%d')
        today = date.today()
        A_age = today.year - DobO.year - ((today.month, today.day) < (DobO.month, DobO.day))
        print(A_age)
        if Pass_word == C_Password:
            newUser = User.objects.create_user(first_name=Fname, last_name = Lname, email=Email_Id,  username=User_name,password=Pass_word)
            userdata = users_db(user = newUser,  phone_num = Phone , gender = Gender , dob = Dob )
            userdata.save()
        else:
            res = {'success': False,'message': 'OOPS!! Password mismatch'}
            return JsonResponse(res , status = 403)
        res = {'success': True,'message': 'User Successfully Registered'}
        return JsonResponse(res, status = 200)
    else:
        res = {'success': False,'message': 'Invalid method of requesting'}
    return JsonResponse(res , status = 403)

def LoginUser(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body['email']
        password = body['password']
        username = User.objects.get(email = email).username
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            res = {'success': True,'message': 'Successfully logged in!!'}
            return JsonResponse(res,status = 200)
        else:
            res = {'success': False,'message': 'Wrong credentials!!'}
            return JsonResponse(res,status = 403)
    else:
        res = {'success': False,'message': 'Invalid method of requesting'}
    return JsonResponse(res , status = 403)


def logout_view(request):
    logout(request)
    res = {
        "message": "Logged out successfully!!"
    }
    return JsonResponse(res , status = 200)

def mylogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email = email).username
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Login successful")
            return render(request, 'dashboard.html')
            # res = {'success': True,'message': 'Successfully logged in!!'}
            # return JsonResponse(res,status = 200)
        else:
            res = {'success': False,'message': 'Wrong credentials!!'}
            return JsonResponse(res,status = 403)
    # else:
    #     res = {'success': False,'message': 'Invalid method of 51requesting'}
    return render(request , 'login.html')

def addTodo(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == 'POST':
            todo = request.POST.get('todo')
            Todos.objects.create(todo_name=todo,created_by=request.user)
        context['todos'] = Todos.objects.filter(created_by=request.user)
    return render(request,'dashboard.html',context)
        

    

# def Dashboard(request):
#     # if request.method == 'GET':
#         if request.user.is_authenticated:
#             userdata = users_db.objects.filter(user = request.user)[0]
#             if userdp.objects.filter(user_id = request.user.id).exists():
#                 dp = userdp.objects.get(user_id = request.user.id)
#             print(userdata.gender)
#             print(userdata.dob)
#             print(request)

#             print(request.user.get_full_name())
#             sum = 0
#             sizeobj = files.objects.filter(user_id = request.user.id).values('file')
#             for i in range(len(sizeobj)):
#                 obj = files.objects.filter(user_id = request.user.id)[i]
#                 sum = sum+  obj.file.size
#             res = {
#                 "username":  request.user.get_username(),
#                 "email": request.user.email,
#                 "name": request.user.get_full_name(),
#                 "fname": request.user.get_short_name(),
#                 "dob": userdata.dob.strftime("%d-%m-%Y") ,
#                 "gender": userdata.gender,
#                 "phone": userdata.phone_num,
                
#                 "dp": dp.pc.url,
#                 "size": sum
#             }
#             return JsonResponse(res, status = 200)
#         else:
#             res = {
#                 "success": False,
#                 "message": "You have to login first"
#             }
#             return JsonResponse(res,status = 403)

