@[toc]
# cinder --help
usage: cinder [--version] [-d] [--os-auth-system <auth-system>]
              [--service-type <service-type>] [--service-name <service-name>]
              [--volume-service-name <volume-service-name>]
              [--os-endpoint-type <os-endpoint-type>]
              [--endpoint-type <endpoint-type>]
              [--os-volume-api-version <volume-api-ver>]
              [--bypass-url <bypass-url>] [--retries <retries>]
              [--profile HMAC_KEY] [--os-auth-strategy <auth-strategy>]
              [--os-username <auth-user-name>] [--os-password <auth-password>]
              [--os-tenant-name <auth-tenant-name>]
              [--os-tenant-id <auth-tenant-id>] [--os-auth-url <auth-url>]
              [--os-user-id <auth-user-id>]
              [--os-user-domain-id <auth-user-domain-id>]
              [--os-user-domain-name <auth-user-domain-name>]
              [--os-project-id <auth-project-id>]
              [--os-project-name <auth-project-name>]
              [--os-project-domain-id <auth-project-domain-id>]
              [--os-project-domain-name <auth-project-domain-name>]
              [--os-region-name <region-name>] [--os-token <token>]
              [--os-url <url>] [--insecure] [--os-cacert <ca-certificate>]
              [--os-cert <certificate>] [--os-key <key>] [--timeout <seconds>]
              <subcommand> ...

Command-line interface to the OpenStack Cinder API.

