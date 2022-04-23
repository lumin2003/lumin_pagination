from django.shortcuts import render
from django.shortcuts import redirect
from hello import models
from .models import PatientInfo
import csv
import io
from django_tables2 import SingleTableView, RequestConfig
from .tables import PatientInfoTable
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
    return redirect('/PatientInfo_upload/', context)
# Create your views here.




def gene(request):
    data = {}
    listdata = PatientInfo.objects.all()
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



class PatientInfoListView(SingleTableView):
    model = PatientInfo
    template_name = 'gene_pagination.html'
    table_class = PatientInfoTable

def PatientInfo_upload(request):
    PatientInfos = PatientInfo.objects.all()  # fetching all post objects from database
    p = Paginator(PatientInfos, 45)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'PatientInfo_upload.html', context)

