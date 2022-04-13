from django.shortcuts import render
from django.shortcuts import redirect
from hello import models
from .models import PatientInfo
import csv
import io
from django.core.paginator import Paginator


def gene_upload(request):
    if request.method == 'POST':
        new_PatientInfo = request.FILES['myfile']
        print("i am here6")
    tem2 = new_PatientInfo.read().decode('utf-8')
    print("i am here")
    io_string = io.StringIO(tem2)
    print("io_string", io_string)
    next(io_string) #removal header
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = PatientInfo.objects.update_or_create(
            classify=column[0],
            age =column[1],
            phenotype=column[2],
            numbers=column[3],
            size=column[4],
            location=column[5],
            migration = column[6],
        )
        context = dict()
    print("context", context)
    return redirect('/gene/', context)
# Create your views here.

def gene(request):

    data = {}
    listdata = PatientInfo.objects.all()
    #paginator = Paginator(listdata, 50)
    data['gene'] = listdata
    return render(request, 'gene.html',data)

def insert(request):
    if request.method == 'GET':
       return render(request, 'register.html')
    elif request.method == "POST":
        classify = request.POST.get("classify", None) # change from get("username") to get("name")
        age = request.POST.get("age", None)
        phenotype = request.POST.get("phenotype", None)
        numbers = request.POST.get("numbers", None)
        size = request.POST.get("size", None)
        location = request.POST.get("location", None)
        migration = request.POST.get("migration", None)
        tem=PatientInfo.objects.create(classify=classify, age=age, phenotype=phenotype,  numbers=numbers,
                                       size=size, location=location,migration=migration) #change model.UserInfo to UserInfo
        return redirect('/gene/')

def delete_gene(request):
    delete_id = request.GET.get('id')
    # 从数据库删除的
    models.PatientInfo.objects.filter(id=delete_id).delete()
    return redirect('/gene/')
    #return render(request, 'index.html', {'UserInfo': UserInfo})