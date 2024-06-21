from django.shortcuts import render
from django.http import HttpResponse
from . models import Art, ArtCategory

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError



# Create your views here.
def home(request):
    arts = Art.objects.all()
    context = {
        'arts': arts,
    }
    return render(request, 'index.html', context)


def art_details(request, slug):
    try: 
        art = get_object_or_404(Art, slug=slug)
        context = {
            'art': art,
        }
        return render(request, 'product-details.html', context)
    
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error in product_detail view: {e}")
        # Return a server error response
        return HttpResponseServerError("Sorry, something went wrong. Please try again later.")
    
    

def shop(request):
    arts = Art.objects.all()
    context = {
        'arts': arts,
    }
    return render(request, 'shop.html', context)    


def favorite(request):
    context = {
        
    }
    return render(request, 'favorites.html', context)




def cartpage(request):
    return render(request, 'cart.html')

def checkoutpage(request):
    return render(request, 'checkout.html')

def product_details(request):
    return render(request, 'product-details.html')
    
    