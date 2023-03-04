from django.urls import path
from app_blog import views

#from django.conf.urls import url Django v3
from .views import (HomePageView, ArticleDetail,  
                    ArticleList, ArticleCategoryList)

#urlpatterns = [
#    path(r'', views.HomePageView.as_view()),
#]


#urlpatterns = [
#    path(r'^$', views.home)#, name='home')
#    path(r'^about/$', views.about, name='about'),
#    path(r'^about/company/$', views.about_company, 
#        name='about_company'),  
#


urlpatterns = [
    path(r'', HomePageView.as_view()),
    path(r'articles', ArticleList.as_view(), 
         name='articles-list'),
    path(r'articles/category/<slug>',
         ArticleCategoryList.as_view(),
         name='articles-category-list'),
    path(r'articles/<year>/<month>/<day>/<slug>',
         ArticleDetail.as_view(),
         name='news-detail'),
]