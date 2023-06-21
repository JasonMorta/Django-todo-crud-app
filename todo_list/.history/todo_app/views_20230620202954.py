from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    print('todo_list')
    todos = Todo.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})


def todo_create(request):
    print('todo_create')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            print('redirect(todo_list)')
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_app/todo_create.html', {'form': form})


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
