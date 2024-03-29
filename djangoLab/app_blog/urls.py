from django.urls import path
from app_blog import views

#from django.conf.urls import url Django v3
from app_blog.views import (HomePageView, ArticleDetail,  
                    ArticleList, ArticleCategoryList)
#from django.conf import settings
#from django.conf.urls.static import static


#urlpatterns = [
#    path(r'', views.HomePageView.as_view()),
#]


#urlpatterns = [
 #   path(r'^$', views.home)#, name='home')
  #  path(r'^about/$', views.about, name='about'),
   # path(r'^about/company/$', views.about_company, 
    #    name='about_company'),  

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticleList.as_view(), name='articles-list'),
    path('articles/category/<slug>/', ArticleCategoryList.as_view(), name='articles-category-list'),
    path('articles/<year>/<month>/<day>/<slug>/', ArticleDetail.as_view(), name='news-detail'),
]

#urlpatterns = [
#    path(r'', HomePageView.as_view()),
#    path(r'articles', ArticleList.as_view(), 
#         name='articles-list'),
#    path(r'articles/category/<slug>',
#         ArticleCategoryList.as_view(),
#         name='articles-category-list'),
#    path(r'articles/<year>/<month>/<day>/<slug>',
#         ArticleDetail.as_view(),
#         name='news-detail'),
#]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



