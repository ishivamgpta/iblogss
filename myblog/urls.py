from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
# from myblog import views 
from .views import post,home,category,about


urlpatterns = [
    path('home/', home,name='home'),
    path('blog/<slug:url>',post,name='post'),
    path('category/<slug:url>',category,name='category'),
    path('about/',about,name='about')
    #path('tinymce/', include('tinymce.urls'))
]