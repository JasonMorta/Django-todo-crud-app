from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    print('todo_list')
    todos = Todo.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})


def todo_create(request):
    
    if request.method == 'POST':
        
        form = TodoForm(request.POST) 
        # create a form instance and populate it with data from the request. 
        # The form would then look like this: <TodoForm bound=True, valid=False, fields=(title;description)>
        if form.is_valid(): # check if the form is valid (correct data types, etc.)
            form.save()
   
            return redirect('todo_list') # save the form and redirect to todo_list.html
    else:
        form = TodoForm()
        print('render(request,"todo_app/todo_create.html"')
    return render(request, 'todo_app/todo_create.html', {'form': form}) # navigate to todo_create.html


def todo_update(request, pk):
    print('todo_update')
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_app/todo_update.html', {'form': form})


def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_delete.html', {'todo': todo})
