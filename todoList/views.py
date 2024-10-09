from django.shortcuts import render, redirect, HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):

    todoItems = Todo.objects.all()

    context = {
        'todoItems': todoItems,
    }

    return render(request, 'todoList/home.html', context)


def createPost(request):

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()

    context = {
        'form': form,
        'title': 'Add',
    }

    return render(request, 'todoList/createPost.html', context)

def update(request, id):
    post = Todo.objects.get(id=id)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=post)
    
    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'todoList/update.html', context)

def delete(request, id):

    if request.method == 'POST':
        post = Todo.objects.get(id=id)
        post.delete()
        return redirect('home')
    

    return HttpResponse('<h1>Not Allowed</h1>')