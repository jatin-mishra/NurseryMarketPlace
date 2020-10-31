from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
# Create your models here.

class AccountManager(BaseUserManager):

	def create_user(self, email, username, password=None, is_manager=False):
		if not email:
			raise ValueError('Users must have an email')

		if not username:
			raise ValueError('Users must have an userName')

		if not password:
			raise ValueError('password is required to create user')

		user = self.model(email=self.normalize_email(email), username=username)
		user.set_password(password)
		user.is_manager = is_manager
		user.save(using=self._db)
		return user


	def create_superuser(self, email, username, password=None, is_manager=False):
		user = self.create_user(email=self.normalize_email(email), username=username, password=password, is_manager=is_manager)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, username, password=None, is_manager=False):
		user = self.create_user(email, username, password, is_manager)
		user.is_staff = True
		user.save(using=True)
		return user

class customUser(AbstractBaseUser):
	email = models.EmailField(verbose_name='email', max_length=60, unique=True)
	username = models.CharField(max_length=30, unique=True)
	date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)
	is_manager = models.BooleanField(default=False)
	profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']


	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.profile_pic.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.profile_pic.path)



