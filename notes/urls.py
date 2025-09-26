
from django.urls import path
from . import views




urlpatterns = [
   
    path('',views.check,name="check"),
    path('display/',views.display_items,name='display'),
    path('add_note/',views.Add_view,name='add_note'),
    path('view/<int:pk>/',views.view_page,name='view_page'),
    path('edit/<int:pk>/',views.edit_view,name='edit_page'),
    path('delete/<int:pk>/',views.delete_view,name='delete_page')
    

]
