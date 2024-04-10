from django.shortcuts import HttpResponse


def index(request):
    name = request.GET.get('name', 'Recruto')
    message = request.GET.get('message', 'Давай дружить')
    return HttpResponse(f'<h1>Hello {name}! {message}!</h1>')
