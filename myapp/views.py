from django.shortcuts import render
from django.http import HttpResponse
from .models import person
import json

# Create your views here.

def index(request):
	P = person.objects.all()
	context = {"P":P}
	return render(request,'index.html',context)

def ajax(request):
	print(request.POST)
	if request.POST["type"] == "search":
		r = '<table class="table table-bordered table-hover"><thead><th>Name</th><th>Age</th></thead><tbody>'
		P = person.objects.all()

		page = request.POST["s_age"] 
		pname = request.POST["s_name"].lower()
		
		f1 = (pname == "")
		f2 = (page == "")

		for p in P:
			if f1 and f2:
				r = r + '<tr><td>{}</td><td>{}</td></tr>'.format(p.name,p.age)
			elif f1:
				if p.age == page:
					r = r + '<tr><td>{}</td><td>{}</td></tr>'.format(p.name,p.age)
			elif f2:
				if pname in p.name.lower():
					r = r + '<tr><td>{}</td><td>{}</td></tr>'.format(p.name,p.age)
			else:
				if pname in p.name.lower() and page == p.age:
					r = r + '<tr><td>{}</td><td>{}</td></tr>'.format(p.name,p.age)

		r = r + '</tbody></table>'
		resp = {"t": r}
		return HttpResponse(json.dumps(resp),content_type='application/javascript')

	if request.POST["type"] == "add":
		page = request.POST['a_age']
		pname = request.POST['a_name']
		if(pname == "" or page == ""):
			P = person.objects.all()
			context = {"P":P}
			return render(request,'index.html',context)

		p = person(name=pname,age=int(page))
		p.save()

		r = '<table class="table table-bordered table-hover"><thead><th>Name</th><th>Age</th></thead><tbody>'
		P = person.objects.all()
		for p in P:
				r = r + '<tr><td>{}</td><td>{}</td></tr>'.format(p.name,p.age)
		r = r + '</tbody></table>'
		resp = {"t": r}
		return HttpResponse(json.dumps(resp),content_type='application/javascript')
