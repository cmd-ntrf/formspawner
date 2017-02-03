from formspawner import form_wrapper
from batchspawner import MoabSpawner
from wtforms import Form, StringField, validators, IntegerField

class MoabForm(Form):
    runtime  = IntegerField('Runtime (hours)', [validators.NumberRange(min=1, max=10)])
    email    = StringField('Email Address', [validators.Length(min=6, max=70)])

c.JupyterHub.spawner_class = form_wrapper(MoabSpawner, "MoabFormSpawner") 
c.MoabFormSpawner.form_class = MoabForm
c.MoabFormSpawner.req_nprocs = '8'
c.MoabFormSpawner.batch_submit_cmd = 'cat'
c.MoabFormSpawner.batch_script = """#!/bin/sh
#PBS -l walltime={user_options[runtime]}:00:00
#PBS -l nodes=1:ppn={nprocs}
#PBS -N jupyterhub-singleuser
#PBS -v {keepvars}
#PBS {options}
{cmd}
"""

