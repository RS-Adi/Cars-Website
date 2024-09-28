from django.shortcuts import redirect, render
from django.views import View

from .forms import ProductForm
from .models import Thing

class Home(View):
    # We make a GET request to a specific URL that maps to the Home view.
    def get(self, request):
        # The get method is called to handle the request.
        # The Thing.objects.all() query retrieves all objects from the Thing model.
        things = Thing.objects.all()

        # The render function generates an HTTP response, rendering the 'home.html' template 
        # and passing the things queryset to the template for display.
        # The things queryset will be accessible in the template as {{ things }},
        # allowing us to display the Thing objects.
        return render(request, 'home.html', {'things': things})  # {'key': value} key-value pairs passed to the template

class Item(View):

    def get(self, request, name):
        thing = Thing.objects.get(name=name)
        return render(request, 'item.html', {'thing': thing})


class NewProduct(View):

    def get(self, request):
        form = ProductForm()
        return render(request, 'new_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return render(request, 'new_product.html', {'form': form})


class Success(View):

    def get(self, request):
        return render(request, 'success.html')
