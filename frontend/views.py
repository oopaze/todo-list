from django.shortcuts import render

def todo_list(request):
    uri = request.get_raw_uri()
    return render(request, 'frontend/list.html', {'uri':uri})