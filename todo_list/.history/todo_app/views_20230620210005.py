from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Get the todo list from the database and render it to todo_list.html
# This function is called when the user navigates to the home page
def todo_list(request):
    print('request', request)

    todos = Todo.objects.all() # get all the todos from the database
    
    #The third argument is a dictionary that contains the data that will be rendered to the template.
    return render(request, 'todo_app/todo_list.html', {'todos': todos})


def todo_create(request):
    
    # if the request method is POST, then the form is being submitted and save to the database
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request.
        form = TodoForm(request.POST) 

        # The form would then look like this: <TodoForm bound=True, valid=False, fields=(title;description)>
        if form.is_valid(): # check if the form is valid (correct data types, etc.)
            form.save() # save the form to the database
   
            return redirect('todo_list') #redirect to todo_list.html / the home page
        
    # else, redirect to todo_create.html to render the form
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
