from django.shortcuts import render,redirect
from .models import Note
from .forms import AddNote
# Create your views here.


def check(request):
    return render (request,'index.html')




def display_items(request):
    items=Note.objects.all()
    return render(request,'display.html',{'items':items})



def Add_view(request):
    if request.method=='POST':
        form=AddNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
        
        return render(request,'add_note.html',{'form':form})

    else:
        form=AddNote()
        return render(request,'add_note.html',{'form':form})




