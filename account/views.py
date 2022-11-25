from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView

from .forms import RegisterForm, LoginForm


class RegisterView(View):

    form_class = RegisterForm
    initial = {'key' : 'value'}
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """ En GET on défini et retourne un formulaire de register """
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """ En post on récupère les infos du formulaire """
        form = self.form_class(request.POST)

        if form.is_valid():
            # Formulaire valide, on enregistre le client
            form.save()

            email = form.cleaned_data.get('email')
            messages.success(request, f'Compte créé pour : {email}')

            return redirect(to='book:book-home')

        # Si formulaire invalide on retourne le register
        return render(request, self.template_name, {'form':form})


class TrainLoginView(LoginView):
    
    form_class = LoginForm

    def form_valid(self, form) -> HttpResponse:

        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True


        return super(TrainLoginView, self).form_valid(form) 