from django.views.generic.list import ListView

from .models import Ad, User


class MainView(ListView):

    model = Ad
    template_name = 'main/alternative.html'

    def get_context_data(self, **kwargs):
        all_ad = Ad.ad.all()
        context = {'users': all_ad,
                   'login_user': None
                   }
        return context


class MainLoginView(ListView):

    model = Ad
    template_name = 'main/alternative.html'

    def get_context_data(self, **kwargs):
        all_ad = Ad.ad.all()
        context = {'users': all_ad,
                   'login_user': User.user.get(full_name=self.kwargs['user'])
                   }
        return context
