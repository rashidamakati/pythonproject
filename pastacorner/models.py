from django.db import models

# Create your models here.

# Create class for Menus
class Menu(models.Model):
    name = models.CharField(max_length = 140)
    desc = models.TextField()
    menu_type = models.CharField(max_length = 50)

    def __str__(self):
        #return{'name':self.name,'desc':self.desc,'menu_type':self.menu_type}
        #return "name:{}, desc:{}, menu_type:{}" .format(self.name, self.desc, self.menu_type)
        return self.name



class Contact(models.Model):
    username = models.CharField(max_length = 140)
    email = models.EmailField(max_length = 100)
    message = models.TextField()

    def __str__(self):
        return self.username
