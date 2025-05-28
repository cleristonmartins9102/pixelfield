from django.db import models
from django.utils.timezone import now

from . import UserModel, BookModel

class LoanModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_fk')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='book_fk')
    borrow = models.DateTimeField(default=now)
    returned_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)