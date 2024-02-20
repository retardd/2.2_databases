from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, CollectTags, Tags

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if 'maintag' in form.cleaned_data:
                if form.cleaned_data['maintag']:
                    count += 1
            if count == 0:
                raise ValidationError('Выберите основной тэг')
            elif count > 1:
                raise ValidationError('Выберите только один основной тэг')
            else:
                pass
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = CollectTags
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tags)
class ObjectAdmin(admin.ModelAdmin):
    pass