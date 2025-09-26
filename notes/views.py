from django.shortcuts import render,redirect,get_object_or_404
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
    


def view_page(request,pk):
    note=get_object_or_404(Note,pk=pk)
    return render(request,'view.html',{'note':note})



def edit_view(request,pk):
    st=get_object_or_404(Note,pk=pk)
    if request.method=='POST':
        form=AddNote(request.POST,instance=st)

        if form.is_valid():
            form.save()
            return redirect('display')
        
        return render(request,'edit.html',{'form':form})

    form=AddNote(instance=st)
    return render(request,'edit.html',{'form':form})



def delete_view(request,pk):
    note=get_object_or_404(Note,pk=pk)

    if request. method=='POST':
        note.delete()
        return redirect('display')
    

    return render(request,'delete.html',{'note':note})











