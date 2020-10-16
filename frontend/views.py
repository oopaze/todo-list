from django.shortcuts import render

def todo_list(request):
    uri = request.get_raw_uri().split('?')[0]
    return render(request, 'frontend/list.html', {'uri':uri})