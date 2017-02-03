from wtforms import Form
from jinja2 import Template
from traitlets import Type, HasTraits, List, Dict, Unicode

class MockMultiDict(dict):
    def getlist(self, key):
        value = self[key]
        return value if isinstance(value, list) else [self[key]]

class FormSpawner(HasTraits):
    options_form_template = Unicode("""
{% for field in form %}
    {{ field.label() }} {{ field() }} <br>
{% endfor %}""")

    form_class = Type(Form).tag(config=True)
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.form = self.form_class()

    @property
    def options_form(self):
       return Template(self.options_form_template).render(form=self.form) 

    def options_from_form(self, options):
        self.form.process(formdata=MockMultiDict(options))
        if not self.form.validate():
            raise Exception(self.form.errors)
        return self.form.data 

def form_wrapper(baseclass, name):
    return type(name, (FormSpawner, baseclass), {})
