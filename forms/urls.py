from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('schedule', schedule, name='schedule'),
    path('gallery', gallery, name='gallery'),
    path('instruction', instruction, name='instruction'),
    path('team', team, name='team'),


    # path('blog', blog, name='blog'),
    # path('blog_details', blog_details, name='blog_details'),

]