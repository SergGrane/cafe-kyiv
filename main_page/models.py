from django.db import models
from uuid import uuid4
from os import path
from PIL import Image
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=40,unique=True,db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position',)

class Dish(models.Model):


    def get_file_name(self,filename):
        ext = filename.strip().split('.',)[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes',filename)


    name = models.CharField(max_length=40,unique=True,db_index=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    ingredients = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField(max_length=500,blank=True)
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.desc}'


class Why(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)
    desc = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}: {self.desc}'

    class Meta:
        ordering = ('position',)

class Events(models.Model):

    def get_file_name(self,filename):
        ext = filename.strip().split('.',)[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes',filename)

    name = models.CharField(max_length=40, unique=True, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    head = models.TextField(max_length=500, blank=True)
    row1 = models.TextField(max_length=500, blank=True)
    row2 = models.TextField(max_length=500, blank=True)
    row3 = models.TextField(max_length=500, blank=True)
    bottom = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to= get_file_name, blank=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    def save(self):
        super().save()
        img = Image.open(self.photo.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):
        return f'{self.name}: {self.price}'

    class Meta:
        ordering = ('position',)

class About(models.Model):

    name = models.CharField(max_length=100, unique=True, db_index=True)
    head1 = models.TextField(max_length=300, blank=True)
    head2 = models.TextField(max_length=300, blank=True)
    head3 = models.TextField(max_length=300, blank=True)
    row1 = models.TextField(max_length=300, blank=True)
    row2 = models.TextField(max_length=300, blank=True)
    row3 = models.TextField(max_length=300, blank=True)
    bottom = models.TextField(max_length=300, blank=True)
    about_video = models.URLField(max_length=300, blank=True)
    is_visible = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name}: {self.head1}'


class Chefs(models.Model):

    def get_file_name(self,filename):
        ext = filename.strip().split('.',)[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/chefs',filename)

    name = models.CharField(max_length=40, unique=True, db_index=True)
    speciality = models.TextField(max_length=40, blank=True)
    photo = models.ImageField(upload_to= get_file_name, blank=True)
    twit = models.URLField(max_length=800,blank=True)
    faceb = models.URLField(max_length=800, blank=True)
    insta = models.URLField(max_length=800,blank=True)
    linked = models.URLField(max_length=800,blank=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}: {self.speciality}'


    def save(self):
        super().save()
        img = Image.open(self.photo.path)

        if img.height > 500 or img.width > 400 or img.height < 500 or img.width < 400:
            output_size = (500, 400)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    class Meta:
        ordering = ('position',)

class Gallery(models.Model):

    def get_file_name(self,filename):
        ext = filename.strip().split('.',)[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/gallery',filename)


    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)
    photo = models.ImageField(upload_to=get_file_name, blank=True)

    def __str__(self):
        return f'{self.position}'

    def __eq__(self, other):
        if isinstance(other, Gallery):
            return self.id == other.id
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Gallery):
            return self.id != other.id
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Gallery):
            return self.id > other.id
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Gallery):
            return self.id < other.id
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Gallery):
            return self.id >= other.id
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Gallery):
            return self.id <= other.id
        return NotImplemented

    def save(self):
        super().save()
        img = Image.open(self.photo.path)

        if img.height > 500 or img.width > 400:
            output_size = (500, 400)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    class Meta:
        ordering = ('position',)


class Contactus(models.Model):


    map = models.URLField(max_length=800, blank=True)
    street = models.TextField(max_length=100, blank=True)
    city = models.TextField(max_length=100, blank=True)
    opendays = models.TextField(max_length=100, blank=True)
    openhours = models.TextField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.position}: {self.street} {self.city}'


class Contmail(models.Model):
    mail = models.EmailField()
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.mail}: {self.position}'

    class Meta:
        ordering = ('position',)

class Contphone(models.Model):
    phone = models.TextField(max_length=20, blank=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.phone}: {self.position}'

    class Meta:
        ordering = ('position',)

class TestoMonial(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    mail = models.EmailField()
    subj = models.CharField(max_length=50)
    message = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.name} {self.mail} {self.subj} {self.message[:60]}'

class UserReservation(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')

    name=models.CharField(max_length=50,unique=True,db_index=True)
    phone = models.CharField(max_length=15,validators=[mobile_regex])
    persons = models.PositiveIntegerField()
    message = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_processed =models.BooleanField(default=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.name} {self.phone} {self.message[:30]}'

class Slides(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    rows = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} {self.rows[:30]}'

class BestTest(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    profession = models.CharField(max_length=50)
    message = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} {self.profession} {self.message[:30]}'

