from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.

def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST.get("item_text", ""))
        return redirect("/")
    
    
    return render(request, 
                  "home.html", 
                  {"new_item_text": request.POST.get("item_text", "")},)