Positional arguments:
  <subcommand>
    absolute-limits     Lists absolute limits for a user.
    availability-zone-list
                        Lists all availability zones.
    backends-create     create a backend storage type
    backends-delete     delete a backend storage type
    backends-list       show all backend storage types
    backends-update     update a backend storage type
    backup-create       Creates a volume backup.
    backup-delete       Removes one or more backups.
    backup-dump-chain   dump relation chain for the backup.
    backup-export       Export backup metadata record.
    backup-import       Import backup metadata record.
    backup-list         Lists all backups.
    backup-reset-state  Explicitly updates the backup state.
    backup-restore      Restores a backup.
    backup-show         Shows backup details.
    bind-vtype-to-backend
                        bind a volume type with a backend storage type.
    ceph-crush-map-list
    ceph-crush-ruleset-list
    ceph-mon-list
    ceph-osd-create
    ceph-osd-delete
    ceph-osd-host-delete
                        Delete a ceph osd host disk
    ceph-osd-host-list  Lists all ceph osd hosts.
    ceph-osd-host-update
                        update a ceph osd host disk
    ceph-osd-list
    ceph-osd-obj-recovery-progress
    ceph-osd-perf
    ceph-osd-reweight
    ceph-osd-update
    ceph-pg-get-full-ratio
    ceph-pg-list
    ceph-pg-list-by-osd
    ceph-pg-list-by-pool
    ceph-pg-list-by-state
    ceph-pg-update
    ceph-pool-create
    ceph-pool-delete
    ceph-pool-list
    ceph-pool-update
    ceph-status
    ceph-tier-create
    ceph-tier-delete
    ceph-tier-list
    ceph-tier-update
    ceph-valid-pg-state-items
    ceph-valid-tier-modes
    ceph-valid-update-osd-items
    ceph-valid-update-pg-items
    ceph-valid-update-pool-items
    ceph-valid-update-tier-items
    cgsnapshot-create   Creates a cgsnapshot.
    cgsnapshot-delete   Removes one or more cgsnapshots.
    cgsnapshot-list     Lists all cgsnapshots.
    cgsnapshot-show     Shows cgsnapshot details.
    consisgroup-create  Creates a consistency group.
    consisgroup-create-from-src
                        Creates a consistency group from a cgsnapshot or a
                        source CG.
    consisgroup-delete  Removes one or more consistency groups.
    consisgroup-list    Lists all consistencygroups.
    consisgroup-show    Shows details of a consistency group.
    consisgroup-update  Updates a consistencygroup.
    create              Creates a volume.
    credentials         Shows user credentials returned from auth.
    delete              Removes one or more volumes.
    encryption-type-create
                        Creates encryption type for a volume type. Admin only.
    encryption-type-delete
                        Deletes encryption type for a volume type. Admin only.
    encryption-type-list
                        Shows encryption type details for volume types. Admin
                        only.
    encryption-type-show
                        Shows encryption type details for a volume type. Admin
                        only.
    encryption-type-update
                        Update encryption type information for a volume type
                        (Admin Only).
    endpoints           Discovers endpoints registered by authentication
                        service.
    extend              Attempts to extend size of an existing volume.
    extra-specs-list    Lists current volume types and extra specs.
    failover-host
    force-delete        Attempts force-delete of volume, regardless of state.
    freeze-host
    get-capabilities    Show backend volume stats and properties. Admin only.
    get-pools           Show pool information for backends. Admin only.
    image-metadata      Sets or deletes volume image metadata.
    image-metadata-show
                        Shows volume image metadata.
    list                Lists all volumes.
    manage              Manage an existing volume.
    metadata            Sets or deletes volume metadata.
    metadata-show       Shows volume metadata.
    metadata-update-all
                        Updates volume metadata.
    migrate             Migrates volume to a new host.
    qos-associate       Associates qos specs with specified volume type.
    qos-create          Creates a qos specs.
    qos-delete          Deletes a specified qos specs.
    qos-disassociate    Disassociates qos specs from specified volume type.
    qos-disassociate-all
                        Disassociates qos specs from all its associations.
    qos-get-association
                        Lists all associations for specified qos specs.
    qos-key             Sets or unsets specifications for a qos spec.
    qos-list            Lists qos specs.
    qos-show            Shows qos specs details.
    quota-class-show    Lists quotas for a quota class.
    quota-class-update  Updates quotas for a quota class.
    quota-defaults      Lists default quotas for a tenant.
    quota-delete        Delete the quotas for a tenant.
    quota-show          Lists quotas for a tenant.
    quota-update        Updates quotas for a tenant.
    quota-usage         Lists quota usage for a tenant.
    rate-limits         Lists rate limits for a user.
    readonly-mode-update
                        Updates volume read-only access-mode flag.
    rename              Renames a volume.
    replication-promote
                        Promote a secondary volume to primary for a
                        relationship.
    replication-reenable
                        Sync the secondary volume with primary for a
                        relationship.
    reset-data          Reset the data of a volume.
    reset-state         Explicitly updates the volume state in the Cinder
                        database.
    retype              Changes the volume type for a volume.
    service-disable     Disables the service.
    service-enable      Enables the service.
    service-list        Lists all services. Filter by host and service binary.
    set-bootable        Update bootable status of a volume.
    show                Shows volume details.
    snapshot-create     Creates a snapshot.
    snapshot-delete     Removes one or more snapshots.
    snapshot-list       Lists all snapshots.
    snapshot-manage     Manage an existing snapshot.
    snapshot-metadata   Sets or deletes snapshot metadata.
    snapshot-metadata-show
                        Shows snapshot metadata.
    snapshot-metadata-update-all
                        Updates snapshot metadata.
    snapshot-rename     Renames a snapshot.
    snapshot-reset-state
                        Explicitly updates the snapshot state.
    snapshot-restore    Restores a snapshot.
    snapshot-show       Shows snapshot details.
    snapshot-unmanage   Stop managing a snapshot.
    thaw-host
    transfer-accept     Accepts a volume transfer.
    transfer-create     Creates a volume transfer.
    transfer-delete     Undoes a transfer.
    transfer-list       Lists all transfers.
    transfer-show       Shows transfer details.
    type-access-add     Adds volume type access for the given project.
    type-access-list    Print access information about the given volume type.
    type-access-remove  Removes volume type access for the given project.
    type-create         Creates a volume type.
    type-default        List the default volume type.
    type-delete         Deletes a volume type.
    type-key            Sets or unsets extra_spec for a volume type.
    type-list           Lists available 'volume types'. (Admin only will see
                        private types)
    type-show           Show volume type details.
    type-update         Updates volume type name, description, and/or
                        is_public.
    unbind-vtype-to-backend
                        unbind a volume type from a backend storage type.
    unmanage            Stop managing a volume.
    update-status-based-on-attachment
                        Update a volume's status based its attachment.
    upload-to-image     Uploads volume to Image Service as an image.
    bash-completion     Prints arguments for bash_completion.
    help                Shows help about this program or one of its
                        subcommands.
    list-extensions     Lists all available os-api extensions.

