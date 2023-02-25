
from django.contrib import admin
from django.urls import path


from kibru.views import(
    kibru_Admin_Site_View
)
app_name="kibru"
urlpatterns = [
    path("dashboard/", kibru_Admin_Site_View,name="dashboard"),
    
]
