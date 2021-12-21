from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from list_price_revision.models import UserModel
from django.shortcuts import reverse


class LoginRequiredMiddleware(MiddlewareMixin):
    not_required_path = [
        '/login-api/check-auth/'
    ]

    def process_response(self, request, response):
        try:
            obj = UserModel.objects.get(username=request.user)
        except UserModel.DoesNotExist:
            if request.user.is_authenticated:
                UserModel.objects.create(username=request.user)

        if (request.path != reverse('accounts:login') and not request.user.is_authenticated) and request.path not in self.not_required_path:
            return HttpResponseRedirect(reverse('accounts:login'))
        return response
