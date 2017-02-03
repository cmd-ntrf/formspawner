from collections import OrderedDict
from formspawner import FormSpawner
from batchspawner import MoabSpawner
from wtforms import BooleanField, StringField, validators, IntegerField, SelectField, SelectMultipleField, Form
from wtforms.fields.html5 import EmailField

class MoabFormSpawner(FormSpawner, MoabSpawner):
    @property
    def options_form(self):
        self.form.project.choices = [('ipm-500-aa', 'ipm-500-aa')] 
        return super().options_form

class MoabForm(Form):
    project   = SelectField("Project")
    runtime   = IntegerField('Runtime (hours)', [validators.NumberRange(min=1, max=10)])
    email_addr = EmailField('Email address', [validators.Email()])

c.JupyterHub.spawner_class = MoabFormSpawner
c.MoabFormSpawner.form_class = MoabForm
c.MoabFormSpawner.req_nprocs = '8'
c.MoabFormSpawner.batch_submit_cmd = 'cat'
c.MoabFormSpawner.batch_script = """#!/bin/sh
#PBS -l walltime={user_options[runtime]}:00:00
#PBS -l nodes=1:ppn={nprocs}
#PBS -N jupyterhub-singleuser
#PBS -v {keepvars}
{cmd}
"""

