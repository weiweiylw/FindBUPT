from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=80)
    position_x = models.CharField(max_length=10)
    position_y = models.CharField(max_length=10)

    def __unicode__(self):
        return self.location_name   


class Tag(models.Model):
    key = models.CharField(max_length=10)
    reference_count = models.IntegerField(max_length=50)

    def __unicode__(self):
        return self.key

class Card(models.Model):
    name = models.CharField(max_length=30)
    student = 'ST'
    teacher = 'TC'
    staff = 'SF'
    type_choice = (
        (student, 'student'),
        (teacher, 'teacher'),
        (staff, 'staff'),
    )
    type_status = models.CharField(max_length=2, choices=type_choice, default='NULL')
    praise_count = models.IntegerField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    card = models.ForeignKey(Card)

    def __unicode__(self):
        return u'%s %s' % (self.user, self.card)


class Department(models.Model):
    name = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    location = models.ManyToManyField(Location)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        abstract = True


class PublicNotice(Notice):
    author = models.ForeignKey(Department, blank=True, null=True)
    pub_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __unicode__(self):
        return self.title


class PersonalNotice(Notice):
    author = models.ForeignKey(UserProfile)
    pub_time = models.DateTimeField(auto_now_add=True)