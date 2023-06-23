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


# This function can be triggered by clicking the edit or update button
# It has two main goals: 
## 1. Get the todo from the database by id > inserts that data into the form fields. 
## 2. Grabs all the new input filed data > updates the todo in the database > returns to the home page
def todo_update(request, pk):
    
    # get the todo from the database
    # The get() method returns a single with the same id as the primary key (pk) value.
    # The pk is the primary key of the todo, that is, the id of the todo
    # So 'pk' = 'id' of the todo in the database
    
    todo = Todo.objects.get(pk=pk)
    # To fill the form with the data from the database, we need to pass the todo object to the form
    
    # if the request method is POST, then update the todo in the database with the new data
    if request.method == 'POST':
        
        # 'instance=todo' means populate the data from the database into the form
        # 'instance'refers to the object that the form is editing
        # The 'todo' object contains the data from the database
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save() # save the form to the database/ UPDATE
            
               # After updating the todo, redirect to the home page
            return redirect('todo_list')
        
        # else, redirect to todo_update.html to render the form into the template
    else:
        form = TodoForm(instance=todo)
     
     #When the edit button is clicked, the todo_update.html template is rendered with the form
    return render(request, 'todo_app/todo_update.html', {'form': form})



# When the delete button is clicked, redirect to the todo_delete.html template
def todo_delete(request, pk):
    
    todo = Todo.objects.get(pk=pk) # get the todo from the database by id
    
    if request.method == 'POST':
        todo.delete() 
        
        return redirect('todo_list')
    
    return render(request, 'todo_app/todo_delete.html', {'todo': todo})
