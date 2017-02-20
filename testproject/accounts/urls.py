from django.conf.urls import url,include
#from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.GetData),
    #url(r'^$', views.UpdateData),
   # url(r'^admin/', admin.site.urls),
]
