from django.shortcuts import render
from django.contrib.auth.models import User as auth_user
from django.http import JsonResponse
from django.contrib.auth import authenticate
import json
from random import randint

from .models import *

# Create your views here.

def get_session_obj(token):
    return Session.objects.filter(token = token).first()

def check_session(session):
    return (session is None) or (not session.status)

def create_new_user(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_name = body['name']
        user_email = body['email']
        user_password = body['password']

        isUserExists = auth_user.objects.filter(email=user_email).first()
        if isUserExists:
            return JsonResponse({'status':'User Already Exists'})
        else:
            new_auth_user = auth_user.objects.create_user(username = user_name, email=user_email, password=user_password)
            if new_auth_user:
                new_user = User()
                new_user.to_db(body)
                new_user.save()
                return JsonResponse({'status':'User Created Successfully'})
            else:
                return JsonResponse({'status':'Failed to Create New User'})
    
    else:
        return JsonResponse({'status':'Invalid Request Method, only POST Method is Allowed'})

def update_user(request):
    if request.method == 'POST':
        token = request.headers['token']
        session_obj = get_session_obj(token)
        if check_session(session_obj):
            return JsonResponse({'status': 'User not Logged in'})
        else:
            body = json.loads(request.body)
            user_obj = User.objects.filter(id = session_obj.user.id).first()
            user_obj.to_db(body)
            user_obj.save()
            return JsonResponse({'status': 'User Details Updated Successfully'})
    
    else:
        return JsonResponse({'status': 'Invalid Request Method, Only POST Method is Allowed'})

def delete_user(request):
    if request.method == 'POST':
        token = request.headers['token']
        session_obj = get_session_obj(token)
        if check_session(session_obj):
            return JsonResponse({'status': 'User not Logged in'})
        else:
            auth_obj = auth_user.objects.filter(email = session_obj.user.email)
            auth_obj.delete()

            user_obj = User.objects.filter(id = session_obj.user.id).first()
            user_obj.delete()
            return JsonResponse({'status': 'User Deleted Successfully'})
    
    else:
        return JsonResponse({'status': 'Invalid Request Method, Only POST Method is Allowed'})

def login_user(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_email = body['email']
        user_password = body['password']

        auth_obj = auth_user.objects.filter(email = user_email).first()
        if auth_obj is not None:
            user_obj = User.objects.filter(email = user_email).first()
            session_obj = Session.objects.filter(user = user_obj).first()
            if session_obj is None:
                token = randint(1000, 9999)
                data = {'token': token, 'status': True, 'user': user_obj}

                session_obj = Session()
                session_obj.to_db(data)
                session_obj.save()
                return JsonResponse({'status': 'User Logged in Successfully'})
            
            else:
                if session_obj.status:
                    return JsonResponse({'status': 'User Already Logged in'})
                else:
                    session_obj.status = True
                    session_obj.save()
                    return JsonResponse({'status': 'User Logged in Successfully'})
        
        else:
            return JsonResponse({'status': 'User Does Not Exist'})
    
    else:
        return JsonResponse({'status': 'Invalid Request Method, Only POST Method is Allowed'})
    
def logout_user(request):
    if request.method == 'POST':
        token = request.headers['token']
        session_obj = get_session_obj(token)
        if check_session(session_obj):
            return JsonResponse({'status': 'User not Logged in'})
        else:
            session_obj.status = False
            session_obj.save()
            return JsonResponse({'status': 'User Logged out Successfully'})
    else:
        return JsonResponse({'status': 'Invalid Request Method, Only POST Method is Allowed'})

