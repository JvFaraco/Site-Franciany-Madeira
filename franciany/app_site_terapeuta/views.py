from django.shortcuts import render, redirect


def home(request):
    return render(request, 'franciany/home.html')


def whatsapp(request):
    return redirect('https://api.whatsapp.com/send?phone=5548988482713&text=Olá.%20Gostaria%20de%20Informações%20sobre%20atendimento%20em%20Psicogenealogia.')


def instagram(request):
    return redirect('https://www.instagram.com/francianymadeira/')


def obrigado(request):
    return render(request, 'franciany/obrigado.html')
