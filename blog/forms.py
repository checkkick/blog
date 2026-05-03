from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        label="Имя",
        error_messages={"required": "Обязательное поле"},
    )
    email = forms.EmailField(
        label="Ваша почта",
        error_messages={
            "required": "Обязательное поле",
            "invalid": "Введите корректную почту",
        },
    )
    to = forms.EmailField(
        label="Кому",
        error_messages={
            "required": "Обязательное поле",
            "invalid": "Введите корректную почту",
        },
    )
    comments = forms.CharField(
        required=False, widget=forms.Textarea, label="Комментарий"
    )
