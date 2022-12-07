import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from voting.models import Binary_Voting

from django.shortcuts import get_object_or_404

from base import mods


# TODO: check permissions and census
class BoothView(TemplateView):
    template_name = 'booth/booth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})

            # Casting numbers to string to manage in javascript with BigInt
            # and avoid problems with js and big number conversion
            for k, v in r[0]['pub_key'].items():
                r[0]['pub_key'][k] = str(v)

            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        context['KEYBITS'] = settings.KEYBITS

        return context

class BinaryBoothView(TemplateView):
    template_name = 'booth/booth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            binary_voting = get_object_or_404(Binary_Voting,pk=vid)


            context['voting'] = json.dumps(Binary_Voting.to_json(binary_voting))
        except:
            raise Http404

        context['KEYBITS'] = settings.KEYBITS

        return context
