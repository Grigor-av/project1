from django.shortcuts import render

# View for the homepage (index)
def index(request):
    # You can pass context data to the template if needed
    return render(request, 'index.html')

# View for the cart page
def cart_view(request):
    # You can pass cart data or other context if needed
    return render(request, 'cart.html')
