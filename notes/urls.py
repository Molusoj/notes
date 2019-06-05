from django.urls import path, include
from . import views

app_name = 'notes'
urlpatterns = [
    # path('create/', views.note_create, name='create'),
    # path('', views.HomePageView.as_view(), name='home'),
    # path('detail/<note_id>/', views.detail, name='detail'),

    path('detail/<pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('create/', views.NoteCreateview.as_view(), name='create'),

]
