from django.shortcuts import render,redirect
from .models import Employee
from django.db.models import Q
from django.http import HttpResponse
def index(Request):
	if (Request.method=="POST"):
		search =Request.POST.get("search")
		data = Employee.objects.filter(Q(name__icontains=search)|Q(email__icontains=search)|Q(phone__icontains=search)|Q(salary__icontains=search)|Q(city__icontains=search)|Q(state__icontains=search))
	else:
		data = Employee.objects.all()
	return render(Request,'index.html',{'data':data})
def delete(Request,id):
	data = Employee.objects.get(id=id)
	if (data):
		data.delete()
	return redirect("/")
def add(request):
	if (request.method == "POST"):
		e = Employee()
		e.name=request.POST.get("name")
		e.email=request.POST.get("email")
		e.phone = request.POST.get("phone")
		e.salary = request.POST.get("salary")
		e.city = request.POST.get("city")
		e.state = request.POST.get("state")
		e.save()
		
	return render(request,"add.html")
def update(request,id):
	data = Employee.objects.get(id=id)
	if (request.method ==  "POST"):
		data.name=request.POST.get("name")
		data.email=request.POST.get("email")
		data.phone = request.POST.get("phone")
		data.salary = request.POST.get("salary")
		data.city = request.POST.get("city")
		data.state = request.POST.get("state")
		data.save()
	return render(request,"update.html",{'data':data})
def chk(request):
	return render(request,"chk.html")
# Create your views here.
