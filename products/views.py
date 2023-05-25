from django.shortcuts import render
from django.http import HttpResponse

def check_product(request):
	status = 'online'
	return render(request, 'check_product.html', {'status':status})

def insert_product(request):
	return HttpResponse('Nice!')
