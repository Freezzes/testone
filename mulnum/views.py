from django.shortcuts import render
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from .models import number

# Create your views here.

#call text box
def inputnum(request):
    return render(request,'mulnum/index.html')

#number from url
# def show(request,id):
#     number = []
#     for i in range(1,13):
#         ans = id * i
#         number.append(ans)
#     context = {
#         'id': id,
#         'num': number
#     }
#     return render(request, 'mulnum/showmul.html', context)

#number from textbox
# def mul(request):
#     number = []
#     for i in range(1,13):
#         ans = int(request.POST['inte']) * i
#         number.append(ans)
#     context = {
#         'id': request.POST['inte'],
#         'num': number
#     }
#     return render(request, 'mulnum/showmul.html', context)

def mul(request):
    ans = number.objects.get(request.POST['number'])
    numbers=[]
    for i in range(1,13): 
        numbers.append(int(ans) * i)

    context = {
        'id': request.POST['number'],
        'num': numbers
    }
    return render(request, 'mulnum/showmul.html', context)



def calstat(request):
    k = request.POST['number'] 
    d={}
    all_k = []
    all_k.append(k)
    # if k in d.keys() :
    #     d.values+=1
    # else:
    #     d.keys = k
    #     d.values[k] = 1
    context = {
        'num':k,
        'lst':all_k
    }
    return render(request, 'mulnum/statistic.html', context)
    #return HttpResponseRedirect(reverse('m:often'))

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))