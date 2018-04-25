from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from enquete.models import Questao, Escolhas
from django.template import loader
from django.urls import reverse

# Create your views here.

def index(request):
#    latest_question_list = Questao.objects.order_by('-questao_data_pub')[:5]
#    output = ', '.join([q.questao_pergunta for q in latest_question_list])
#    return HttpResponse(output)
    latest_question_list = Questao.objects.order_by('-questao_data_pub')
    #escolhas_list = Escolhas.objects.order_by('-questao_fk')
    #template = loader.get_template('enquete/index.html')
    template = loader.get_template('enquete/detalhes.html')
    context = {
        'latest_question_list': latest_question_list,
    #    'escolhas_list' : escolhas_list,
    }
    return HttpResponse(template.render(context, request))

def detalhes(request, questao_id):
	#questao = Questao.objects.get(id=questao_id)
    return HttpResponse("You're looking at question %d." % questao_id)

def resultado(request, questao_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % questao_id)
    question = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'enquete/resultado.html', {'question': question})

def votar(request, questao_id):
    #return HttpResponse("You're voting on question %s." % questao_id)
    '''
    if 'questao' in request.POST:
        message = 'You VOTED for: %r' % request.POST['questao']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
    #DJANGO TUTORIAL
    '''
    question = get_object_or_404(Questao, pk=questao_id)
    try:
        selected_choice = question.escolhas_set.get(pk=request.POST['questao'])
    except (KeyError, Escolhas.DoesNotExist):
        # HttpResponse("EXCEPTION EM> You're voting on question %s. Selecionada a opção: %s." % questao_id, % selected_choice)
        # Redisplay the question voting form.
        return render(request, 'enquete/detalhes.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.qtd_votos += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('enquete:resultado', args=(question.id,)))
    