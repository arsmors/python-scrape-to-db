import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
from .models import Headline
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q


class SampleClass(View):
    template_name = "index.html"

    def get(self, request):

        source = requests.get('https://money.cnn.com/data/markets/').text
        soup = BeautifulSoup(source, 'html.parser')

        for table in soup.find_all('a', class_="stock"):
            ins = table.find('span', class_="column stock-name")
            instrument = ins.text
            pri = table.find('span', class_="column stock-price")
            price = pri.text
            cha = table.find('span', class_="column stock-change")
            change = cha.text

            self.add(instrument, price, change)
        return render(request, self.template_name, {})

    def list(self):
        return Headline.objects.all()

    def add(self, instrument, price, change, operation='add'):
        if operation.lower() == 'add':
            obj = Headline.objects.create(instrument=instrument, price=price, change=change)
            for row in Headline.objects.all():
                if Headline.objects.filter(instrument=instrument).count() > 1:
                    row.delete()

        elif operation.lower() == 'delete':
            obj = Headline.objects.get(instrument=instrument)
            obj.delete

        return obj


class HeadlineListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Headline.objescts.filter(
                Q(category_iexact=slug) |
                Q(category_icontains=slug)
            )
        else:
            queryset = Headline.objects.all()
        return queryset


class HeadlineDetailView(DetailView):
    queryset = Headline.objects.all()

#  def get_object(self, *args, **kwargs):
#    rest_id = self.kwargs.get('rest_id')
#    obj = get_object_or_404(Headline, id = rest_id)
#    return obj
