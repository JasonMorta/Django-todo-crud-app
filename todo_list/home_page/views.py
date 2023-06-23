from django.shortcuts import render, redirect

def home_route(request):
    print("printed", request)
    # return render(request, 'homepage/home.html')
    #return render(request, 'todo_app/todo_list.html', {'todos': todos})
