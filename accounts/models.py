from django.db import models

from django.contrib.auth.models import User

from post.models import Post


class UserBookAccount(models.Model):

    user = models.OneToOneField(
        User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)


    def __str__(self):
        return str(self.account_no)



class UserAddress(models.Model):

    user = models.OneToOneField(
        User, related_name='address', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.email)


BOOKING_STATUS=[
    ('PENDING','Pending'),
    ('Accepted', 'Accepted'),
]

class BookedHotelModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)

    buy_status = models.CharField(choices=BOOKING_STATUS, max_length=10, default='PENDING')

    def __str__(self):

        return f"{self.id}-{self.user.first_name}  Hotel : {self.book.title}"

