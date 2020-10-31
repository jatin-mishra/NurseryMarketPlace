# Nursery Market Place:
	a portal where person can register and buy plants, seller can register and sell plants.

	secured links/ if links are important then i have used either mixins or decoratos to make them safe from unknown users.

tour:
	landing page:
		showing a automatic sliding page with 3 partitions.


		links for next:
			for logged out user:
				home: 
					itself
				contact: 	
					dead link
				register: 
					1. as user mode
					2. as manager mode
					[ but data will be stored in single model only ]
				login:
					implemented using custom user so it gives real web exp.
					login through email and password
				learn more:
					dead link

			for logged in:
				usermode will be in navbar:
					M- manager
					U- User

				you can also switch modes after visiting profile section 
				
				Links:
					home:
						in the name of market place
					plants:
						all plants available to buy
					profile:
						manager your profile
					checkout:
						if you bought something then click checkout and order request will get send.
					logout:
						to log user out.

					cart:
						check items added in your cart

	register:
		already having account functionality

		fields:
			username: must be unique
			email : 
			password :
			confirm password : 

		errors while registering will be shown in the window created in left.

	login:
		no account functionality

		fields:
			email
			password
		errors while registering will be shown in the window created in left.


	plants:
		you will be able to see all plants available
		add them into cart, or decrease from cart
		if cart items are zero:
			option : Add To cart
		else:
			+ : to add more quantity
			- : to decrease quantity
			and you will also be able to check number of quantities available 

		add them your quantity as much as possible.

		links:
			add to cart
			 	and once added you can increase or decrease quantities
			remove from cart

			check cart
			plantname:
				if you click plant name: take to to that plants detail page
			manager name:
				if you click managername:
					it will take you to page where all plants offered by him are available.
			you can also see image and price here.

	profile:
		link to user's all plant:
			if havn't posted any plant it will show you empty page
			it will show you rank: manager or user at details plate.

		able to update:
			username
			email
			profile pic
			rank
		you will be able to see "add plants" option only if you are manager.

		my orders:
			manager:
				orders placed for you
			user:
				orders you placed

			if you can switch your wank to look into other aspect.

	checkout:
		if no item in cart:
			will ask to you to add
		else:
			will clear your cart
			add orders

	logout:
		to log out
		will give you link to signin again.

	Add plants:
		only manager can add them, bcz only manager can see that option in their profile.
		to check your status from nav bar or details plate, if you are not manager/seller and want to sell, then switch your account to manager rank and then you will be able to see that option in profile section.

		fields:
			plantname
			price
			quantity
			some description
			image

			then post it.


It also has password reset functionality, through email, 
put a mail and password in settings.py and use it.[
	It will not work as of now bcz i am not entering my mail and password bcz of confidentiallity reasons.
]

I have used PIL to give a proper size to plant image. if image is larger than (300x300) then it will resize that image to 300x300.



not perfectly responsive, there are some glitches to be improved.



