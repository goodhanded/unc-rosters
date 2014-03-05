from django.db import models

# Create your models here.

class Player(models.Model):

    HANDS = (
        ('L/L', 'Bat Left/Throw Left'),
        ('L/R', 'Bat Left/Throw Right'),
        ('R/R', 'Bat Right/Throw Right'),
        ('R/L', 'Bat Right/Throw Left'),
        ('S/L', 'Switch Hit/Throw Left'),
        ('S/R', 'Switch Hit/Throw Right'),
    )

    student = models.ForeignKey('Student')
    team = models.ForeignKey('Team')
    position = models.CharField(max_length=25)
    number = models.IntegerField()
    hand = models.CharField(max_length=3, choices=HANDS)
    bio = models.TextField()
    photo = models.ImageField(upload_to='images/avatars/', blank=True, default='')

    def __unicode__(self):
        return U'%s %s (%s): %s %s' % (self.team.school.name, self.team.sport.name, self.team.gender, self.student.first_name, self.student.last_name)

class School(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta(object):
        ordering = ('name',)

    def __unicode__(self):
        return U'%s' % (self.name)

class Student(models.Model):

    YEARS = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    height = models.IntegerField() # Height in inches
    weight = models.IntegerField() # Weight in pounds
    hometown = models.CharField(max_length=50)
    highschool = models.CharField(max_length=50)
    year = models.CharField(max_length=2, choices=YEARS)

    class Meta(object):
        ordering = ('last_name','first_name',)

    def __unicode__(self):
        return U'%s, %s' % (self.last_name, self.first_name)

class Sport(models.Model):
    name = models.CharField(unique=True, max_length=50)
    image = models.ImageField(upload_to='images/sports/', blank=True, default='')

    class Meta(object):
        ordering = ('name',)

    def __unicode__(self):
        return U'%s' % (self.name)

class Team(models.Model):
    GENDERS = (
        ('M', 'Men\'s'),
        ('W', 'Women\'s'),
        ('C', 'Coed'),
    )
    sport = models.ForeignKey('Sport')
    school = models.ForeignKey('School')
    gender = models.CharField(max_length=1, choices=GENDERS)

    def __unicode__(self):
        return U'%s - %s' % (self.school.name, self.sport.name)