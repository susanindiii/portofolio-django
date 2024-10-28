from django.shortcuts import render


def biodata_view(request):
    return render(request, 'biodata.html')

