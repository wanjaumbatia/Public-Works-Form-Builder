from django.shortcuts import redirect
from django.urls import reverse_lazy
from forms_builder.models import Field, Form, Section
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from forms_builder.form import FormBuilderForm

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


def create_section(request, pk):
    form = Form.objects.get(pk=pk)
    section = Section.objects.create(
        name=request.POST['name'],
        form = form
    )
    return redirect('/forms-builder/details/'+pk)

def delete_section(request, pk):
    section = Section.objects.get(pk = pk)
    section.delete()    
    return redirect('/forms-builder/details/'+ str(section.form.id))

def delete_field(request, pk):
    field = Field.objects.get(pk = pk)
    field.delete()  
    section_id = field.section.form.id  
    return redirect('/forms-builder/details/'+ str(section_id))
