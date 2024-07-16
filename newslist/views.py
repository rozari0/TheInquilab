from django.shortcuts import render


# Create your views here.
def testrender(request):
    return render(request, template_name="base.html")
