from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import ColorForm, UserForm, UserProfileForm


class RegisterView(View):
    user_form_class = UserForm
    profile_user_form_class = UserProfileForm
    template_name = 'antmonitor/register_form.html'

    def get(self, request, *args, **kwargs):
        uform = self.user_form_class()
        pform = self.profile_user_form_class()
        return render(request, self.template_name, {'uform':uform, 'pform':pform})

    def post(self, request, *args, **kwargs):
        pass

class SuccessView(View):
    template_name = 'antmonitor/success.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"color":request.COOKIES['color']})


class ColorView(View):
    form_class = ColorForm
    template_name = "antmonitor/color_form.html"
    initial = {'color':'green'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        color = request.COOKIES.get('color', '')
        return render(request, self.template_name, {'form': form,
                                                    'color':color})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            response = HttpResponseRedirect('/success/')
            if 'color' in request.POST:
                response.set_cookie('color', request.POST['color'])
            return response

        return render(request, self.template_name, {'form': form})
