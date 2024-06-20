import django.contrib.auth
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from forms_builder.models import Field, FieldChoice, Form, Section
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from forms_builder.form import FormBuilderForm
from django.contrib.auth.decorators import login_required

class FormListView(ListView):
    model = Form
    context_object_name = 'forms'
    template_name='forms_builder/list.html'

class FormDetailView(DetailView):
    model = Form
    context_object_name = 'form_data'
    template_name = "forms_builder/details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = self.object.sections.all().prefetch_related('form_fields__choices')
        return context


class FormCreateView(CreateView):
    model = Form
    form_class = FormBuilderForm
    template_name = "forms_builder/create.html"
    success_url = reverse_lazy('forms-builder-list')
    

class FormUpdateView(UpdateView):
    model = Form
    form_class = FormBuilderForm
    template_name = "forms_builder/edit.html"
    success_url = reverse_lazy('forms-builder-list')


class FormDeleteView(DeleteView):
    model = Form
    context_object_name = 'form_data'
    template_name = "forms_builder/delete.html"
    success_url = reverse_lazy('forms-builder-list')

@login_required
def create_section(request, pk):
    form = Form.objects.get(pk=pk)
    section = Section.objects.create(
        name=request.POST['name'],
        form = form
    )
    return redirect('/forms-builder/details/'+pk)

@login_required
def delete_section(request, pk):
    section = Section.objects.get(pk = pk)
    section.delete()    
    return redirect('/forms-builder/details/'+ str(section.form.id))

@login_required
def create_field(request):
    section = Section.objects.get(pk=request.POST['section'])
    field = Field.objects.create(
        label=request.POST['label'],
        name=request.POST['name'],
        field_type=request.POST['type'],
        order=request.POST['order'],
        section = section
    )
    return redirect('/forms-builder/details/'+ str(section.form.id))

@login_required
def delete_field(request, pk):
    field = Field.objects.get(pk = pk)
    field.delete()  
    section_id = field.section.form.id  
    return redirect('/forms-builder/details/'+ str(section_id))

@login_required
def create_choice(request):
    field = Field.objects.get(pk=request.POST['field'])
    choice = FieldChoice.objects.create(
        choice_text=request.POST['choice_text'],
        field = field
    )
    return redirect('/forms-builder/details/'+ str(field.section.form.id))

@login_required
def delete_choice(request, pk):
    choice = FieldChoice.objects.get(pk = pk)
    choice.delete()  
    form_id = choice.field.section.form.id  
    return redirect('/forms-builder/details/'+ str(form_id))

@login_required
def preview(request, pk):
    form = get_form_with_fields_and_choices(pk)
    return render(request, 'forms_builder/preview.html', {'form': form})

@login_required
def publish(request, pk):
    form = Form.objects.get(pk=pk)
    return redirect('/forms-builder/details/'+ str(form.id))


def get_form_with_fields_and_choices(form_id):
    form = get_object_or_404(Form, id=form_id)
    form_data = {
        "id": form.id,
        "name": form.name,
        "description": form.description,
        "status": form.status,
        "created_on": form.created_on,
        "published_on": form.published_on,
        "created_by": form.created_by.username if form.created_by else None,
        "sections": []
    }
    
    for section in form.sections.all():
        section_data = {
            "name": section.name,
            "fields": []
        }
        
        for field in section.form_fields.all():
            field_data = {
                "label": field.label,
                "name": field.name,
                "required": field.required,
                "field_type": field.field_type,
                "order": field.order,
                "choices": []
            }
            
            for choice in field.choices.all():
                choice_data = {
                    "order": choice.order,
                    "choice_text": choice.choice_text
                }
                field_data["choices"].append(choice_data)
                
            section_data["fields"].append(field_data)
        
        form_data["sections"].append(section_data)
    
    return form_data