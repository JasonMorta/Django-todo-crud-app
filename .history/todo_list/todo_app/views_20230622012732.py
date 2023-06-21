from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Get the todo list from the database and render it to todo_list.html
# This function is called when the user navigates to the home page
def todo_list(request):
    # request = <WSGIRequest: GET '/'>
    # the request parameter contains the type of request (GET, POST, etc.)

    todos = Todo.objects.all() # get all the todos from the database
    # The all() method is used to retrieve all the objects of the specified model from the database.
    
    #The third argument is a dictionary that contains the data that will be rendered to the template.
    return render(request, 'todo_app/todo_list.html', {'todos': todos})


def todo_create(request):
    # request = <WSGIRequest: POST '/create/'>
    print(request.POST.get('title')) # get the title from the request
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
    print(pk)
    
    # get the todo from the database
    # The get() method returns a single object, or raises an exception if no matching object is found.
    # The pk is the primary key of the todo, that is, the id of the todo
    # So 'pk=pk' means get the todo with the id of pk
    # Also retrieves a single instance of the Todo model from the database based on a specific primary key (pk) value.
    todo = Todo.objects.get(pk=pk)
    
    if request.method == 'POST':
        
        # 'instance=todo' means populate the form with the data from the todo
        # 'instance'refers to the object that the form is editing
        # The 'todo' object contains the data from the database
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
