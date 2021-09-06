from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from portifolio.cadastro.forms import ClienteForm
from portifolio.cadastro.models import Cliente


def Home(request):
    return HttpResponseRedirect(reverse('url_cliente_list'))


def ClienteNew(request):
    cliente = Cliente()
    cliente.is_active = True
    cliente.slug = '***'
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            try:
                cliente = form.save()
                return HttpResponseRedirect(reverse('url_cliente_update', kwargs={'pk': cliente.pk}))
            except Exception as e:
                messages.error(request, e)
    context = {
        'form': form
    }
    return render(request, 'cadastro/cliente_edit.html', context)


def ClienteUpdate(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return HttpResponseRedirect(reverse('url_cliente_update', kwargs={'slug': cliente.slug}))


def ClienteUpdateSlug(request, slug):
    cliente = Cliente.objects.get(slug=slug)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            try:
                cliente = form.save()
                return HttpResponseRedirect(reverse('url_cliente_update', kwargs={'pk': cliente.pk}))
            except Exception as e:
                messages.error(request, e)
    context = {
        'form': form
    }
    return render(request, 'cadastro/cliente_edit.html', context)


def ClienteList(request):
    lista = Cliente.objects.all()
    context = {'lista': lista}
    return render(request, 'cadastro/cliente_list.html', context)


def ClienteDelete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return HttpResponseRedirect(reverse('url_cliente_list'))
