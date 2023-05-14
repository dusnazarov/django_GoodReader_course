from django.shortcuts import render


def landing_page(request):    
    # print(request.COOKIES['sessionid'])
    # print(request.COOKIES)
    # print(request.CustomUser.is_authenticated)
    # print(request.CustomUser.CustomUsername)
    
    return render(request,'landing.html')

