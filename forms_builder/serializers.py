import django.db
from rest_framework import serializers  
from users.serializers import UserSerializer
from  .models import Form, Section, Field, FieldChoice

class FieldChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= FieldChoice
        fields= ["id", "choice_text"]


class FieldSerializer(serializers.ModelSerializer):
    choices = FieldChoiceSerializer(many=True)
    
    class Meta: 
        model= Field
        fields=['id', 'label', 'field_type', 'choices']
        
class SectionSerializer(serializers.ModelSerializer):
    form_fields = FieldSerializer(many=True)
    
    class Meta: 
        model= Section
        fields=['id', 'name', 'form_fields']

class FormSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)
    
    class Meta: 
        model= Form
        fields=['id', 'name', 'sections', 'description', 'created_on', 'created_by', 'status', 'published_on']

    def create(self, validated_data):
        sections = validated_data.pop('sections', [])
        form = Form.objects.create(**validated_data)
        
        for section_data in sections:
            fields = section_data.pop('form_fields', [])
            section = Section.objects.create(form=form, **section_data)
            
            for field in fields:
                choices = field.pop('choices', [])
                field = Field.objects.create(section=section, **field)

                for choice in choices:
                    FieldChoice.objects.create(field=field, **choice)
                    
        return form
    def update(self, instance, validated_data):
        sections_data = validated_data.pop("sections")
        
        #get existing sections
        existing_sections = instance.sections.all()
        existing_sections = list(existing_sections)
        
        #save the form data
        instance.name = validated_data.get('name')
        instance.save()
        
        #loop through the section data
        for section_data in sections_data:
            if section_id := section_data.get("id"):
                section = existing_sections.pop(0)
                section.name = section_data.get("name", section.name)
                section.save()
            else:
                #create a new section
                section = Section.objects.create(
                    name=section_data.get("name"), form = instance
                )
                
            #get the form fields
            fields_data = section_data.pop('form_fields', [])
            
            #get existing fields
            existing_fields = section.form_fields.all()
            existing_fields = list(existing_fields)
            
            #loop through the fields data
            for  field_data in fields_data:
                if field_id := field_data.get('id', None):
                    #update existing fields
                    field = existing_fields.pop(0)
                    field.label = field_data.get('label', field.label)
                    field.field_type = field_data.get('field_type', field.field_type)
                    field.save()
                else:
                    field = Field.objects.create(
                        label = field_data.get("label"),
                        field_type = field_data.get("field_type"),
                        section = section
                    )
                
                # get the choices data
                choices_data = field_data.pop("choices", [])
                
                #get existing choices
                existing_choices = field.choices.all()
                existing_choices = list(existing_choices)
                
                #loop through all choices
                for choice_data in choices_data:
                    if choice_id := choice_data.get('id', None):
                        print(choice_id)
                        choice = existing_choices.pop(0)
                        choice.choice_text = choice_data.get(
                            "choice_text", choice.choice_text
                        )
                        choice.save()
                    else:
                        choice = FieldChoice.objects.create(
                            choice_text = choice_data.get('choice_text'), field = field
                        )
                        
                #delete any existing choices
                for choice in existing_choices:
                    choice.delete()
                    
            #delete any existing fields
            for field in existing_fields:
                field.delete()
            
        #delete any existing section
        for section in existing_sections:
            section.delete()
        
        return instance

        