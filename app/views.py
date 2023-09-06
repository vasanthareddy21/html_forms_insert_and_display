from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if(request.method=='POST'):
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        
        TO=Topic.objects.get(Topic_name=tn)

        WO=Webpage.objects.get_or_create(Topic_name=TO,name=na,url=ur)[0]
        WO.save()
        QSWO=Webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if(request.method=='POST'):
        na=request.POST['na']
        da=request.POST['da']
        au=request.POST['au']
        em=request.POST['em']

        WO=Webpage.objects.get(pk=na)

        AO=AccessRecords.objects.get_or_create(name=WO,date=da,author=au,email=em)[0]
        AO.save()

        QARO=AccessRecords.objects.all()
        d1={'QARO':QARO}
        return render(request,'display_accessrecords.html',d1)

    return render(request,'insert_accessrecords.html',d)

def select_and_display(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tnlist=request.POST.getlist('tn')
        print(tnlist)
        QSWO=Webpage.objects.none()
        for tn in tnlist:
            QSWO=QSWO|Webpage.objects.filter(Topic_name=tn)
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)


    return render(request,'select_and_display.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)

def radiobuttons(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'radiobuttons.html',d)



    