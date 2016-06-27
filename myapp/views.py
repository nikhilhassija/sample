from django.shortcuts import render
from django.http import HttpResponse
from .models import person
import json

# Create your views here.

def index(request):
	return render(request,'index.html')

def ajax(request):
	print("here")
	if request.method == "POST":
		print("there")
		print(request.POST[s_name])
		print(request.POST[s_age])
		r = '<table class="table table-bordered table-hover"><thead><th>Name</th><th>Age</th></thead><tbody>'
		P = person.objects.all()
		for p in P:
			r = r + '<tr><td>{}</td><td>{}</td></tr>'.format(p.name,p.age)
		r = r + '</tbody></table>'
		resp = {"t": r}
		return HttpResponse(json.dumps(resp),content_type='application/javascript')