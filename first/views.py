from django.views.generic.list import ListView
from tokenize import Name
from django.shortcuts import render, redirect
from django.template import context
from first.forms import TodoForm

from first.models import Todos


class TodoList(ListView):
    template_name = 'first/todo_detail.html'
    queryset = Todos.objects.all()
    context_object_name = 'todo'
    
    

#def todo_list(request):
   # todo = Todos.objects.all()
   # context = {
   #     'todo':todo
   # }
   # return render(request, 'first/todo_detail.html', context)

def todo_detail(request, id):
    todos = Todos.objects.get(id=id)
    context = {
        "todos":todos
    }
    return render(request, 'first/todo_details.html', context)



def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        'form':form
    }    
    return render(request, 'first/todo_create.html', context)



def todo_update(request, id):
    todo = Todos.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        'form': form
    }    
    return render(request, 'first/todo_update.html', context)    




def todo_delete(request, id):
     todo = Todos.objects.get(id=id)
     todo.delete()
     return redirect("/")
    