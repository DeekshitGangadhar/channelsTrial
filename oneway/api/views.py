from django.shortcuts import render

def room(request):
    print("rendered")
    return render(request, 'api/room.html')