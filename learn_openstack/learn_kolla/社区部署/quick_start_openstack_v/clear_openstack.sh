
venv_path='/py3_env'
source ${venv_path}/bin/activate

kolla-ansible destroy  --include-images  --yes-i-really-really-mean-it

