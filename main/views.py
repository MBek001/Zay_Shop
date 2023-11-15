import json
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import *
from django.http.response import JsonResponse

User = get_user_model()


# Create your views here.

class Homeview(View):
    template = "index.html"
    context = {}

    def get(self,request):
        pro = Products.objects.all()
        pro_data = []

        for prod in pro:
            image = Img.objects.filter(product=prod).first()
            prod.image = image
            pro_data.append(prod)
        self.context.update({"product_data":pro_data})
        return render(request,self.template,self.context)

    def post(self,request):
        product_id = request.POST.get('product_id')
        if request.user is None:
            return redirect("/accounts/login")
        user = request.user.id

        if not ShoppingCart.objects.filter(Q(user_id=user)& Q(product_id=product_id)).exists():
            shoppping_cart = ShoppingCart.objects.create(
                product_id=product_id,
                user_id=user
            )
            shoppping_cart.save()
            return redirect(f'/#product_{product_id}')
        return redirect(f'/#product_{product_id}')



def about(request):
    return render(request, 'about.html')

def shop (request):
    return render(request, 'shop.html')

def contact (request):
    return render(request, 'contact.html')

def shop_single(request):
    return render(request, 'shop-single.html')

def register(request):
    return render(request, 'regst.html')

def fr_password(request):
    return render(request, 'forgot_pasword.html')

def shoppingcart(request):
    return render(request, 'shopping_cart.html')

def admin_site(request):
    return render(request, 'admin.html')

class ShoppingCartView(View):
    template = 'shopping_cart.html'
    content = {}

    def get(self, request):
        if request.user.id is None:
            return redirect('/accounts/login')
        shopping_cart = ShoppingCart.objects.filter(user=request.user)
        data = []
        for index, value in enumerate(shopping_cart):
            image =Img.objects.filter(product=value.product).first()
            value.image = image
            value.index = index + 1
            data.append(value)
        self.content.update({'shopping_cart_products': data})
        return render(request, self.template, self.content)

    def post(self, request):
        shopping_cart_id = request.POST.get("shopping_cart_id")
        ShoppingCart.objects.get(pk=shopping_cart_id).delete()
        return redirect('/shopping_cart')


class AddproductView(View):
    template = "add-product.html"
    content = {}

    def get(self,request):
        return render(request,self.template, self.content)

    def post(self,request):
        name = request.POST.get('title')
        decription = request.POST.get('description')
        price = request.POST.get('price')
        images = request.FILES.getlist('images')

        product = Products.objects.create(
            title=name,
            description=decription,
            price=price,
        )
        product.save()

        for image in images:
            image = Img.objects.create(
                image=image,
                product=product
            )
            image.save()

        return redirect('/add-product')

class IncrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            shopping_cart.count +=1
            shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class DecrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if shopping_cart.count > 0:
                shopping_cart.count -= 1
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class ChangeCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            product_count = json_data.get('product_count')

            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if product_count is not None:
                shopping_cart.count = product_count
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})



