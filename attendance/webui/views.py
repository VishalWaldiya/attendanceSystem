from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.edit import CreateView
from datetime import date

# Models
from .models import SecurityPost, Member, Transaction

# Forms
from .forms import TransactionForm

# Create your views here.

class LamdingPage(TemplateView):
    template_name = "webui/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gates = SecurityPost.objects.all()
        
        results = {}
        
        for gate in gates:
            results[gate.name] = Transaction.objects.filter(SecurityPostDetails=gate).filter(inTime__date = date.today())

        context["results"] = results
        # import pdb; pdb.set_trace()
        return context

def index(request):
    return render(request,'webui/menu.html')

class MemberListView(ListView):
    model = Member

# class TransactionCreateView(CreateView):
#     model = Transaction

class CreateTransaction(FormView):
    template_name = "webui/transaction_form.html"
    form_class = TransactionForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        #print "form is valid"
        import pdb; pdb.set_trace()
        return super(CreateTransaction, self).form_valid(form)

    def form_invalid(self, form):
        import pdb; pdb.set_trace()
        return super().form_invalid(form)