from django.db import models
from Web_Login.models import User
import random
import os


# Create your models here.

class category(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'

class slider(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='slider/', blank=False)
    
    def __str__(self):
        return self.title

class Item(models.Model):
    
    name = models.CharField(max_length=264)
    category = models.ForeignKey(category, related_name='category', on_delete=models.CASCADE)
    description = models.TextField(max_length=200, verbose_name='Description')
    rented = models.BooleanField(default=False)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    districtChoices = (('Atlantic Wharf','Atlantic Wharf'),
('Birchgrove', 'Birchgrove'),
('Butetown', 'Butetown'),
('Cardiff Bay','Cardiff Bay'),
('Cardiff city centre','Cardiff city centre'),
('Cardiff Gate','Cardiff Gate'),
('Castle Quarter', 'Castle Quarter'),
('Cathays Park', 'Cathays Park'),
('Cefn Mably', 'Cefn Mably'),
('Coryton, Cardiff', 'Coryton, Cardiff'),
('Culverhouse Cross', 'Culverhouse Cross'),
('Cyncoed', 'Cyncoed'),
('Danescourt', 'Danescourt'),
('Ely, Cardiff', 'Ely, Cardiff'),
('Gabalfa', 'Gabalfa'),
('The Hayes', 'The Hayes'),
('Cardiff International Sports Village', 'Cardiff International Sports Village'),
('Leckwith, Cardiff', 'Leckwith, Cardiff'),
('Llandaff', 'Llandaff'),
('Maindy', 'Maindy'),
('Mermaid Quay', 'Mermaid Quay'),
('Morganstown', 'Morganstown'),
('Mynachdy', 'Mynachdy'),
('Pentrebane', 'Pentrebane'),
('Plasdwr', 'Plasdwr'),
('Pwll-coch', 'Pwll-coch'),
('Radyr', 'Radyr'),
('Rhiwbina', 'Rhiwbina'),
('Rhydlafar', 'Rhydlafar'),
('Roath', 'Roath'),
('St Mellons', 'St Mellons'),
('Tiger Bay', 'Tiger Bay'),
('Tremorfa', 'Tremorfa'))
    
    district = models.CharField(max_length=50, choices=districtChoices, default='Cardiff city centre')

    def imageFolder():
        same = True
        while same == True:
            imageFolder = random.randint(100000000, 999999999)
            if os.path.exists("media/item_img/" + str(imageFolder)):
                same = True
            else:
                same = False
        return str(imageFolder)
    
    a = imageFolder()
        
    image_1 = models.ImageField(upload_to='media/item_img/{}'.format(a), null=True, blank=True)
    image_2 = models.ImageField(upload_to='media/item_img/{}'.format(a), null=True, blank=True)
    image_3 = models.ImageField(upload_to='media/item_img/{}'.format(a), null=True, blank=True)
    image_4 = models.ImageField(upload_to='media/item_img/{}'.format(a), null=True, blank=True)
    image_5 = models.ImageField(upload_to='media/item_img/{}'.format(a), null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created'] # descending order