
from django.urls import path
from . import views




urlpatterns = [
   
    path('',views.check,name="check"),
    path('display/',views.display_items,name='display'),
    path('add_note/',views.Add_view,name='add_note')
    
]
