from django.http import HttpResponse
from django.shortcuts import render
from djangoPytorch.model import main
from rest_framework.response import Response
from rest_framework.decorators import api_view
from djangoPytorch.scrapping import scrap
from django.views.decorators.csrf import csrf_exempt

 

# @api_view(['GET'])

def get_url(request):
    return render(request, "url.html")
    
@csrf_exempt
def got_url(request):
    if request.method == "GET":
        url = request.GET.get('data')
        scrap(url)
    return HttpResponse()

def show_model(request):
    pred, url = main()
    mylist = zip(pred, url)
    content = {"Image": mylist}

    # return Response({'Predicted as disaster': url })
    return render(request, "home.html", content)
 