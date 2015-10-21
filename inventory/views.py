from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic

from .models import Platform, Game


class IndexView(generic.ListView):
    template_name = 'inventory/index.html'
    context_object_name = 'platform_list'

    def get_queryset(self):
        """

        :return:
        """
        return Platform.objects.all()


class DetailView(generic.DetailView):
    model = Platform
    template_name = 'inventory/detail.html'

    def get_queryset(self):
        """

        :return:
        """
        return Platform.objects.all()


def add_time(request, platform_id):
    """

    :param request:
    :param platform_id:
    :return:
    """
    platform = get_object_or_404(Platform, pk=platform_id)
    try:
        # get number from text field and add to hours_played
        pass
    except KeyError:
        return render(request, 'inventory/detail.html', {
            'platform': platform,
            'error_message': "You didn't select a choice.",
        })
    else:
        # get number from text field and add to hours_played
        pass
