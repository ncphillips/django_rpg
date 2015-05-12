from django.views import generic
from django.core.urlresolvers import reverse
from django.shortcuts import render
from forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class LoginView(generic.FormView):

    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = "https://www.google.ca/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=whats%20the%20home%20page%3F"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)
