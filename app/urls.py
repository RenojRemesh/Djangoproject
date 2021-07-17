from django.urls import path, include
from  .import views
app_name = "app"
urlpatterns = [

path('',views.index,name='index'),
path('registration', views.registration,name='registration'),
path('login',views.login,name='login'),
path('userhome/<int:id>',views.userhome,name='userhome'),
path('update/<int:id>',views.edit_profile,name='update'),
path('destroy/<int:id>',views.Destroy,name='destroy'),
path('changepassword/<int:id>',views.change_password,name='changepassword'),
# path('gallery',views.AddGalleryDetails,name='gallery'),
path('registratione', views.registratione,name='registratione'),
path('gallery', views.printimages,name='gallery'),
 
]
