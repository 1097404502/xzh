```bash

 kolla-ansible help
Usage: /py3_env/bin/kolla-ansible COMMAND [options]

Options:
    --inventory, -i <inventory_path>   Specify path to ansible inventory file
    --playbook, -p <playbook_path>     Specify path to ansible playbook file
    --configdir <config_path>          Specify path to directory with globals.yml
    --key -k <key_path>                Specify path to ansible vault keyfile
    --help, -h                         Show this usage information
    --tags, -t <tags>                  Only run plays and tasks tagged with these values
    --skip-tags <tags>                 Only run plays and tasks whose tags do not match these values
    --extra, -e <ansible variables>    Set additional variables as key=value or YAML/JSON passed to ansible-playbook
    --passwords <passwords_path>       Specify path to the passwords file
    --limit <host>                     Specify host to run plays
    --forks <forks>                    Number of forks to run Ansible with
    --vault-id <@prompt or path>       Specify @prompt or password file (Ansible >=  2.4)
    --ask-vault-pass                   Ask for vault password
    --vault-password-file <path>       Specify password file for vault decrypt
    --verbose, -v                      Increase verbosity of ansible-playbook

Environment variables:
    EXTRA_OPTS                         Additional arguments to pass to ansible-playbook

Commands:
    prechecks            Do pre-deployment checks for hosts
    check                Do post-deployment smoke tests
    mariadb_recovery     Recover a completely stopped mariadb cluster
    mariadb_backup       Take a backup of MariaDB databases
                             --full (default)
                             --incremental
    bootstrap-servers    Bootstrap servers with kolla deploy dependencies
    destroy              Destroy Kolla containers, volumes and host configuration
                             --include-images to also destroy Kolla images
                             --include-dev to also destroy dev mode repos
    deploy               Deploy and start all kolla containers
    deploy-bifrost       Deploy and start bifrost container
    deploy-servers       Enroll and deploy servers with bifrost
    deploy-containers    Only deploy and start containers (no config updates or bootstrapping)
    post-deploy          Do post deploy on deploy node
    pull                 Pull all images for containers (only pulls, no running container changes)
    reconfigure          Reconfigure OpenStack service
    stop                 Stop Kolla containers
    certificates         Generate self-signed certificate for TLS *For Development Only*
    octavia-certificates Generate certificates for octavia deployment
    upgrade              Upgrades existing OpenStack Environment
    upgrade-bifrost      Upgrades an existing bifrost container
    genconfig            Generate configuration files for enabled OpenStack services
    prune-images         Prune orphaned Kolla images

```