from django.contrib import admin
from .models import BookModel, UserModel, LoanModel

admin.register(BookModel)
admin.register(UserModel)
admin.register(LoanModel)