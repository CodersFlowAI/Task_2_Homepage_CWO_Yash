from django.shortcuts import render

from homepage.forms import NewsletterForm

# Create your views here.
def homepage(request):
    form = NewsletterForm()
    
    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'homepage/home.html')
        else:
            print('FORM INVALID')
    
    return render(request,'homepage/home.html',{'form':form})

