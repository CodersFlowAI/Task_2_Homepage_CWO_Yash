from django.shortcuts import render
from cases.forms import ReportAnonymouslyForm,ReportForm
from homepage.forms import NewsletterForm
from cases.models import Report

# Create your views here.

def cases(request):
    form1 = ReportAnonymouslyForm()
    form = NewsletterForm()
    if request.method == "POST":
        form1 = ReportAnonymouslyForm(request.POST)
        form = NewsletterForm(request.POST)
        if form1.is_valid():
            
            form1.save(commit=True)
            return render(request,'homepage/home.html')

        elif form.is_valid():
            form.save(commit=True)
            return render(request,'homepage/home.html')
        else:
            print('FORM INVALID')
        
    
    return render(request,'cases/complaint.html',{'form1':form1,'form':form})




def report(request):
    form = NewsletterForm()
    form2= ReportForm()
    if request.method == 'POST':
        form2 = ReportForm(request.POST)
        form = NewsletterForm(request.POST)
        if form2.is_valid():
            # p = Report.objects.get(pk=10)
            # p.name = 'Rico'
            # p.save() 
            form2.save(commit=True)
            return render(request,'homepage/home.html')
        elif form.is_valid():
            form.save(commit=True)
            return render(request,'homepage/home.html')
        else:
            print('FORM INVALID')
        
        
    return render(request,'cases/report.html',{'form2':form2,'form':form})


