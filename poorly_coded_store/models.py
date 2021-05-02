from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 2:
            errors["name"] = "Course's name should be at least 5 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Description should be at least 5 characters"
        return errors

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, related_name = 'messages', on_delete = models.CASCADE )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now = True) 

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name = 'comments', on_delete = models.CASCADE )
    user = models.ForeignKey(User, related_name = 'comments', on_delete = models.CASCADE )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now = True) 