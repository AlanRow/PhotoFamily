from django.db import models


"""Sex of person"""
SEX = [
    ("m", "Man"),
    ("w", "Woman")
]


"""Model of cousin. Contains information about name, sex, age, and biography"""
class Person(models.Model):
    """Name parameters"""
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronimyc = models.CharField(max_length=50, null=True)

    """Sex parameter"""
    sex = models.CharField(max_length=1, choices=SEX)

    #"""Parents"""
    #parents = models.ForeignKey('Parents', on_delete=models.SET_NULL, null=True)
    #father = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    #mother = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    """Life dates"""
    birth = models.DateField(null=True)
    #death = models.ForeignKey('Death', on_delete=models.SET_NULL, null=True)

    """Biography details"""
    birthplace = models.CharField(max_length=100, null=True)
    spec = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)


"""Marks dead person"""
class Death(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    date = models.DateField(null=True)


"""Marks man-sex person"""
class Man(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)


"""Marks woman-sex person"""
class Woman(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)


"""Contains informaition about person mother and father"""
class Parents(models.Model):
    child = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    father = models.ForeignKey(Man, on_delete=models.SET_NULL, null=True)
    mother = models.ForeignKey(Woman, on_delete=models.SET_NULL, null=True)


"""Information about pairs^ wife, handsom number and date of marriage"""
class Marriage(models.Model):
    wife = models.ForeignKey(Woman, on_delete=models.CASCADE)
    handsom = models.ForeignKey(Man, on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateField(null=True)
    #divorce = models.OneToOneField(Divorce, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = [['wife', 'handsom', 'number']]


"""Marks divorced pairs"""
class Divorce(models.Model):
    marriage = models.OneToOneField(Marriage, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)


"""Contains infornation about photo: image, name, place, date and description"""
class Photo(models.Model):
    image = models.ImageField(upload_to='photos', max_length=100, unique=True)
    
    name = models.CharField(max_length=50, null=True)
    place = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    description = models.TextField(null=True)


"""Name of tag"""
class Tag(models.Model):
    name = models.CharField(max_length=25, primary_key=True)


"""Tag on photos"""
class Tagged(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
