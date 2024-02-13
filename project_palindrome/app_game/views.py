from django.contrib.auth.models import User as auth_user
from django.http import JsonResponse
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
        payload = json.loads(request.body)
        user_name = payload['name']
        user_email = payload['email']
        user_password = payload['password']

        isUserExists = auth_user.objects.filter(email=user_email).first()
        if isUserExists:
            return JsonResponse({'status':'User Already Exists'})
        else:
            new_auth_user = auth_user.objects.create_user(username = user_name, email=user_email, password=user_password)
            if new_auth_user:
                new_user = User()
                new_user.to_db(payload)
                new_user.save()
                return JsonResponse({'status':'User Created Successfully'})
            else:
                return JsonResponse({'status':'Failed to Create New User'})
    
    else:
        return JsonResponse({'status':'Invalid Request Method, only POST Method is Allowed'})

def update_user(request):
    if request.method == 'PUT':
        token = request.headers['token']
        session_obj = get_session_obj(token)
        if check_session(session_obj):
            return JsonResponse({'status': 'User not Logged in'})
        else:
            payload = json.loads(request.body)
            user_obj = User.objects.filter(id = session_obj.user.id).first()
            user_obj.to_db(payload)
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
        payload = json.loads(request.body)
        user_email = payload['email']
        user_password = payload['password']

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
                return JsonResponse({'status': 'User Logged in Successfully', 'token': token})
            
            else:
                if session_obj.status:
                    return JsonResponse({'status': 'User Already Logged in'})
                else:
                    session_obj.status = True
                    session_obj.save()
                    return JsonResponse({'status': 'User Logged in Successfully', 'token': session_obj.token})
        
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

def check_palindrome(string):
    return string == string[::-1]

def start_game(request):
    if request.method == 'GET':
        token = request.headers['token']
        session_obj = get_session_obj(token)
        if check_session(session_obj):
            return JsonResponse({'status': 'User not Logged in'})
        else:
            game = Game.objects.filter(session = session_obj).first()
            if game is not None:
                game.status = False
                game.save()
            
            new_game = Game()
            new_game.session = session_obj
            new_game.save()
            return JsonResponse({'status':'Game Started Successfully'})
    
    else:
        return JsonResponse({'status': 'Invalid Request Method, Only GET Method is Allowed'})

def get_board(request):
    if request.method == 'GET':
        token = request.headers['token']
        session_obj = get_session_obj(token)
        if check_session(session_obj):
            return JsonResponse({'status': 'User not Logged in'})
        else:
            game_obj = Game.objects.filter(session = session_obj).first()
            return JsonResponse({'string': game_obj.game_string})
    
    else:
        return JsonResponse({'status': 'Invalid Request Method, Only GET Method is Allowed'})

def update_board(request):
    if request.method == 'POST':
        token = request.headers['token']
        session_obj = get_session_obj(token)
        if check_session(session_obj):
            return JsonResponse({'status': 'User not Logged in'})
        else:
            game_obj = Game.objects.filter(session = session_obj).first()
            if len(game_obj.game_string) == 6:
                is_palindrome = check_palindrome(game_obj.game_string)
                game_obj.is_palindrome = is_palindrome
                game_obj.save()
                return JsonResponse({'status': 'Game String is a Palindrome (Cannot Update the Board Anymore)' if is_palindrome else 'Game String is not a Palindrome (Cannot Update the Board Anymore)'})
            else:
                payload = json.loads(request.body)
                game_obj.game_string = game_obj.game_string + payload['char'][0]
                game_obj.save()
                return JsonResponse({'status': 'Updated Game Board'})
    
    else:
        return JsonResponse({'status': 'Invalid Request Method, Only POST Method is Allowed'})
    
def get_game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        game_ids = []
        for each_game in games:
            print(each_game)
            game_ids.append(each_game.pk)
        return JsonResponse({'Games IDs': game_ids})
    else:
        return JsonResponse({'status': 'Invalid Request Method, Only GET Method is Allowed'})
