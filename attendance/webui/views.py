from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from datetime import datetime, timedelta, date

# Models
from .models import SecurityPost, Member, Transaction

# Forms
from .forms import TransactionForm

# Create your views here.

class LandingPage(TemplateView):
    template_name = "webui/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gates = SecurityPost.objects.all()
        
        results = {}
        datetoday = datetime.now() + timedelta(hours=5,minutes = 30)
        for gate in gates:
            results[gate.name] = Transaction.objects.filter(SecurityPostDetails=gate).filter(inTime__date = datetoday.date())

        context["results"] = results
        context["form"] = TransactionForm
        # import pdb; pdb.set_trace()
        return context

def index(request):
    return render(request,'webui/menu.html')

class MemberListView(ListView):
    model = Member

class CreateTransaction(FormView):
    template_name = "webui/transaction_form.html"
    form_class = TransactionForm
    success_url = reverse_lazy('webui:home')

    def form_invalid(self, form):
        date_format = '%Y-%m-%d %H:%M'
        outTime = datetime.strptime(form.data.get('outime').replace('T',' '), date_format)
        inTime = datetime.strptime(form.data.get('inTime').replace('T',' '), date_format)
        MemberDetails__id = form.data.get('ID')
        SecurityPostDetails__id = form.data.get('SecurityPost')
        inTime = inTime
        outtime = outTime
        obj = Transaction.objects.create(
            MemberDetails = Member.objects.get(pk=MemberDetails__id),
            SecurityPostDetails = SecurityPost.objects.get(pk=SecurityPostDetails__id),
            inTime = inTime,
            outtime = outtime
        )
        return HttpResponseRedirect(self.get_success_url())
        # return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context