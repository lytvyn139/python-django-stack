from django.db import models
""" 
-Books can be published by many publishers and publishers can publish many books
Many publishers can have  
- 
"""
# Create your models here.
class User(models.Model):
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	gender = models.CharField(max_length=255, null = True)
	birthday = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
	likes = models.ManyToManyField(User, related_name="liked_messages")
	uploader = models.ForeignKey(User, related_name="messages_uploaded", on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

""" 
SELECT * FROM manytomanyApp_message;
SELECT * FROM manytomanyApp_user;

#this is many to many 
SELECT * FROM manytomanyApp_message_likes;

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell
from manytomanyApp.models import *

# create User
User.objects.create(firstName="BOT_1", lastName="LAST1", email="bot@gmail.com", gender="male", birthday="1990-05-10")
User.objects.create(firstName="BOT_2", lastName="LAST2", email="2bot@gmail.com", gender="female", birthday="1200-07-15")
User.objects.create(firstName="BOT_3", lastName="LAST3", email="3bot@gmail.com", gender="robot", birthday="1992-06-18")
User.objects.create(firstName="PES", lastName="DAHAL", email="smerduh32@gmail.com", gender="dog", birthday="2020-06-18")

# create Message, doesn't have to have "likes", likes still not created
Message.objects.create(content="wooof wooof", uploader=User.objects.get(id=4))
Message.objects.create(content="I want dogo food", uploader=User.objects.get(id=4))
Message.objects.create(content="Im a good boy! bark bark", uploader=User.objects.get(id=4))
Message.objects.create(content="Like this post now,", uploader=User.objects.get(id=4))

###################################################
# MAKE THE JOIN MANY TO MANY

# retrieve an instance of a user1
#user1 = User.objects.get(id=1).firstName #BOT_1

user1 = User.objects.get(id=1)
user2 = User.objects.get(id=2)
user3 = User.objects.get(id=3)

# retrieve an instance of a message with id4
#message4 = Message.objects.get(id=4).content #like this post now

message1 = Message.objects.get(id=1)
message2 = Message.objects.get(id=2)
message3 = Message.objects.get(id=3)
message4 = Message.objects.get(id=4)


#if you want to obj x like obj y, you can do it from either way
# now you want user#1 to like message#4 from message obj ???
#(make sure the message4 is = message4 = Message.objects.get(id=4)
# and not pointing to content or etc )

add = create many to many relationship
remove = remove many to many relationship
run the query to see updated: SELECT * FROM manytomanyApp_message_likes;

#Add from Message class
message4.likes.add(user1)
message4.likes.add(user2)
message3.likes.add(user1)

#Add from User class
user3.liked_messages.add(message4)

###################################################
#	LET"S SEE WHO LIKED WHAT ???
many to many is not in user class, but it has access in the related name
let's see that messages liked user 1
user1.liked_messages.all()

let's see all the users who like message 4
message4.likes.all()

how make likes was for message 4 ?
len(message4.likes.all())
""" 