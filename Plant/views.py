from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Plant, Orders
from django.views.generic import (
		ListView, 
		DetailView, 
		CreateView, 
		UpdateView, 
		DeleteView
		)

from django.contrib.auth.decorators import login_required
from .models import Plant
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def home(request):
	return render(request, 'Plant/home.html')


def PlantList(request):
	context = {
		'plants' : Plant.objects.all()
	}
	return render(request, 'Plant/plant_list.html', context)

@login_required
def myOrdersView(request):
	orders = []
	
	if request.method == 'GET':
		if request.user.is_manager:
			orders = Orders.objects.filter(seller=request.user.username, status=False)
		else:
			orders = Orders.objects.filter(buyer=request.user.username, status=False)

	elif request.method == 'POST':
		pass

	present = len([x.plant.name for x in orders])
	# print(f'orders are : {orders}')
	return render(request, 'Plant/myOrders.html', { 'orders' : orders , 'present': present })

class orderDetailView(LoginRequiredMixin, DetailView):
	model = Orders   # Plant/plant_detail.html

	def post(self, request, pk=None):
		print(f'post called {pk}')
		order = Orders.objects.filter(pk=pk).first()
		if order.seller == request.user.username:
			Orders.objects.filter(pk=pk).update(status=True)
		else:
			if not order.status:
				order.delete()
		return redirect('myorders')






@login_required
def cartView(request):
	plants = []
	presence = False
	if request.method == 'GET':
		kys = request.session.get('cart')
		if kys is not None and len(kys) > 0:
			print(f'key is not none : {kys}')
			presence = True
			plants = list(request.session.get('cart').keys())
		else:
			print('no items')

	if request.method == 'POST':
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		chkotsignal = request.POST.get('checkout')
		print('post called ')
		if chkotsignal:
			print('checkout signal')
			if cart:
				print('cart not empty')
				allplants = Plant.objects.all()
				cartKeys = list(cart.keys())
				for plant in allplants:
					if str(plant.id) in cartKeys:
						orderexist = Orders.objects.filter(plant=plant, seller=plant.manager.username, buyer=request.user.username,status=False).first()
						if orderexist:
							print('updating ==========================================')
							q = orderexist.quantity + cart[str(plant.id)]
							Orders.objects.filter(plant=plant, seller=plant.manager.username, buyer=request.user.username,status=False).update(quantity=q)
						else:
							order = Orders(plant=plant, seller=plant.manager.username, buyer=request.user.username, quantity=cart[str(plant.id)], status=False)
							order.save()
						cart.pop(str(plant.id))
						print(f' id  found {plant.id}')
				print(f'after removal: {cart}')
				request.session['cart'] = cart
		else:
			print('no checkout')
			if cart:
				quantity = cart.get(product)
				if quantity:
					if remove:
						if quantity <= 1:
							cart.pop(product)
						else:
							cart[product] = quantity - 1
					else:
						cart[product] = quantity + 1
				else:
					cart[product] = 1
			else:
				cart = {}
				cart[product] = 1
		print(cart)
		request.session['cart'] = cart
		return redirect('cart')

	context = {
		'plants': [x for x in Plant.objects.all() if str(x.id) in plants],
		'presence':presence
	}

	if len(context['plants']) == 0:
		presence = False;

	print(context)
	return render(request,'Plant/cart.html', context)


class plantListView(LoginRequiredMixin, ListView):
	model = Plant
	template_name = 'Plant/plant_list.html'
	context_object_name = 'plants'
	ordering = ['-date_posted']
	paginate_by = 2;

	def post(self, request):
		print('post called')
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity <= 1:
						cart.pop(product)
					else:
						cart[product] = quantity - 1
				else:
					cart[product] = quantity + 1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1
		print(cart)
		request.session['cart'] = cart
		return redirect('plant-list')


	def get(self, request):
		print('get called')
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		# print(cart)
		# if cart is not None:
		# 	request.session['cart'] = {}
		# 	print('cart created')
		return render(request,'Plant/plant_list.html' , { 'plants' : Plant.objects.all() })


# def register(request):
# 	if request.method == 'POST':
# 		form = UserRegisterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f'Account created for {username}')
# 			return redirect('login')
# 		# else:
# 		# 	messages.error(request, f'form invalid')
# 		# 	return redirect('plant-home')
# 	else:
# 		form = UserRegisterForm()
# 	return render(request, 'account/register.html', { 'form' : form })


class managerPlantListView(LoginRequiredMixin, ListView):
	model = Plant
	template_name = 'Plant/user_plants.html'
	context_object_name = 'plants'
	paginate_by = 2;

	def get_queryset(self):
		user = get_object_or_404(get_user_model(), username=self.kwargs.get("username"))
		return Plant.objects.filter(manager=user).order_by('-date_posted')



class plantDetailView(LoginRequiredMixin, DetailView):
	model = Plant   # Plant/plant_detail.html

class plantCreateView(LoginRequiredMixin, CreateView):
	model = Plant   # Plant/plant_form.html
	fields = ['name', 'price', 'q_avail', 'plant_image', 'description']

	def form_valid(self, form):
		form.instance.manager = self.request.user
		return super().form_valid(form)

class plantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Plant   # Plant/plant_form.html
	fields = ['name', 'price', 'q_avail', 'plant_image', 'description']

	def form_valid(self, form):
		form.instance.manager = self.request.user
		return super().form_valid(form)

	def test_func(self):
		plant = self.get_object()
		if self.request.user == plant.manager:
			return True
		return False

class plantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Plant   # Plant/plant_detail.html
	success_url = '/plants/'
	def test_func(self):
		plant = self.get_object()
		if self.request.user.username == plant.manager.username:
			return True
		return False


# from django.shortcuts import render
# from django.http import HttpResponse

# create new function which will handle traffic and will take request argument.

# def home(request):
# 	return HttpResponse('<h1> Blog Home </h1>')