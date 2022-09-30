
class BoostrapFormMixin:
    fields = {}
    disabled_fields = '__all__'

    def _init_bootstrap_fields(self):
        for name, field in self.fields.items():
            if not hasattr(field, 'attrs'):
                setattr(field, 'attrs', {})

            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''

            field.widget.attrs['class'] += 'form-control'

    def _init_disabled_fields(self):
        for (name, field) in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue

            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'



