from django.shortcuts import render, HttpResponse

TAX_RATE = 15

def default(request):
    return HttpResponse("THIS IS A SITE TO CALCULATE TAX")


def calculate(request, num):
    return HttpResponse(
        f" The total is : {((TAX_RATE/100)*num)+num} "
    )


def tax_rate(request):
    return HttpResponse(
        f" <h1>Tax Rate: {TAX_RATE}%</h1> "
    )