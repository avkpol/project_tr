from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models.control import Control



def controls_list(request):
    controls = Control.objects.all()
    # noinspection PyUnresolvedReferences
    return render(request, 'controls_list.html',
        {"controls":controls})

def index(request):
     return render(request, 'index.html',{})

# def control_edit_form(request):
#     return render(request, 'control_edit_form.html',{})

class ControlUpdateForm(ModelForm):
    class Meta: # determine features of modelkwargs
        model = Control
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ControlUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        # set form tag attributes
        self.helper.form_action = reverse('control_edit_form', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline =True
        self.helper.html5_required =True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Save',css_class = 'btn btn-primary'),
            Submit('cancel_button',u'Cancel', css_class ='btn btn-link'),
            )



#
class ControlUpdateView(UpdateView):
    model = Control
    template_name = 'control_edit_form.html'
    form_class = ControlUpdateForm

    def get_success_url(self):

        return u'%s?status_message= Save'% reverse('home')

    def post(self, request, *args, **kwargs):

        if request.POST.get('cancel_button'):
            return HttpResponseRedirect( u'%s?status_message= Cancel' %reverse('controls_list'))
        else:
            return super(ControlUpdateView, self).post(request, *args,**kwargs)





