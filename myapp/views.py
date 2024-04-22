from django.shortcuts import render

# Create your views here.
def your_view(request):
    user = request.user  # Assuming user is passed to the template
    return render(request, 'home', {'user': user})