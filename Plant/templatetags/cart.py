from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
	keys = cart.keys()
	for productid in keys:
		if int(productid) == product.id:
			return True;
	return False


@register.filter(name='cart_count')
def cart_count(product,cart):
	keys = cart.keys()
	for productid in keys:
		print(productid, product.id)
		if int(productid) == product.id:
			return cart.get(productid);
	return 0;

