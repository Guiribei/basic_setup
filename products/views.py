from django.shortcuts import render
from django.http import HttpResponse
from .models import Suggestion

def check_product(request):
	if request.method == 'GET':
		status = 'online'
		return render(request, 'check_product.html', {'status':status})
	elif request.method == 'POST':
		text = request.POST.get('suggestion')
		suggestion = Suggestion(text=text)
		suggestion.save()
		return render(request, 'check_product.html')
def insert_product(request):
	return HttpResponse('Nice!')
