from types import MethodType
from django.db.models import DateTimeField
from django.core.exceptions import FieldDoesNotExist
from django.utils.safestring import SafeText
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.formats import localize
from datetime import datetime
from django.contrib import admin
from example.models import AModel1, AModel2, AModel3, AModel4, AModel5


def datetime_to_html(datetime: datetime | None) -> SafeText:
    if datetime is None:
        return mark_safe('never')
    return format_html('<span class="local-datetime" data-iso="{}">Custom: {}</span>', datetime.isoformat(), localize(datetime))


class AbstractAdmin(admin.ModelAdmin):
    def __init__(self, model: type, admin_site: admin.AdminSite | None) -> None:
        super().__init__(model, admin_site)
        for field in self.readonly_fields:
            if isinstance(field, str):
                try:
                    f = self.model._meta.get_field(field)
                    if isinstance(f, DateTimeField):
                        field_alias = f'{field}_local'

                        @admin.display(description=f.verbose_name, ordering=field)
                        def get_local_datetime(self, obj=None, f=field):
                            if obj is not None:
                                return datetime_to_html(getattr(obj, f))
                            return None
                        setattr(self, field_alias, MethodType(get_local_datetime, self))
                        self.readonly_fields = [field_alias if n == field else n for n in self.readonly_fields]
                        self.list_display = [field_alias if n == field else n for n in self.list_display]
                        if self.fields:
                            fields = []
                            for field_name in self.fields:
                                if field_name == field:
                                    fields.append(field_alias)
                                elif isinstance(field_name, tuple):
                                    fields.append(tuple(field_alias if n == field else n for n in field_name))
                                else:
                                    fields.append(field_name)
                            self.fields = fields
                        if self.fieldsets:
                            for _, field_options in self.fieldsets:
                                fields = []
                                for field_name in field_options['fields']:
                                    if field_name == field:
                                        fields.append(field_alias)
                                    elif isinstance(field_name, tuple):
                                        fields.append(tuple(field_alias if n == field else n for n in field_name))
                                    else:
                                        fields.append(field_name)
                                field_options['fields'] = fields
                except FieldDoesNotExist:
                    pass


@admin.register(AModel1)
class ExampleAdmin1(AbstractAdmin):
    model = AModel1
    readonly_fields = ['modified1', 'created1']


@admin.register(AModel2)
class ExampleAdmin2(AbstractAdmin):
    model = AModel2
    readonly_fields = ['modified2', 'created2']


@admin.register(AModel3)
class ExampleAdmin3(AbstractAdmin):
    model = AModel3
    readonly_fields = ['modified3', 'created3']


@admin.register(AModel4)
class ExampleAdmin4(AbstractAdmin):
    model = AModel4
    readonly_fields = ['modified4', 'created4']


@admin.register(AModel5)
class ExampleAdmin5(AbstractAdmin):
    model = AModel5
    readonly_fields = ['modified5', 'created5']
