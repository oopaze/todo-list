from django.shortcuts import render
import ipdb

def todo_list(request):
    import ipdb; ipdb.set_trace()
    uri = request.get_raw_uri().split('?')[0]
    return render(request, 'frontend/list.html', {'uri':uri})