from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsPreferencesForm

def customize_news(request):
    if request.method == 'POST':
        form = NewsPreferencesForm(request.POST)
        if form.is_valid():
            response = redirect('customize_news')
            response.set_cookie('topics', ','.join(form.cleaned_data.get('topics', [])), max_age=3600*24*30)
            response.set_cookie('sources', form.cleaned_data.get('sources', ''), max_age=3600*24*30)
            response.set_cookie('language', form.cleaned_data.get('language', ''), max_age=3600*24*30)
            messages.success(request, 'Ваши настройки успешно сохранены!')
            return response
    else:
        initial_data = {
            'topics': request.COOKIES.get('topics', '').split(','),
            'sources': request.COOKIES.get('sources', ''),
            'language': request.COOKIES.get('language', ''),
        }
        form = NewsPreferencesForm(initial=initial_data)

    return render(request, 'myapp/news_form.html', {'form': form})