from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Contact
from django.views.generic import CreateView
from django.urls import reverse_lazy


def main(reqeust):
    return render(reqeust, 'main.html')


def banquets(reqeust):
    return render(reqeust, 'banquets.html')


def customcake(reqeust):
    return render(reqeust, 'customcake.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['limoncellovl@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main")
    return render(request, "contact.html", {'form': form})


class ContactCreate(CreateView):
    model = Contact
    fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение с формы от {data["first_name"]} {data["last_name"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject, massage):
    send_mail(subject,
              massage,
              'admin@example.com',
              ['limoncellovl@gmail.com']
              )


def success(request):
    return HttpResponse('Письмо отправлено!')


def mainEng(reqeust):
    return render(reqeust, 'mainEng.html')


def banquetsEng(reqeust):
    return render(reqeust, 'banquetsEng.html')


def customcakeEng(reqeust):
    return render(reqeust, 'customcakeEng.html')


def contactEng(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['limoncellovl@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main")
    return render(request, "contactEng.html", {'form': form})


def menu(reqeust):
    return render(reqeust, 'menu.html')
