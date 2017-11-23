from django.conf.urls import url
from . import views

# Defining urls for different pages of html
#app_name = 'pastacorner'
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^about/$',views.about, name='about'),
url(r'^menu/$',views.menu, name='menu'),
url(r'^gallary/$',views.gallary, name='gallary'),
url(r'^contact/$',views.contact, name='contact'),

]
