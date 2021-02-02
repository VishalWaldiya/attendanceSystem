from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from datetime import date

# Models
from .models import SecurityPost, MemberList, TransactionPermanent

# Forms
from .forms import TransactionPermanentForm

# Create your views here.

class LamdingPage(TemplateView):
    template_name = "webui/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gates = SecurityPost.objects.all()
        
        results = {}
        
        for gate in gates:
            results[gate.name] = TransactionPermanent.objects.filter(SecurityPostDetails=gate).filter(inTime__date = date.today())

        context["results"] = results
        # import pdb; pdb.set_trace()
        return context

def index(request):
    return render(request,'webui/menu.html')

class MemberListListView(ListView):
    model = MemberList


# class TransactionPermanentCreateView(CreateView):
#     model = TransactionPermanent

class CreateTransaction(TemplateView):
    template_name = "webui/transactionpermanent_form.html"

    # def get_context_data(self, **kwargs):

    #     form_class = TransactionPermanentForm
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TransactionPermanentForm
        return context
    