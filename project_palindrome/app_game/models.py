from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def to_db(self, data):
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']

class Session(models.Model):
    token = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def to_db(self, data):
        self.token = data['token']
        self.status = data['status']
        self.user = data['user']

class Game(models.Model):
    game_string = models.CharField(max_length=255, default='')
    is_palindrome = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

