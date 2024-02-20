from django.contrib import admin
from django.urls import path, include
from addressbook import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('addressbook.urls')),
    path('sites/', views.site_list, name='site_list'), 
    path('add-site/', views.add_site, name='add_site'),  
    path('export-passwords/', views.export_passwords_csv, name='export_passwords_csv'),
    path('login/', views.user_login, name='login'),
]
