from django import forms

class NewsPreferencesForm(forms.Form):
    topics = forms.MultipleChoiceField(
        choices=[
            ('tech', 'Технологии'),
            ('science', 'Наука'),
            ('business', 'Бизнес'),
            ('world', 'Новости мира'),
            ('sports', 'Спорт'),
            ('culture', 'Культура'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Интересующие темы'
    )
    sources = forms.CharField(
        required=False,
        label='Предпочтительные источники (через запятую)',
        help_text='Например: РИА Новости, Лента.ру, Meduza',
    )
    language = forms.ChoiceField(
        choices=[
            ('ru', 'Русский'),
            ('en', 'Английский'),
            ('es', 'Испанский'),
        ],
        required=False,
        label='Язык',
    )