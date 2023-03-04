from django.urls import path
from app_blog import views

#from django.conf.urls import url Django v3

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]


#urlpatterns = [
#    path(r'^$', views.home)#, name='home')
#    path(r'^about/$', views.about, name='about'),
#    path(r'^about/company/$', views.about_company, 
#        name='about_company'),  
#]