Optional arguments:
  --version             show program's version number and exit
  -d, --debug           Shows debugging output.
  --os-auth-system <auth-system>
                        Defaults to env[OS_AUTH_SYSTEM].
  --service-type <service-type>
                        Service type. For most actions, default is volume.
  --service-name <service-name>
                        Service name. Default=env[CINDER_SERVICE_NAME].
  --volume-service-name <volume-service-name>
                        Volume service name.
                        Default=env[CINDER_VOLUME_SERVICE_NAME].
  --os-endpoint-type <os-endpoint-type>
                        Endpoint type, which is publicURL or internalURL.
                        Default=env[OS_ENDPOINT_TYPE] or nova
                        env[CINDER_ENDPOINT_TYPE] or publicURL.
  --endpoint-type <endpoint-type>
                        DEPRECATED! Use --os-endpoint-type.
  --os-volume-api-version <volume-api-ver>
                        Block Storage API version. Valid values are 1 or 2.
                        Default=env[OS_VOLUME_API_VERSION].
  --bypass-url <bypass-url>
                        Use this API endpoint instead of the Service Catalog.
                        Defaults to env[CINDERCLIENT_BYPASS_URL].
  --retries <retries>   Number of retries.
  --profile HMAC_KEY    HMAC key to use for encrypting context data for
                        performance profiling of operation. This key needs to
                        match the one configured on the cinder api server.
                        Without key the profiling will not be triggered even
                        if osprofiler is enabled on server side.
  --os-auth-strategy <auth-strategy>
                        Authentication strategy (Env: OS_AUTH_STRATEGY,
                        default keystone). For now, any other value will
                        disable the authentication.
  --os-username <auth-user-name>
                        OpenStack user name. Default=env[OS_USERNAME].
  --os-password <auth-password>
                        Password for OpenStack user. Default=env[OS_PASSWORD].
  --os-tenant-name <auth-tenant-name>
                        Tenant name. Default=env[OS_TENANT_NAME].
  --os-tenant-id <auth-tenant-id>
                        ID for the tenant. Default=env[OS_TENANT_ID].
  --os-auth-url <auth-url>
                        URL for the authentication service.
                        Default=env[OS_AUTH_URL].
  --os-user-id <auth-user-id>
                        Authentication user ID (Env: OS_USER_ID).
  --os-user-domain-id <auth-user-domain-id>
                        OpenStack user domain ID. Defaults to
                        env[OS_USER_DOMAIN_ID].
  --os-user-domain-name <auth-user-domain-name>
                        OpenStack user domain name. Defaults to
                        env[OS_USER_DOMAIN_NAME].
  --os-project-id <auth-project-id>
                        Another way to specify tenant ID. This option is
                        mutually exclusive with --os-tenant-id. Defaults to
                        env[OS_PROJECT_ID].
  --os-project-name <auth-project-name>
                        Another way to specify tenant name. This option is
                        mutually exclusive with --os-tenant-name. Defaults to
                        env[OS_PROJECT_NAME].
  --os-project-domain-id <auth-project-domain-id>
                        Defaults to env[OS_PROJECT_DOMAIN_ID].
  --os-project-domain-name <auth-project-domain-name>
                        Defaults to env[OS_PROJECT_DOMAIN_NAME].
  --os-region-name <region-name>
                        Region name. Default=env[OS_REGION_NAME].
  --os-token <token>    Defaults to env[OS_TOKEN].
  --os-url <url>        Defaults to env[OS_URL].
  --insecure            Explicitly allow client to perform "insecure" TLS
                        (https) requests. The server's certificate will not be
                        verified against any certificate authorities. This
                        option should be used with caution.
  --os-cacert <ca-certificate>
                        Specify a CA bundle file to use in verifying a TLS
                        (https) server certificate. Defaults to
                        env[OS_CACERT].
  --os-cert <certificate>
                        Defaults to env[OS_CERT].
  --os-key <key>        Defaults to env[OS_KEY].
  --timeout <seconds>   Set request timeout (in seconds).

Run "cinder help SUBCOMMAND" for help on a subcommand.
