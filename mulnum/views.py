from django.shortcuts import render
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import loader
from django.views import generic
from .models import Num
from django.urls import reverse
from django.utils import timezone

# Create your views here.

# class IndexView(generic.ListView):
#     template_name = 'mulnum/index.html'
#     context_object_name = 'latest_firstnum'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Num.objects.order_by('-pub_date')[:5]

# answer = []
# muled = range(1,13)
# def multiple(request):
#     i = Num.objects.all()
#     nummul = Num.objects.request.POST.get('number')
#     for k in muled :
#         ans = nummul * k
#         answer.append(ans)
#     return HttpResponseRedirect(reverse('mulnum:index'))

# class IndexView(generic.ListView):
#     template_name = 'mulnum/index.html'
#     context_object_name = 'latest_num_list'

def show(request,id):
    context = {'number': id }

    return render(request, 'mulnum/index.html', context)