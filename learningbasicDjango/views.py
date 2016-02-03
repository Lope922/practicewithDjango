from django.shortcuts import render

# Create your views here. # these will be referened from templates.

# this is a function based view. When it is called it will return the template referecening it. in this only case
# it's start
def post_list(request):
#takes requests and return a function render that will render/put together our template blog/post_list.html
    return render(request, 'start.html', {})
