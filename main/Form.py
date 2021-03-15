from django.forms.forms import Form
from django.forms import fields,widgets
from acount import models
class StuForm(Form):
    name = fields.CharField(
        max_length=32,)
    age = fields.IntegerField(
        max_value=25,
        min_value=18
    )
    sex = fields.ChoiceField(
        choices=((1,'男'),(2,'女')),
        widget=widgets.Select
    )
    cls_id = fields.ChoiceField(
        choices=tuple(models.cls.objects.all().values_list('id','title')),
        widget=widgets.Select
    )

class ClsForm(Form):
    title = fields.CharField(
        max_length=32
    )

class TeaForm(Form):
    name = fields.CharField(
        max_length=32
    )
    age =fields.IntegerField()
    sex = fields.ChoiceField(
        choices=((1,'男'),(2,'女')),
        widget=widgets.Select
    )