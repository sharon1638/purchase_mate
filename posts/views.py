from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request, 'posts/shop.html')


def shop_detail(request):
    return render(request, 'posts/shop_detail.html')