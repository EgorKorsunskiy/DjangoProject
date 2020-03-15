from django.views.generic import DetailView
from main.models import Ad


class AdView(DetailView):

    model = Ad
    template_name = 'ad/index.html'

    def get_context_data(self, **kwargs):
        all_ad = Ad.ad.get(pk=self.kwargs['pk'])
        context = {'ad': all_ad}
        return context
