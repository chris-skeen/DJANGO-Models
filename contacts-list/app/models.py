from django.db import models

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=15)
  is_favorite = models.BooleanField()


def create_contact(name, email, phone, is_favorite):
  new_contact = Contact.objects.create(name=name, email=email, phone=phone, is_favorite=is_favorite)
  return new_contact
  
def all_contacts():
  return Contact.objects.all()

def find_contact_by_name(name):
  for i in Contact.objects.all():
    if i.name == name:
      print(i)
      return i
    else:
      continue

def favorite_contacts():
  return Contact.objects.filter(is_favorite=True)

def update_contact_email(name, new_email):
  obj = Contact.objects.get(name=name)
  obj.email = new_email
  obj.save()

def delete_contact(name):
  try:
    obj = Contact.objects.get(name=name)
    obj.delete()
  except:
    print("error")