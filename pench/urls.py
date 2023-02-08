from django.urls import path
from . import views

urlpatterns = [
	path('', views.viewLogin, name='login'),
	path('home/', views.viewHome, name='home'),
	path('folder/<int:location>', views.viewFolder, name='folder'),

	path('logout/', views.exit, name='exit'),

	path('createFolder/<int:location>', views.createFolder, name='createFolder'),
	path('deleteFolder/<int:pk>', views.deleteFolder, name='deleteFolder'),

	path('uploadFile/<int:location>', views.uploadFile, name='uploadFiles'),
	path('deleteFile/<int:pk>', views.deleteFile, name='deleteFile'),
	path('downloadFile/<int:pk>', views.downloadFile, name='downloadFile')
]