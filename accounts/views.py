from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import BookedHotelModel, UserBookAccount
from django.shortcuts import get_object_or_404, redirect
from post.models import Post
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login , update_session_auth_hash

class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        # print(user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'user_login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserBookAccountUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})

# @login_required
# def ProfileData(request):
#     print(request)
#     if hasattr(request.user, 'account'):
#         user_account = request.user.account

#         if hasattr(user_account, 'user'):
#             user = user_account.user

#             data = BookedHotelModel.objects.filter(user=user, buy_status='PENDING')
#             print(data)
#             return render(request, 'profile.html', {'data': data})
        
#     return render(request, 'profile.html', {'data': None})
@login_required
def ProfileData(request):
    print(request)
    data_pending = None
    data_accepted = None

    if hasattr(request.user, 'account'):
        user_account = request.user.account

        if hasattr(user_account, 'user'):
            user = user_account.user

            data_pending = BookedHotelModel.objects.filter(user=user, buy_status='PENDING')
            data_accepted = BookedHotelModel.objects.filter(user=user, buy_status='Accepted')

        
    return render(request, 'profile.html', {'data_pending': data_pending, 'data_accepted': data_accepted})


# class ReturnBookView(View):
#     def get(self, request, id):
#         book = get_object_or_404(Post, pk=id)
#         user_account = request.user.account
#         user = user_account.user
        
#         if user_account.balance >= book.price:
#             # Deleting from the database
#             purchases = BookedHotelModel.objects.filter(user=user, book=book)
#             for purchase in purchases:
#                 purchase.buy = False
#                 purchase.save()
#                 purchase.delete()

#             user_account.balance += book.price
#             user_account.save()

#             messages.success(request, "Booking canceled successfully.")
#             return redirect('profile')
#         else:
#             messages.success(request, "Booking canceled failed.")
#             return redirect('home')
class ReturnBookView(View):
    def get(self, request, id):
        book = get_object_or_404(Post, pk=id)
        user_account = request.user.account
        user = user_account.user
        
        if user_account.balance >= book.price:
            # Deleting from the database
            purchases = BookedHotelModel.objects.filter(user=user, book=book)
            for purchase in purchases:
                purchase.delete()

            user_account.balance += book.price
            user_account.save()

            messages.success(request, "Booking canceled successfully.")
            return redirect('profile')
        else:
            messages.success(request, "Booking canceled failed.")
            return redirect('home')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})
