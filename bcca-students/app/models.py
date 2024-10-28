from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=100)
  class_of = models.CharField(max_length=4)
  email = models.CharField(max_length=80)
  enrolled = models.BooleanField()


def create_student(name, class_of, email, enrolled):
  new_student = Student.objects.create(name=name, class_of=class_of, email=email, enrolled=enrolled)
  return new_student

def all_students():
  return Student.objects.all()

def find_student_by_name(name):
  for i in Student.objects.all():
    if i.name == name:
      print(i)
      return i
    else:
      continue

def enrolled_students():
  return Student.objects.filter(enrolled=True)

def update_student_email(name, new_email):
  obj = Student.objects.get(name=name)
  obj.email = new_email
  obj.save()


def delete_student(name):
  try:
    obj = Student.objects.get(name=name)
    obj.delete()
  except:
    print("error")