import os
import shutil

print(os.getcwd())

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_docc = '{{ cookiecutter.deploy_docc }}' == 'yes'

if not create_docc:
    remove(os.path.join(os.getcwd(), '.github/workflows', 'deploy_docc.yml'))