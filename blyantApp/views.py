from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    
    
    if request.is_mobile:
        banners = ["blyantApp/images/home/mobileBanners/bannerNew.jpg"]
        for i in range(1, 11): 
            banners.append(f"blyantApp/images/home/mobileBanners/banner{i}.jpg")
        template = 'home_mobile.html'

    else:
        banners = ["blyantApp/images/home/banners/banner.jpg"]
        for i in range(1, 11): 
            banners.append(f"blyantApp/images/home/banners/banner{i}.jpg")
        template = 'home.html'
    
    
    profileImages = []
    for i in range(1, 13): {
        profileImages.append(f"blyantApp/images/home/introImages/image{i}.jpg")
    }
           
    return render(request, template, {'banners': banners, 'images': profileImages})

def projekter(request):
    if request.is_mobile:
        template = "projekter_mobile.html"
    else:
        template = "projekter.html"
    return render(request, template)

def kontakt(request):
    return render(request, "kontakt.html")

def omOs(request):
    profileImages = []
    for i in range(1, 13): {
        profileImages.append(f"blyantApp/images/home/introImages/image{i}.jpg")
    }
        
    if request.is_mobile:
        template = "omOs_mobile.html"
    else:
        template = "omOs.html"
    return render(request, template, {'images':profileImages})

