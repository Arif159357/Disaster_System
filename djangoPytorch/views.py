from django.http import HttpResponse
from django.shortcuts import render
from djangoPytorch.model import main
from rest_framework.response import Response
from rest_framework.decorators import api_view
from djangoPytorch.scrapping import scrap

# @api_view(['GET'])

def get_url(request):
    return render(request, "url.html")


def show_model(request):
    print("request",request.GET.get('search_url'))
    scrap()
    pred, url = main()
    mylist = zip(pred, url)
    content = {"Image": mylist}

    # return Response({'Predicted as disaster': url })
    return render(request, "home.html", content)
 