from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

from banch import settings

import os

#OPERAÇÕES

#pastas

def createFolder (request, location):
	if request.user.is_authenticated == False:
		return redirect('/')

	folder = Folder()

	folder.name = request.POST['name']

	if location != 0:
		thisFolder = Folder.objects.get(pk=location)
		folder.location = thisFolder

		folder.save()
		return redirect('/folder/' + str(location))

	else:
		folder.save()
		return redirect('/home/')


def deleteFolder (request, pk):
	if request.user.is_authenticated == False:
		return redirect('/')

	folder = Folder.objects.get(pk=pk)

	try:
		returnLocate = '/folder/' + str(folder.location.id)
	except Exception as e:
		returnLocate = '/home/'


	folder.delete()

	return redirect(returnLocate)

def exit (request):
	logout(request)
	return redirect('/')

#arquivos

def uploadFile (request, location):
	if request.user.is_authenticated == False:
		return redirect('/')

	folderFile = Folder.objects.get(pk=location)

	_file = File()
	_file.file = request.FILES['file']
	_file.name = request.POST['name']
	_file.location = folderFile

	_file.save()

	return JsonResponse({'id':_file.id})

def deleteFile (request, pk):
	_file = File.objects.get(pk=pk)
	_file.delete()

	pass

def downloadFile (request, pk):
	_file = File.objects.get(pk=pk)

	file_path = os.path.join(settings.MEDIA_ROOT, _file.file.path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/octet-stream")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
			raise Http404

#VIEWS

def viewLogin (request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])

		if user is not None:
			login(request, user)
			return redirect('/home/')

		else:
			return render(request, 'login.html', {
				'msg': 'Usuário ou senha incorretos'
			})

	if request.user.is_authenticated:
		return redirect('/home/')

	else:
		return render(request, 'login.html')

def viewHome (request):
	if request.user.is_authenticated == False:
		return redirect('/')

	folders = Folder.objects.filter(location=None)

	return render(request, 'home.html', {
		'folders': folders,
	})

def viewFolder (request, location):
	if request.user.is_authenticated == False:
		return redirect('/')

	folders = Folder.objects.filter(location=location)
	files = File.objects.filter(location=location)
	thisFolder = Folder.objects.get(pk=location)

	return render(request, 'folder.html', {
		'this_folder': thisFolder,
		'folders': folders,
		'files': files
	})