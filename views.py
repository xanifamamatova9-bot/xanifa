from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect

def qidirish_view(request):
    query = request.GET.get('q')

    if query:
        q = query.lower().replace(" ", "")
        if q == 'bubblesort':
            return redirect('bubble')
        elif q == 'selectionsort':
            return redirect('selection')

        # Agar boshqa matn yozilsa (oddiy qidiruv)
        # natijalar = Post.objects.filter(mavzu__icontains=query)
        # return render(request, 'qidirish.html', {
        #     'natijalar': natijalar,
        #     'query': query
        # })
    
def saralash(request):
     
     return render(request, "Saralash_algoritmlari.html")


def bubble_view(request):
    p = get_object_or_404(Post, id=2)
    return render(request, 'bubble.html', {'p': p})

def selection_view(request):
    p = get_object_or_404(Post,id=3)
    return render(request, 'selection.html', {'p': p})

def Index(request):
    p=Post.objects.all()
    return render(request,"base.html",{"p":p})

def salom_view(request):
    return HttpResponse("Xush kelibsiz!")

def xanifa_view(request):
    return HttpResponse("172-23 gurux talabasi Mamatova Xanifa")


