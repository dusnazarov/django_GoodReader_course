from django.shortcuts import render


def landing_page(request):    
    # print(request.COOKIES['sessionid'])
    # print(request.COOKIES)
    # print(request.user.is_authenticated)
    # print(request.user.username)
    
    return render(request,'landing.html')

