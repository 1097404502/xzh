
 General usage: 
 ==============
usage: ceph [-h] [-c CEPHCONF] [-i INPUT_FILE] [-o OUTPUT_FILE]
            [--setuser SETUSER] [--setgroup SETGROUP] [--id CLIENT_ID]
            [--name CLIENT_NAME] [--cluster CLUSTER]
            [--admin-daemon ADMIN_SOCKET] [-s] [-w] [--watch-debug]
            [--watch-info] [--watch-sec] [--watch-warn] [--watch-error]
            [-W WATCH_CHANNEL] [--version] [--verbose] [--concise]
            [-f {json,json-pretty,xml,xml-pretty,plain,yaml}]
            [--connect-timeout CLUSTER_TIMEOUT] [--block] [--period PERIOD]

Ceph administration tool

optional arguments:
  -h, --help            request mon help
  -c CEPHCONF, --conf CEPHCONF
                        ceph configuration file
  -i INPUT_FILE, --in-file INPUT_FILE
                        input file, or "-" for stdin
  -o OUTPUT_FILE, --out-file OUTPUT_FILE
                        output file, or "-" for stdout
  --setuser SETUSER     set user file permission
  --setgroup SETGROUP   set group file permission
  --id CLIENT_ID, --user CLIENT_ID
                        client id for authentication
  --name CLIENT_NAME, -n CLIENT_NAME
                        client name for authentication
  --cluster CLUSTER     cluster name
  --admin-daemon ADMIN_SOCKET
                        submit admin-socket commands ("help" for help
  -s, --status          show cluster status
  -w, --watch           watch live cluster changes
  --watch-debug         watch debug events
  --watch-info          watch info events
  --watch-sec           watch security events
  --watch-warn          watch warn events
  --watch-error         watch error events
  -W WATCH_CHANNEL, --watch-channel WATCH_CHANNEL
                        watch live cluster changes on a specific channel
                        (e.g., cluster, audit, cephadm, or '*' for all)
  --version, -v         display version
  --verbose             make verbose
  --concise             make less verbose
  -f {json,json-pretty,xml,xml-pretty,plain,yaml}, --format {json,json-pretty,xml,xml-pretty,plain,yaml}
  --connect-timeout CLUSTER_TIMEOUT
                        set a timeout for connecting to the cluster
  --block               block until completion (scrub and deep-scrub only)
  --period PERIOD, -p PERIOD
                        polling period, default 1.0 second (for polling
                        commands only)

 Local commands: 
 ===============

ping <mon.id>           Send simple presence/life test to a mon
                        <mon.id> may be 'mon.*' for all mons
daemon {type.id|path} <cmd>
                        Same as --admin-daemon, but auto-find admin socket
daemonperf {type.id | path} [stat-pats] [priority] [<interval>] [<count>]
daemonperf {type.id | path} list|ls [stat-pats] [priority]
                        Get selected perf stats from daemon/admin socket
                        Optional shell-glob comma-delim match string stat-pats
                        Optional selection priority (can abbreviate name):
                         critical, interesting, useful, noninteresting, debug
                        List shows a table of all available stats
                        Run <count> times (default forever),
                         once per <interval> seconds (default 1)
    

 Monitor commands: 
 =================
alerts send                                                                                        (re)send alerts immediately
auth add <entity> [<caps>...]                                                                      add auth info for <entity> from input file, or random key if no input is given, and/or any caps 
                                                                                                    specified in the command
auth caps <entity> <caps>...                                                                       update caps for <name> from caps specified in the command
auth export [<entity>]                                                                             write keyring for requested entity, or master keyring if none given
auth get <entity>                                                                                  write keyring file with requested key
auth get-key <entity>                                                                              display requested key
auth get-or-create <entity> [<caps>...]                                                            add auth info for <entity> from input file, or random key if no input given, and/or any caps 
                                                                                                    specified in the command
auth get-or-create-key <entity> [<caps>...]                                                        get, or add, key for <name> from system/caps pairs specified in the command.  If key already 
                                                                                                    exists, any given caps must match the existing caps for that key.
auth import                                                                                        auth import: read keyring file from -i <file>
auth ls                                                                                            list authentication state
auth print-key <entity>                                                                            display requested key
auth print_key <entity>                                                                            display requested key
auth rm <entity>                                                                                   remove all caps for <name>
balancer dump <plan>                                                                               Show an optimization plan
balancer eval [<option>]                                                                           Evaluate data distribution for the current cluster or specific pool or specific plan
balancer eval-verbose [<option>]                                                                   Evaluate data distribution for the current cluster or specific pool or specific plan (verbosely)
balancer execute <plan>                                                                            Execute an optimization plan
balancer ls                                                                                        List all plans
balancer mode none|crush-compat|upmap                                                              Set balancer mode
balancer off                                                                                       Disable automatic balancing
balancer on                                                                                        Enable automatic balancing
balancer optimize <plan> [<pools>...]                                                              Run optimizer to create a new plan
balancer pool add <pools>...                                                                       Enable automatic balancing for specific pools
balancer pool ls                                                                                   List automatic balancing pools. Note that empty list means all existing pools will be automatic 
                                                                                                    balancing targets, which is the default behaviour of balancer.
balancer pool rm <pools>...                                                                        Disable automatic balancing for specific pools
balancer reset                                                                                     Discard all optimization plans
balancer rm <plan>                                                                                 Discard an optimization plan
balancer show <plan>                                                                               Show details of an optimization plan
balancer status                                                                                    Show balancer status
cephadm check-host <host> [<addr>]                                                                 Check whether we can access and manage a remote host
cephadm clear-key                                                                                  Clear cluster SSH key
cephadm clear-ssh-config                                                                           Clear the ssh_config file
cephadm generate-key                                                                               Generate a cluster SSH key (if not present)
cephadm get-extra-ceph-conf                                                                        Get extra ceph conf that is appended
cephadm get-pub-key                                                                                Show SSH public key for connecting to cluster hosts
cephadm get-ssh-config                                                                             Returns the ssh config as used by cephadm
cephadm get-user                                                                                   Show user for SSHing to cluster hosts
cephadm prepare-host <host> [<addr>]                                                               Prepare a remote host for use with cephadm
cephadm registry-login [<url>] [<username>] [<password>]                                           Set custom registry login info by providing url, username and password or json file with login 
                                                                                                    info (-i <file>)
cephadm set-extra-ceph-conf                                                                        Text that is appended to all daemon's ceph.conf.
Mainly a workaround, till `config generate-
                                                                                                    minimal-conf` generates
a complete ceph.conf.

Warning: this is a dangerous operation.
cephadm set-priv-key                                                                               Set cluster SSH private key (use -i <private_key>)
cephadm set-pub-key                                                                                Set cluster SSH public key (use -i <public_key>)
cephadm set-ssh-config                                                                             Set the ssh_config file (use -i <ssh_config>)
cephadm set-user <user>                                                                            Set user for SSHing to cluster hosts, passwordless sudo will be needed for non-root users
config assimilate-conf                                                                             Assimilate options from a conf, and return a new, minimal conf file
config dump                                                                                        Show all configuration option(s)
config generate-minimal-conf                                                                       Generate a minimal ceph.conf file
config get <who> [<key>]                                                                           Show configuration option(s) for an entity
config help <key>                                                                                  Describe a configuration option
config log [<num:int>]                                                                             Show recent history of config changes
config ls                                                                                          List available configuration options
config reset <num:int>                                                                             Revert configuration to a historical version specified by <num>
config rm <who> <name>                                                                             Clear a configuration option for one or more entities
config set <who> <name> <value> [--force]                                                          Set a configuration option for one or more entities
config show <who> [<key>]                                                                          Show running configuration
config show-with-defaults <who>                                                                    Show running configuration (including compiled-in defaults)
config-key dump [<key>]                                                                            dump keys and values (with optional prefix)
config-key exists <key>                                                                            check for <key>'s existence
config-key get <key>                                                                               get <key>
config-key ls                                                                                      list keys
config-key rm <key>                                                                                rm <key>
config-key set <key> [<val>]                                                                       set <key> to value <val>
crash archive <id>                                                                                 Acknowledge a crash and silence health warning(s)
crash archive-all                                                                                  Acknowledge all new crashes and silence health warning(s)
crash info <id>                                                                                    show crash dump metadata
crash json_report <hours>                                                                          Crashes in the last <hours> hours
crash ls                                                                                           Show new and archived crash dumps
crash ls-new                                                                                       Show new crash dumps
crash post                                                                                         Add a crash dump (use -i <jsonfile>)
crash prune <keep>                                                                                 Remove crashes older than <keep> days
crash rm <id>                                                                                      Remove a saved crash <id>
crash stat                                                                                         Summarize recorded crashes
dashboard ac-role-add-scope-perms <rolename> <scopename> <permissions>...                          Add the scope permissions for a role
dashboard ac-role-create <rolename> [<description>]                                                Create a new access control role
dashboard ac-role-del-scope-perms <rolename> <scopename>                                           Delete the scope permissions for a role
dashboard ac-role-delete <rolename>                                                                Delete an access control role
dashboard ac-role-show [<rolename>]                                                                Show role info
dashboard ac-user-add-roles <username> <roles>...                                                  Add roles to user
dashboard ac-user-create <username> [<password>] [<rolename>] [<name>] [<email>] [--enabled] [--   Create a user
 force-password] [<pwd_expiration_date:int>] [--pwd-update-required]                               
dashboard ac-user-del-roles <username> <roles>...                                                  Delete roles from user
dashboard ac-user-delete <username>                                                                Delete user
dashboard ac-user-disable <username>                                                               Disable a user
dashboard ac-user-enable <username>                                                                Enable a user
dashboard ac-user-set-info <username> <name> <email>                                               Set user info
dashboard ac-user-set-password <username> <password> [--force-password]                            Set user password
dashboard ac-user-set-password-hash <username> <hashed_password>                                   Set user password bcrypt hash
dashboard ac-user-set-roles <username> <roles>...                                                  Set user roles
dashboard ac-user-show [<username>]                                                                Show user info
dashboard create-self-signed-cert                                                                  Create self signed certificate
dashboard debug enable|disable|status                                                              Control and report debug status in Ceph-Dashboard
dashboard feature enable|disable|status [rbd|mirroring|iscsi|cephfs|rgw|nfs...]                    Enable or disable features in Ceph-Mgr Dashboard
dashboard get-alertmanager-api-host                                                                Get the ALERTMANAGER_API_HOST option value
dashboard get-audit-api-enabled                                                                    Get the AUDIT_API_ENABLED option value
dashboard get-audit-api-log-payload                                                                Get the AUDIT_API_LOG_PAYLOAD option value
dashboard get-enable-browsable-api                                                                 Get the ENABLE_BROWSABLE_API option value
dashboard get-ganesha-clusters-rados-pool-namespace                                                Get the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option value
dashboard get-grafana-api-password                                                                 Get the GRAFANA_API_PASSWORD option value
dashboard get-grafana-api-ssl-verify                                                               Get the GRAFANA_API_SSL_VERIFY option value
dashboard get-grafana-api-url                                                                      Get the GRAFANA_API_URL option value
dashboard get-grafana-api-username                                                                 Get the GRAFANA_API_USERNAME option value
dashboard get-grafana-update-dashboards                                                            Get the GRAFANA_UPDATE_DASHBOARDS option value
dashboard get-iscsi-api-ssl-verification                                                           Get the ISCSI_API_SSL_VERIFICATION option value
dashboard get-jwt-token-ttl                                                                        Get the JWT token TTL in seconds
dashboard get-prometheus-api-host                                                                  Get the PROMETHEUS_API_HOST option value
dashboard get-pwd-policy-check-complexity-enabled                                                  Get the PWD_POLICY_CHECK_COMPLEXITY_ENABLED option value
dashboard get-pwd-policy-check-exclusion-list-enabled                                              Get the PWD_POLICY_CHECK_EXCLUSION_LIST_ENABLED option value
dashboard get-pwd-policy-check-length-enabled                                                      Get the PWD_POLICY_CHECK_LENGTH_ENABLED option value
dashboard get-pwd-policy-check-oldpwd-enabled                                                      Get the PWD_POLICY_CHECK_OLDPWD_ENABLED option value
dashboard get-pwd-policy-check-repetitive-chars-enabled                                            Get the PWD_POLICY_CHECK_REPETITIVE_CHARS_ENABLED option value
dashboard get-pwd-policy-check-sequential-chars-enabled                                            Get the PWD_POLICY_CHECK_SEQUENTIAL_CHARS_ENABLED option value
dashboard get-pwd-policy-check-username-enabled                                                    Get the PWD_POLICY_CHECK_USERNAME_ENABLED option value
dashboard get-pwd-policy-enabled                                                                   Get the PWD_POLICY_ENABLED option value
dashboard get-pwd-policy-exclusion-list                                                            Get the PWD_POLICY_EXCLUSION_LIST option value
dashboard get-pwd-policy-min-complexity                                                            Get the PWD_POLICY_MIN_COMPLEXITY option value
dashboard get-pwd-policy-min-length                                                                Get the PWD_POLICY_MIN_LENGTH option value
dashboard get-rest-requests-timeout                                                                Get the REST_REQUESTS_TIMEOUT option value
dashboard get-rgw-api-access-key                                                                   Get the RGW_API_ACCESS_KEY option value
dashboard get-rgw-api-admin-resource                                                               Get the RGW_API_ADMIN_RESOURCE option value
dashboard get-rgw-api-host                                                                         Get the RGW_API_HOST option value
dashboard get-rgw-api-port                                                                         Get the RGW_API_PORT option value
dashboard get-rgw-api-scheme                                                                       Get the RGW_API_SCHEME option value
dashboard get-rgw-api-secret-key                                                                   Get the RGW_API_SECRET_KEY option value
dashboard get-rgw-api-ssl-verify                                                                   Get the RGW_API_SSL_VERIFY option value
dashboard get-rgw-api-user-id                                                                      Get the RGW_API_USER_ID option value
dashboard get-user-pwd-expiration-span                                                             Get the USER_PWD_EXPIRATION_SPAN option value
dashboard get-user-pwd-expiration-warning-1                                                        Get the USER_PWD_EXPIRATION_WARNING_1 option value
dashboard get-user-pwd-expiration-warning-2                                                        Get the USER_PWD_EXPIRATION_WARNING_2 option value
dashboard grafana dashboards update                                                                Push dashboards to Grafana
dashboard iscsi-gateway-add <service_url> [<name>]                                                 Add iSCSI gateway configuration
dashboard iscsi-gateway-list                                                                       List iSCSI gateways
dashboard iscsi-gateway-rm <name>                                                                  Remove iSCSI gateway configuration
dashboard reset-alertmanager-api-host                                                              Reset the ALERTMANAGER_API_HOST option to its default value
dashboard reset-audit-api-enabled                                                                  Reset the AUDIT_API_ENABLED option to its default value
dashboard reset-audit-api-log-payload                                                              Reset the AUDIT_API_LOG_PAYLOAD option to its default value
dashboard reset-enable-browsable-api                                                               Reset the ENABLE_BROWSABLE_API option to its default value
dashboard reset-ganesha-clusters-rados-pool-namespace                                              Reset the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option to its default value
dashboard reset-grafana-api-password                                                               Reset the GRAFANA_API_PASSWORD option to its default value
dashboard reset-grafana-api-ssl-verify                                                             Reset the GRAFANA_API_SSL_VERIFY option to its default value
dashboard reset-grafana-api-url                                                                    Reset the GRAFANA_API_URL option to its default value
dashboard reset-grafana-api-username                                                               Reset the GRAFANA_API_USERNAME option to its default value
dashboard reset-grafana-update-dashboards                                                          Reset the GRAFANA_UPDATE_DASHBOARDS option to its default value
dashboard reset-iscsi-api-ssl-verification                                                         Reset the ISCSI_API_SSL_VERIFICATION option to its default value
dashboard reset-prometheus-api-host                                                                Reset the PROMETHEUS_API_HOST option to its default value
dashboard reset-pwd-policy-check-complexity-enabled                                                Reset the PWD_POLICY_CHECK_COMPLEXITY_ENABLED option to its default value
dashboard reset-pwd-policy-check-exclusion-list-enabled                                            Reset the PWD_POLICY_CHECK_EXCLUSION_LIST_ENABLED option to its default value
dashboard reset-pwd-policy-check-length-enabled                                                    Reset the PWD_POLICY_CHECK_LENGTH_ENABLED option to its default value
dashboard reset-pwd-policy-check-oldpwd-enabled                                                    Reset the PWD_POLICY_CHECK_OLDPWD_ENABLED option to its default value
dashboard reset-pwd-policy-check-repetitive-chars-enabled                                          Reset the PWD_POLICY_CHECK_REPETITIVE_CHARS_ENABLED option to its default value
dashboard reset-pwd-policy-check-sequential-chars-enabled                                          Reset the PWD_POLICY_CHECK_SEQUENTIAL_CHARS_ENABLED option to its default value
dashboard reset-pwd-policy-check-username-enabled                                                  Reset the PWD_POLICY_CHECK_USERNAME_ENABLED option to its default value
dashboard reset-pwd-policy-enabled                                                                 Reset the PWD_POLICY_ENABLED option to its default value
dashboard reset-pwd-policy-exclusion-list                                                          Reset the PWD_POLICY_EXCLUSION_LIST option to its default value
dashboard reset-pwd-policy-min-complexity                                                          Reset the PWD_POLICY_MIN_COMPLEXITY option to its default value
dashboard reset-pwd-policy-min-length                                                              Reset the PWD_POLICY_MIN_LENGTH option to its default value
dashboard reset-rest-requests-timeout                                                              Reset the REST_REQUESTS_TIMEOUT option to its default value
dashboard reset-rgw-api-access-key                                                                 Reset the RGW_API_ACCESS_KEY option to its default value
dashboard reset-rgw-api-admin-resource                                                             Reset the RGW_API_ADMIN_RESOURCE option to its default value
dashboard reset-rgw-api-host                                                                       Reset the RGW_API_HOST option to its default value
dashboard reset-rgw-api-port                                                                       Reset the RGW_API_PORT option to its default value
dashboard reset-rgw-api-scheme                                                                     Reset the RGW_API_SCHEME option to its default value
dashboard reset-rgw-api-secret-key                                                                 Reset the RGW_API_SECRET_KEY option to its default value
dashboard reset-rgw-api-ssl-verify                                                                 Reset the RGW_API_SSL_VERIFY option to its default value
dashboard reset-rgw-api-user-id                                                                    Reset the RGW_API_USER_ID option to its default value
dashboard reset-user-pwd-expiration-span                                                           Reset the USER_PWD_EXPIRATION_SPAN option to its default value
dashboard reset-user-pwd-expiration-warning-1                                                      Reset the USER_PWD_EXPIRATION_WARNING_1 option to its default value
dashboard reset-user-pwd-expiration-warning-2                                                      Reset the USER_PWD_EXPIRATION_WARNING_2 option to its default value
dashboard set-alertmanager-api-host <value>                                                        Set the ALERTMANAGER_API_HOST option value
dashboard set-audit-api-enabled <value>                                                            Set the AUDIT_API_ENABLED option value
dashboard set-audit-api-log-payload <value>                                                        Set the AUDIT_API_LOG_PAYLOAD option value
dashboard set-enable-browsable-api <value>                                                         Set the ENABLE_BROWSABLE_API option value
dashboard set-ganesha-clusters-rados-pool-namespace <value>                                        Set the GANESHA_CLUSTERS_RADOS_POOL_NAMESPACE option value
dashboard set-grafana-api-password <value>                                                         Set the GRAFANA_API_PASSWORD option value
dashboard set-grafana-api-ssl-verify <value>                                                       Set the GRAFANA_API_SSL_VERIFY option value
dashboard set-grafana-api-url <value>                                                              Set the GRAFANA_API_URL option value
dashboard set-grafana-api-username <value>                                                         Set the GRAFANA_API_USERNAME option value
dashboard set-grafana-update-dashboards <value>                                                    Set the GRAFANA_UPDATE_DASHBOARDS option value
dashboard set-iscsi-api-ssl-verification <value>                                                   Set the ISCSI_API_SSL_VERIFICATION option value
dashboard set-jwt-token-ttl <seconds:int>                                                          Set the JWT token TTL in seconds
dashboard set-login-credentials <username> <password>                                              Set the login credentials
dashboard set-prometheus-api-host <value>                                                          Set the PROMETHEUS_API_HOST option value
dashboard set-pwd-policy-check-complexity-enabled <value>                                          Set the PWD_POLICY_CHECK_COMPLEXITY_ENABLED option value
dashboard set-pwd-policy-check-exclusion-list-enabled <value>                                      Set the PWD_POLICY_CHECK_EXCLUSION_LIST_ENABLED option value
dashboard set-pwd-policy-check-length-enabled <value>                                              Set the PWD_POLICY_CHECK_LENGTH_ENABLED option value
dashboard set-pwd-policy-check-oldpwd-enabled <value>                                              Set the PWD_POLICY_CHECK_OLDPWD_ENABLED option value
dashboard set-pwd-policy-check-repetitive-chars-enabled <value>                                    Set the PWD_POLICY_CHECK_REPETITIVE_CHARS_ENABLED option value
dashboard set-pwd-policy-check-sequential-chars-enabled <value>                                    Set the PWD_POLICY_CHECK_SEQUENTIAL_CHARS_ENABLED option value
dashboard set-pwd-policy-check-username-enabled <value>                                            Set the PWD_POLICY_CHECK_USERNAME_ENABLED option value
dashboard set-pwd-policy-enabled <value>                                                           Set the PWD_POLICY_ENABLED option value
dashboard set-pwd-policy-exclusion-list <value>                                                    Set the PWD_POLICY_EXCLUSION_LIST option value
dashboard set-pwd-policy-min-complexity <value:int>                                                Set the PWD_POLICY_MIN_COMPLEXITY option value
dashboard set-pwd-policy-min-length <value:int>                                                    Set the PWD_POLICY_MIN_LENGTH option value
dashboard set-rest-requests-timeout <value:int>                                                    Set the REST_REQUESTS_TIMEOUT option value
dashboard set-rgw-api-access-key <value>                                                           Set the RGW_API_ACCESS_KEY option value
dashboard set-rgw-api-admin-resource <value>                                                       Set the RGW_API_ADMIN_RESOURCE option value
dashboard set-rgw-api-host <value>                                                                 Set the RGW_API_HOST option value
dashboard set-rgw-api-port <value:int>                                                             Set the RGW_API_PORT option value
dashboard set-rgw-api-scheme <value>                                                               Set the RGW_API_SCHEME option value
dashboard set-rgw-api-secret-key <value>                                                           Set the RGW_API_SECRET_KEY option value
dashboard set-rgw-api-ssl-verify <value>                                                           Set the RGW_API_SSL_VERIFY option value
dashboard set-rgw-api-user-id <value>                                                              Set the RGW_API_USER_ID option value
dashboard set-user-pwd-expiration-span <value:int>                                                 Set the USER_PWD_EXPIRATION_SPAN option value
dashboard set-user-pwd-expiration-warning-1 <value:int>                                            Set the USER_PWD_EXPIRATION_WARNING_1 option value
dashboard set-user-pwd-expiration-warning-2 <value:int>                                            Set the USER_PWD_EXPIRATION_WARNING_2 option value
dashboard sso disable                                                                              Disable Single Sign-On
dashboard sso enable saml2                                                                         Enable SAML2 Single Sign-On
dashboard sso setup saml2 <ceph_dashboard_base_url> <idp_metadata> [<idp_username_attribute>]      Setup SAML2 Single Sign-On
 [<idp_entity_id>] [<sp_x_509_cert>] [<sp_private_key>]                                            
dashboard sso show saml2                                                                           Show SAML2 configuration
dashboard sso status                                                                               Get Single Sign-On status
device check-health                                                                                Check life expectancy of devices
device get-health-metrics <devid> [<sample>]                                                       Show stored device metrics for the device
device info <devid>                                                                                Show information about a device
device light on|off <devid> [ident|fault] [--force]                                                Enable or disable the device light. Default type is `ident`
Usage: device light (on|off) <devid> 
                                                                                                    [ident|fault] [--force]
device ls                                                                                          Show devices
device ls-by-daemon <who>                                                                          Show devices associated with a daemon
device ls-by-host <host>                                                                           Show devices on a host
device ls-lights                                                                                   List currently active device indicator lights
device monitoring off                                                                              Disable device health monitoring
device monitoring on                                                                               Enable device health monitoring
device predict-life-expectancy <devid>                                                             Predict life expectancy with local predictor
device query-daemon-health-metrics <who>                                                           Get device health metrics for a given daemon
device rm-life-expectancy <devid>                                                                  Clear predicted device life expectancy
device scrape-daemon-health-metrics <who>                                                          Scrape and store device health metrics for a given daemon
device scrape-health-metrics [<devid>]                                                             Scrape and store health metrics
device set-life-expectancy <devid> <from> [<to>]                                                   Set predicted device life expectancy
df [detail]                                                                                        show cluster free space stats
features                                                                                           report of connected features
fs add_data_pool <fs_name> <pool>                                                                  add data pool <pool>
fs authorize <filesystem> <entity> <caps>...                                                       add auth for <entity> to access file system <filesystem> based on following directory and 
                                                                                                    permissions pairs
fs clone cancel <vol_name> <clone_name> [<group_name>]                                             Cancel an pending or ongoing clone operation.
fs clone status <vol_name> <clone_name> [<group_name>]                                             Get status on a cloned subvolume.
fs dump [<epoch:int>]                                                                              dump all CephFS status, optionally from epoch
fs fail <fs_name>                                                                                  bring the file system down and all of its ranks
fs flag set enable_multiple <val> [--yes-i-really-mean-it]                                         Set a global CephFS flag
fs get <fs_name>                                                                                   get info about one filesystem
fs ls                                                                                              list filesystems
fs new <fs_name> <metadata> <data> [--force] [--allow-dangerous-metadata-overlay]                  make new filesystem using named pools <metadata> and <data>
fs reset <fs_name> [--yes-i-really-mean-it]                                                        disaster recovery only: reset to a single-MDS map
fs rm <fs_name> [--yes-i-really-mean-it]                                                           disable the named filesystem
fs rm_data_pool <fs_name> <pool>                                                                   remove data pool <pool>
fs set <fs_name> max_mds|max_file_size|allow_new_snaps|inline_data|cluster_down|allow_dirfrags|    set fs parameter <var> to <val>
 balancer|standby_count_wanted|session_timeout|session_autoclose|allow_standby_replay|down|        
 joinable|min_compat_client <val> [--yes-i-really-mean-it] [--yes-i-really-really-mean-it]         
fs set-default <fs_name>                                                                           set the default to the named filesystem
fs status [<fs>]                                                                                   Show the status of a CephFS filesystem
fs subvolume create <vol_name> <sub_name> [<size:int>] [<group_name>] [<pool_layout>] [<uid:int>]  Create a CephFS subvolume in a volume, and optionally, with a specific size (in bytes), a specific 
 [<gid:int>] [<mode>] [--namespace-isolated]                                                        data pool layout, a specific mode, in a specific subvolume group and in separate RADOS namespace
fs subvolume getpath <vol_name> <sub_name> [<group_name>]                                          Get the mountpath of a CephFS subvolume in a volume, and optionally, in a specific subvolume group
fs subvolume info <vol_name> <sub_name> [<group_name>]                                             Get the metadata of a CephFS subvolume in a volume, and optionally, in a specific subvolume group
fs subvolume ls <vol_name> [<group_name>]                                                          List subvolumes
fs subvolume pin <vol_name> <sub_name> export|distributed|random <pin_setting> [<group_name>]      Set MDS pinning policy for subvolume
fs subvolume resize <vol_name> <sub_name> <new_size> [<group_name>] [--no-shrink]                  Resize a CephFS subvolume
fs subvolume rm <vol_name> <sub_name> [<group_name>] [--force]                                     Delete a CephFS subvolume in a volume, and optionally, in a specific subvolume group
fs subvolume snapshot clone <vol_name> <sub_name> <snap_name> <target_sub_name> [<pool_layout>]    Clone a snapshot to target subvolume
 [<group_name>] [<target_group_name>]                                                              
fs subvolume snapshot create <vol_name> <sub_name> <snap_name> [<group_name>]                      Create a snapshot of a CephFS subvolume in a volume, and optionally, in a specific subvolume group
fs subvolume snapshot info <vol_name> <sub_name> <snap_name> [<group_name>]                        Get the metadata of a CephFS subvolume snapshot and optionally, in a specific subvolume group
fs subvolume snapshot ls <vol_name> <sub_name> [<group_name>]                                      List subvolume snapshots
fs subvolume snapshot protect <vol_name> <sub_name> <snap_name> [<group_name>]                     (deprecated) Protect snapshot of a CephFS subvolume in a volume, and optionally, in a specific 
                                                                                                    subvolume group
fs subvolume snapshot rm <vol_name> <sub_name> <snap_name> [<group_name>] [--force]                Delete a snapshot of a CephFS subvolume in a volume, and optionally, in a specific subvolume group
fs subvolume snapshot unprotect <vol_name> <sub_name> <snap_name> [<group_name>]                   (deprecated) Unprotect a snapshot of a CephFS subvolume in a volume, and optionally, in a specific 
                                                                                                    subvolume group
fs subvolumegroup create <vol_name> <group_name> [<pool_layout>] [<uid:int>] [<gid:int>] [<mode>]  Create a CephFS subvolume group in a volume, and optionally, with a specific data pool layout, and 
                                                                                                    a specific numeric mode
fs subvolumegroup getpath <vol_name> <group_name>                                                  Get the mountpath of a CephFS subvolume group in a volume
fs subvolumegroup ls <vol_name>                                                                    List subvolumegroups
fs subvolumegroup pin <vol_name> <group_name> export|distributed|random <pin_setting>              Set MDS pinning policy for subvolumegroup
fs subvolumegroup rm <vol_name> <group_name> [--force]                                             Delete a CephFS subvolume group in a volume
fs subvolumegroup snapshot create <vol_name> <group_name> <snap_name>                              Create a snapshot of a CephFS subvolume group in a volume
fs subvolumegroup snapshot ls <vol_name> <group_name>                                              List subvolumegroup snapshots
fs subvolumegroup snapshot rm <vol_name> <group_name> <snap_name> [--force]                        Delete a snapshot of a CephFS subvolume group in a volume
fs volume create <name> [<placement>]                                                              Create a CephFS volume
fs volume ls                                                                                       List volumes
fs volume rm <vol_name> [<yes-i-really-mean-it>]                                                   Delete a FS volume by passing --yes-i-really-mean-it flag
fsid                                                                                               show cluster FSID/UUID
health [detail]                                                                                    show cluster health
health mute <code> [<ttl>] [--sticky]                                                              mute health alert
health unmute [<code>]                                                                             unmute existing health alert mute(s)
influx config-set <key> <value>                                                                    Set a configuration value
influx config-show                                                                                 Show current configuration
influx send                                                                                        Force sending data to Influx
insights                                                                                           Retrieve insights report
insights prune-health <hours>                                                                      Remove health history older than <hours> hours
iostat                                                                                             Get IO rates
k8sevents ceph                                                                                     List Ceph events tracked & sent to the kubernetes cluster
k8sevents clear-config                                                                             Clear external kubernetes configuration settings
k8sevents ls                                                                                       List all current Kuberenetes events from the Ceph namespace
k8sevents set-access <key>                                                                         Set kubernetes access credentials. <key> must be cacrt or token and use -i <filename> syntax.
e.g. 
                                                                                                    ceph k8sevents set-access cacrt -i /root/ca.crt
k8sevents set-config <key> <value>                                                                 Set kubernetes config paramters. <key> must be server or namespace.
e.g. ceph k8sevents set-config 
                                                                                                    server https://localhost:30433
k8sevents status                                                                                   Show the status of the data gathering threads
log <logtext>...                                                                                   log supplied text to the monitor log
log last [<num:int>] [debug|info|sec|warn|error] [*|cluster|audit|cephadm]                         print last few lines of the cluster log
mds compat rm_compat <feature:int>                                                                 remove compatible feature
mds compat rm_incompat <feature:int>                                                               remove incompatible feature
mds compat show                                                                                    show mds compatibility settings
mds count-metadata <property>                                                                      count MDSs by metadata field property
mds fail <role_or_gid>                                                                             Mark MDS failed: trigger a failover if a standby is available
mds metadata [<who>]                                                                               fetch metadata for mds <role>
mds ok-to-stop <ids>...                                                                            check whether stopping the specified MDS would reduce immediate availability
mds repaired <role>                                                                                mark a damaged MDS rank as no longer damaged
mds rm <gid:int>                                                                                   remove nonactive mds
mds versions                                                                                       check running versions of MDSs
mgr count-metadata <property>                                                                      count ceph-mgr daemons by metadata field property
mgr dump [<epoch:int>]                                                                             dump the latest MgrMap
mgr fail [<who>]                                                                                   treat the named manager daemon as failed
mgr metadata [<who>]                                                                               dump metadata for all daemons or a specific daemon
mgr module disable <module>                                                                        disable mgr module
mgr module enable <module> [--force]                                                               enable mgr module
mgr module ls                                                                                      list active mgr modules
mgr self-test background start <workload>                                                          Activate a background workload (one of command_spam, throw_exception)
mgr self-test background stop                                                                      Stop background workload if any is running
mgr self-test cluster-log <channel> <priority> <message>                                           Create an audit log record.
mgr self-test config get <key>                                                                     Peek at a configuration value
mgr self-test config get_localized <key>                                                           Peek at a configuration value (localized variant)
mgr self-test health clear [<checks>...]                                                           Clear health checks by name. If no names provided, clear all.
mgr self-test health set <checks>                                                                  Set a health check from a JSON-formatted description.
mgr self-test insights_set_now_offset <hours>                                                      Set the now time for the insights module.
mgr self-test module <module>                                                                      Run another module's self_test() method
mgr self-test remote                                                                               Test inter-module calls
mgr self-test run                                                                                  Run mgr python interface tests
mgr services                                                                                       list service endpoints provided by mgr modules
mgr versions                                                                                       check running versions of ceph-mgr daemons
mon add <name> <addr>                                                                              add new monitor named <name> at <addr>
mon count-metadata <property>                                                                      count mons by metadata field property
mon dump [<epoch:int>]                                                                             dump formatted monmap (optionally from epoch)
mon enable-msgr2                                                                                   enable the msgr2 protocol on port 3300
mon feature ls [--with-value]                                                                      list available mon map features to be set/unset
mon feature set <feature_name> [--yes-i-really-mean-it]                                            set provided feature on mon map
mon getmap [<epoch:int>]                                                                           get monmap
mon metadata [<id>]                                                                                fetch metadata for mon <id>
mon ok-to-add-offline                                                                              check whether adding a mon and not starting it would break quorum
mon ok-to-rm <id>                                                                                  check whether removing the specified mon would break quorum
mon ok-to-stop <ids>...                                                                            check whether mon(s) can be safely stopped without reducing immediate availability
mon rm <name>                                                                                      remove monitor named <name>
mon scrub                                                                                          scrub the monitor stores
mon set-addrs <name> <addrs>                                                                       set the addrs (IPs and ports) a specific monitor binds to
mon set-rank <name> <rank:int>                                                                     set the rank for the specified mon
mon set-weight <name> <weight:int>                                                                 set the weight for the specified mon
mon stat                                                                                           summarize monitor status
mon versions                                                                                       check running versions of monitors
nfs cluster config reset <clusterid>                                                               Reset NFS-Ganesha Config to default
nfs cluster config set <clusterid>                                                                 Set NFS-Ganesha config by `-i <config_file>`
nfs cluster create <type> <clusterid> [<placement>]                                                Create an NFS Cluster
nfs cluster delete <clusterid>                                                                     Deletes an NFS Cluster
nfs cluster info [<clusterid>]                                                                     Displays NFS Cluster info
nfs cluster ls                                                                                     List NFS Clusters
nfs cluster update <clusterid> <placement>                                                         Updates an NFS Cluster
nfs export create cephfs <fsname> <clusterid> <binding> [--readonly] [<path>]                      Create a cephfs export
nfs export delete <clusterid> <binding>                                                            Delete a cephfs export
nfs export get <clusterid> <binding>                                                               Fetch a export of a NFS cluster given the pseudo path/binding
nfs export ls <clusterid> [--detailed]                                                             List exports of a NFS cluster
node ls [all|osd|mon|mds|mgr]                                                                      list all nodes in cluster [type]
orch apply [mon|mgr|rbd-mirror|crash|alertmanager|grafana|node-exporter|prometheus] [<placement>]  Update the size or placement for a service or apply a large yaml spec
 [--dry-run] [plain|json|json-pretty|yaml] [--unmanaged]                                           
orch apply iscsi <pool> <api_user> <api_password> [<trusted_ip_list>] [<placement>] [--dry-run]    Scale an iSCSI service
 [plain|json|json-pretty|yaml] [--unmanaged]                                                       
orch apply mds <fs_name> [<placement>] [--dry-run] [--unmanaged] [plain|json|json-pretty|yaml]     Update the number of MDS instances for the given fs_name
orch apply nfs <svc_id> <pool> [<namespace>] [<placement>] [--dry-run] [plain|json|json-pretty|    Scale an NFS service
 yaml] [--unmanaged]                                                                               
orch apply osd [--all-available-devices] [--dry-run] [--unmanaged] [plain|json|json-pretty|yaml]   Create OSD daemon(s) using a drive group spec
orch apply rgw <realm_name> <zone_name> [<subcluster>] [<port:int>] [--ssl] [<placement>] [--dry-  Update the number of RGW instances for the given zone
 run] [plain|json|json-pretty|yaml] [--unmanaged]                                                  
orch cancel                                                                                        cancels ongoing operations
orch daemon add [mon|mgr|rbd-mirror|crash|alertmanager|grafana|node-exporter|prometheus]           Add daemon(s)
 [<placement>]                                                                                     
orch daemon add iscsi <pool> <api_user> <api_password> [<trusted_ip_list>] [<placement>]           Start iscsi daemon(s)
orch daemon add mds <fs_name> [<placement>]                                                        Start MDS daemon(s)
orch daemon add nfs <svc_id> <pool> [<namespace>] [<placement>]                                    Start NFS daemon(s)
orch daemon add osd [<svc_arg>]                                                                    Create an OSD service. Either --svc_arg=host:drives
orch daemon add rgw <realm_name> <zone_name> [<subcluster>] [<port:int>] [--ssl] [<placement>]     Start RGW daemon(s)
orch daemon redeploy <name> [<image>]                                                              Redeploy a daemon (with a specifc image)
orch daemon rm <names>... [--force]                                                                Remove specific daemon(s)
orch daemon start|stop|restart|reconfig <name>                                                     Start, stop, restart, (redeploy,) or reconfig a specific daemon
orch device ls [<hostname>...] [plain|json|json-pretty|yaml] [--refresh] [--wide]                  List devices on a host
orch device zap <hostname> <path> [--force]                                                        Zap (erase!) a device so it can be re-used
orch host add <hostname> [<addr>] [<labels>...]                                                    Add a host
orch host label add <hostname> <label>                                                             Add a host label
orch host label rm <hostname> <label>                                                              Remove a host label
orch host ls [plain|json|json-pretty|yaml]                                                         List hosts
orch host ok-to-stop <hostname>                                                                    Check if the specified host can be safely stopped without reducing availability
orch host rm <hostname>                                                                            Remove a host
orch host set-addr <hostname> <addr>                                                               Update a host address
orch ls [<service_type>] [<service_name>] [--export] [plain|json|json-pretty|yaml] [--refresh]     List services known to orchestrator
orch osd rm <svc_id>... [--replace] [--force]                                                      Remove OSD services
orch osd rm status [plain|json|json-pretty|yaml]                                                   status of OSD removal operation
orch osd rm stop <svc_id>...                                                                       Remove OSD services
orch pause                                                                                         Pause orchestrator background work
orch ps [<hostname>] [<service_name>] [<daemon_type>] [<daemon_id>] [plain|json|json-pretty|yaml]  List daemons known to orchestrator
 [--refresh]                                                                                       
orch resume                                                                                        Resume orchestrator background work (if paused)
orch rm <service_name> [--force]                                                                   Remove a service
orch set backend <module_name>                                                                     Select orchestrator module backend
orch start|stop|restart|redeploy|reconfig <service_name>                                           Start, stop, restart, redeploy, or reconfig an entire service (i.e. all daemons)
orch status [plain|json|json-pretty|yaml]                                                          Report configured backend and its status
orch upgrade check [<image>] [<ceph_version>]                                                      Check service versions vs available and target containers
orch upgrade pause                                                                                 Pause an in-progress upgrade
orch upgrade resume                                                                                Resume paused upgrade
orch upgrade start [<image>] [<ceph_version>]                                                      Initiate upgrade
orch upgrade status                                                                                Check service versions vs available and target containers
orch upgrade stop                                                                                  Stop an in-progress upgrade
osd blacklist add|rm <addr> [<expire:float>]                                                       add (optionally until <expire> seconds from now) or remove <addr> from blacklist
osd blacklist clear                                                                                clear all blacklisted clients
osd blacklist ls                                                                                   show blacklisted clients
osd blocked-by                                                                                     print histogram of which OSDs are blocking their peers
osd count-metadata <property>                                                                      count OSDs by metadata field property
osd crush add <id|osd.id> <weight:float> <args>...                                                 add or update crushmap position and weight for <name> with <weight> and location <args>
osd crush add-bucket <name> <type> [<args>...]                                                     add no-parent (probably root) crush bucket <name> of type <type> to location <args>
osd crush class create <class>                                                                     create crush device class <class>
osd crush class ls                                                                                 list all crush device classes
osd crush class ls-osd <class>                                                                     list all osds belonging to the specific <class>
osd crush class rename <srcname> <dstname>                                                         rename crush device class <srcname> to <dstname>
osd crush class rm <class>                                                                         remove crush device class <class>
osd crush create-or-move <id|osd.id> <weight:float> <args>...                                      create entry or move existing entry for <name> <weight> at/to location <args>
osd crush dump                                                                                     dump crush map
osd crush get-device-class <ids>...                                                                get classes of specified osd(s) <id> [<id>...]
osd crush get-tunable straw_calc_version                                                           get crush tunable <tunable>
osd crush link <name> <args>...                                                                    link existing entry for <name> under location <args>
osd crush ls <node>                                                                                list items beneath a node in the CRUSH tree
osd crush move <name> <args>...                                                                    move existing entry for <name> to location <args>
osd crush rename-bucket <srcname> <dstname>                                                        rename bucket <srcname> to <dstname>
osd crush reweight <name> <weight:float>                                                           change <name>'s weight to <weight> in crush map
osd crush reweight-all                                                                             recalculate the weights for the tree to ensure they sum correctly
osd crush reweight-subtree <name> <weight:float>                                                   change all leaf items beneath <name> to <weight> in crush map
osd crush rm <name> [<ancestor>]                                                                   remove <name> from crush map (everywhere, or just at <ancestor>)
osd crush rm-device-class <ids>...                                                                 remove class of the osd(s) <id> [<id>...],or use <all|any> to remove all.
osd crush rule create-erasure <name> [<profile>]                                                   create crush rule <name> for erasure coded pool created with <profile> (default default)
osd crush rule create-replicated <name> <root> <type> [<class>]                                    create crush rule <name> for replicated pool to start from <root>, replicate across buckets of 
                                                                                                    type <type>, use devices of type <class> (ssd or hdd)
osd crush rule create-simple <name> <root> <type> [firstn|indep]                                   create crush rule <name> to start from <root>, replicate across buckets of type <type>, using a 
                                                                                                    choose mode of <firstn|indep> (default firstn; indep best for erasure pools)
osd crush rule dump [<name>]                                                                       dump crush rule <name> (default all)
osd crush rule ls                                                                                  list crush rules
osd crush rule ls-by-class <class>                                                                 list all crush rules that reference the same <class>
osd crush rule rename <srcname> <dstname>                                                          rename crush rule <srcname> to <dstname>
osd crush rule rm <name>                                                                           remove crush rule <name>
osd crush set <id|osd.id> <weight:float> <args>...                                                 update crushmap position and weight for <name> to <weight> with location <args>
osd crush set [<prior_version:int>]                                                                set crush map from input file
osd crush set-all-straw-buckets-to-straw2                                                          convert all CRUSH current straw buckets to use the straw2 algorithm
osd crush set-device-class <class> <ids>...                                                        set the <class> of the osd(s) <id> [<id>...],or use <all|any> to set all.
osd crush set-tunable straw_calc_version <value:int>                                               set crush tunable <tunable> to <value>
osd crush show-tunables                                                                            show current crush tunables
osd crush swap-bucket <source> <dest> [--yes-i-really-mean-it]                                     swap existing bucket contents from (orphan) bucket <source> and <target>
osd crush tree [--show-shadow]                                                                     dump crush buckets and items in a tree view
osd crush tunables legacy|argonaut|bobtail|firefly|hammer|jewel|optimal|default                    set crush tunables values to <profile>
osd crush unlink <name> [<ancestor>]                                                               unlink <name> from crush map (everywhere, or just at <ancestor>)
osd crush weight-set create <pool> flat|positional                                                 create a weight-set for a given pool
osd crush weight-set create-compat                                                                 create a default backward-compatible weight-set
osd crush weight-set dump                                                                          dump crush weight sets
osd crush weight-set ls                                                                            list crush weight sets
osd crush weight-set reweight <pool> <item> <weight:float>...                                      set weight for an item (bucket or osd) in a pool's weight-set
osd crush weight-set reweight-compat <item> <weight:float>...                                      set weight for an item (bucket or osd) in the backward-compatible weight-set
osd crush weight-set rm <pool>                                                                     remove the weight-set for a given pool
osd crush weight-set rm-compat                                                                     remove the backward-compatible weight-set
osd deep-scrub <who>                                                                               initiate deep scrub on osd <who>, or use <all|any> to deep scrub all
osd destroy <id|osd.id> [--force] [--yes-i-really-mean-it]                                         mark osd as being destroyed. Keeps the ID intact (allowing reuse), but removes cephx keys, config-
                                                                                                    key data and lockbox keys, rendering data permanently unreadable.
osd df [plain|tree] [class|name] [<filter>]                                                        show OSD utilization
osd down <ids>... [--definitely-dead]                                                              set osd(s) <id> [<id>...] down, or use <any|all> to set all osds down
osd dump [<epoch:int>]                                                                             print summary of OSD map
osd erasure-code-profile get <name>                                                                get erasure code profile <name>
osd erasure-code-profile ls                                                                        list all erasure code profiles
osd erasure-code-profile rm <name>                                                                 remove erasure code profile <name>
osd erasure-code-profile set <name> [<profile>...] [--force]                                       create erasure code profile <name> with [<key[=value]> ...] pairs. Add a --force at the end to 
                                                                                                    override an existing profile (VERY DANGEROUS)
osd find <id|osd.id>                                                                               find osd <id> in the CRUSH map and show its location
osd force-create-pg <pgid> [--yes-i-really-mean-it]                                                force creation of pg <pgid>
osd get-require-min-compat-client                                                                  get the minimum client version we will maintain compatibility with
osd getcrushmap [<epoch:int>]                                                                      get CRUSH map
osd getmap [<epoch:int>]                                                                           get OSD map
osd getmaxosd                                                                                      show largest OSD id
osd in <ids>...                                                                                    set osd(s) <id> [<id>...] in, can use <any|all> to automatically set all previously out osds in
osd info [<id|osd.id>]                                                                             print osd's {id} information (instead of all osds from map)
osd last-stat-seq <id|osd.id>                                                                      get the last pg stats sequence number reported for this osd
osd lost <id|osd.id> [--yes-i-really-mean-it]                                                      mark osd as permanently lost. THIS DESTROYS DATA IF NO MORE REPLICAS EXIST, BE CAREFUL
osd ls [<epoch:int>]                                                                               show all OSD ids
osd ls-tree [<epoch:int>] <name>                                                                   show OSD ids under bucket <name> in the CRUSH map
osd map <pool> <object> [<nspace>]                                                                 find pg for <object> in <pool> with [namespace]
osd metadata [<id|osd.id>]                                                                         fetch metadata for osd {id} (default all)
osd new <uuid> [<id|osd.id>]                                                                       Create a new OSD. If supplied, the `id` to be replaced needs to exist and have been previously 
                                                                                                    destroyed. Reads secrets from JSON file via `-i <file>` (see man page).
osd numa-status                                                                                    show NUMA status of OSDs
osd ok-to-stop <ids>...                                                                            check whether osd(s) can be safely stopped without reducing immediate data availability
osd out <ids>...                                                                                   set osd(s) <id> [<id>...] out, or use <any|all> to set all osds out
osd pause                                                                                          pause osd
osd perf                                                                                           print dump of OSD perf summary stats
osd pg-temp <pgid> [<id|osd.id>...]                                                                set pg_temp mapping pgid:[<id> [<id>...]] (developers only)
osd pg-upmap <pgid> <id|osd.id>...                                                                 set pg_upmap mapping <pgid>:[<id> [<id>...]] (developers only)
osd pg-upmap-items <pgid> <id|osd.id>...                                                           set pg_upmap_items mapping <pgid>:{<id> to <id>, [...]} (developers only)
osd pool application disable <pool> <app> [--yes-i-really-mean-it]                                 disables use of an application <app> on pool <poolname>
osd pool application enable <pool> <app> [--yes-i-really-mean-it]                                  enable use of an application <app> [cephfs,rbd,rgw] on pool <poolname>
osd pool application get [<pool>] [<app>] [<key>]                                                  get value of key <key> of application <app> on pool <poolname>
osd pool application rm <pool> <app> <key>                                                         removes application <app> metadata key <key> on pool <poolname>
osd pool application set <pool> <app> <key> <value>                                                sets application <app> metadata key <key> to <value> on pool <poolname>
osd pool autoscale-status                                                                          report on pool pg_num sizing recommendation and intent
osd pool cancel-force-backfill <who>...                                                            restore normal recovery priority of specified pool <who>
osd pool cancel-force-recovery <who>...                                                            restore normal recovery priority of specified pool <who>
osd pool create <pool> [<pg_num:int>] [<pgp_num:int>] [replicated|erasure] [<erasure_code_         create pool
 profile>] [<rule>] [<expected_num_objects:int>] [<size:int>] [<pg_num_min:int>] [on|off|warn]     
 [<target_size_bytes:int>] [<target_size_ratio:float>]                                             
osd pool deep-scrub <who>...                                                                       initiate deep-scrub on pool <who>
osd pool force-backfill <who>...                                                                   force backfill of specified pool <who> first
osd pool force-recovery <who>...                                                                   force recovery of specified pool <who> first
osd pool get <pool> size|min_size|pg_num|pgp_num|crush_rule|hashpspool|nodelete|nopgchange|        get pool parameter <var>
 nosizechange|write_fadvise_dontneed|noscrub|nodeep-scrub|hit_set_type|hit_set_period|hit_set_     
 count|hit_set_fpp|use_gmt_hitset|target_max_objects|target_max_bytes|cache_target_dirty_ratio|    
 cache_target_dirty_high_ratio|cache_target_full_ratio|cache_min_flush_age|cache_min_evict_age|    
 erasure_code_profile|min_read_recency_for_promote|all|min_write_recency_for_promote|fast_read|    
 hit_set_grade_decay_rate|hit_set_search_last_n|scrub_min_interval|scrub_max_interval|deep_scrub_  
 interval|recovery_priority|recovery_op_priority|scrub_priority|compression_mode|compression_      
 algorithm|compression_required_ratio|compression_max_blob_size|compression_min_blob_size|csum_    
 type|csum_min_block|csum_max_block|allow_ec_overwrites|fingerprint_algorithm|pg_autoscale_mode|   
 pg_autoscale_bias|pg_num_min|target_size_bytes|target_size_ratio                                  
osd pool get-quota <pool>                                                                          obtain object or byte limits for pool
osd pool ls [detail]                                                                               list pools
osd pool mksnap <pool> <snap>                                                                      make snapshot <snap> in <pool>
osd pool rename <srcpool> <destpool>                                                               rename <srcpool> to <destpool>
osd pool repair <who>...                                                                           initiate repair on pool <who>
osd pool rm <pool> [<pool2>] [--yes-i-really-really-mean-it] [--yes-i-really-really-mean-it-not-   remove pool
 faking]                                                                                           
osd pool rmsnap <pool> <snap>                                                                      remove snapshot <snap> from <pool>
osd pool scrub <who>...                                                                            initiate scrub on pool <who>
osd pool set <pool> size|min_size|pg_num|pgp_num|pgp_num_actual|crush_rule|hashpspool|nodelete|    set pool parameter <var> to <val>
 nopgchange|nosizechange|write_fadvise_dontneed|noscrub|nodeep-scrub|hit_set_type|hit_set_period|  
 hit_set_count|hit_set_fpp|use_gmt_hitset|target_max_bytes|target_max_objects|cache_target_dirty_  
 ratio|cache_target_dirty_high_ratio|cache_target_full_ratio|cache_min_flush_age|cache_min_evict_  
 age|min_read_recency_for_promote|min_write_recency_for_promote|fast_read|hit_set_grade_decay_     
 rate|hit_set_search_last_n|scrub_min_interval|scrub_max_interval|deep_scrub_interval|recovery_    
 priority|recovery_op_priority|scrub_priority|compression_mode|compression_algorithm|compression_  
 required_ratio|compression_max_blob_size|compression_min_blob_size|csum_type|csum_min_block|csum_ 
 max_block|allow_ec_overwrites|fingerprint_algorithm|pg_autoscale_mode|pg_autoscale_bias|pg_num_   
 min|target_size_bytes|target_size_ratio <val> [--yes-i-really-mean-it]                            
osd pool set-quota <pool> max_objects|max_bytes <val>                                              set object or byte limit on pool
osd pool stats [<pool_name>]                                                                       obtain stats from all pools, or from specified pool
osd primary-affinity <id|osd.id> <weight:float>                                                    adjust osd primary-affinity from 0.0 <= <weight> <= 1.0
osd primary-temp <pgid> <id|osd.id>                                                                set primary_temp mapping pgid:<id>|-1 (developers only)
osd purge <id|osd.id> [--force] [--yes-i-really-mean-it]                                           purge all osd data from the monitors including the OSD id and CRUSH position
osd purge-new <id|osd.id> [--yes-i-really-mean-it]                                                 purge all traces of an OSD that was partially created but never started
osd repair <who>                                                                                   initiate repair on osd <who>, or use <all|any> to repair all
osd require-osd-release luminous|mimic|nautilus|octopus [--yes-i-really-mean-it]                   set the minimum allowed OSD release to participate in the cluster
osd reweight <id|osd.id> <weight:float>                                                            reweight osd to 0.0 < <weight> < 1.0
osd reweight-by-pg [<oload:int>] [<max_change:float>] [<max_osds:int>] [<pools>...]                reweight OSDs by PG distribution [overload-percentage-for-consideration, default 120]
osd reweight-by-utilization [<oload:int>] [<max_change:float>] [<max_osds:int>] [--no-increasing]  reweight OSDs by utilization [overload-percentage-for-consideration, default 120]
osd reweightn <weights>                                                                            reweight osds with {<id>: <weight>,...})
osd rm-pg-upmap <pgid>                                                                             clear pg_upmap mapping for <pgid> (developers only)
osd rm-pg-upmap-items <pgid>                                                                       clear pg_upmap_items mapping for <pgid> (developers only)
osd safe-to-destroy <ids>...                                                                       check whether osd(s) can be safely destroyed without reducing data durability
osd scrub <who>                                                                                    initiate scrub on osd <who>, or use <all|any> to scrub all
osd set full|pause|noup|nodown|noout|noin|nobackfill|norebalance|norecover|noscrub|nodeep-scrub|   set <key>
 notieragent|nosnaptrim|pglog_hardlimit [--yes-i-really-mean-it]                                   
osd set-backfillfull-ratio <ratio:float>                                                           set usage ratio at which OSDs are marked too full to backfill
osd set-full-ratio <ratio:float>                                                                   set usage ratio at which OSDs are marked full
osd set-group <flags> <who>...                                                                     set <flags> for batch osds or crush nodes, <flags> must be a comma-separated subset of {noup,
                                                                                                    nodown,noin,noout}
osd set-nearfull-ratio <ratio:float>                                                               set usage ratio at which OSDs are marked near-full
osd set-require-min-compat-client <version> [--yes-i-really-mean-it]                               set the minimum client version we will maintain compatibility with
osd setcrushmap [<prior_version:int>]                                                              set crush map from input file
osd setmaxosd <newmax:int>                                                                         set new maximum osd value
osd stat                                                                                           print summary of OSD map
osd status [<bucket>]                                                                              Show the status of OSDs within a bucket, or all
osd stop <ids>...                                                                                  stop the corresponding osd daemons and mark them as down
osd test-reweight-by-pg [<oload:int>] [<max_change:float>] [<max_osds:int>] [<pools>...]           dry run of reweight OSDs by PG distribution [overload-percentage-for-consideration, default 120]
osd test-reweight-by-utilization [<oload:int>] [<max_change:float>] [<max_osds:int>] [--no-        dry run of reweight OSDs by utilization [overload-percentage-for-consideration, default 120]
 increasing]                                                                                       
osd tier add <pool> <tierpool> [--force-nonempty]                                                  add the tier <tierpool> (the second one) to base pool <pool> (the first one)
osd tier add-cache <pool> <tierpool> <size:int>                                                    add a cache <tierpool> (the second one) of size <size> to existing pool <pool> (the first one)
osd tier cache-mode <pool> writeback|readproxy|readonly|none [--yes-i-really-mean-it]              specify the caching mode for cache tier <pool>
osd tier rm <pool> <tierpool>                                                                      remove the tier <tierpool> (the second one) from base pool <pool> (the first one)
osd tier rm-overlay <pool>                                                                         remove the overlay pool for base pool <pool>
osd tier set-overlay <pool> <overlaypool>                                                          set the overlay pool for base pool <pool> to be <overlaypool>
osd tree [<epoch:int>] [up|down|in|out|destroyed...]                                               print OSD tree
osd tree-from [<epoch:int>] <bucket> [up|down|in|out|destroyed...]                                 print OSD tree in bucket
osd unpause                                                                                        unpause osd
osd unset full|pause|noup|nodown|noout|noin|nobackfill|norebalance|norecover|noscrub|nodeep-scrub| unset <key>
 notieragent|nosnaptrim                                                                            
osd unset-group <flags> <who>...                                                                   unset <flags> for batch osds or crush nodes, <flags> must be a comma-separated subset of {noup,
                                                                                                    nodown,noin,noout}
osd utilization                                                                                    get basic pg distribution stats
osd versions                                                                                       check running versions of OSDs
pg cancel-force-backfill <pgid>...                                                                 restore normal backfill priority of <pgid>
pg cancel-force-recovery <pgid>...                                                                 restore normal recovery priority of <pgid>
pg debug unfound_objects_exist|degraded_pgs_exist                                                  show debug info about pgs
pg deep-scrub <pgid>                                                                               start deep-scrub on <pgid>
pg dump [all|summary|sum|delta|pools|osds|pgs|pgs_brief...]                                        show human-readable versions of pg map (only 'all' valid with plain)
pg dump_json [all|summary|sum|pools|osds|pgs...]                                                   show human-readable version of pg map in json only
pg dump_pools_json                                                                                 show pg pools info in json only
pg dump_stuck [inactive|unclean|stale|undersized|degraded...] [<threshold:int>]                    show information about stuck pgs
pg force-backfill <pgid>...                                                                        force backfill of <pgid> first
pg force-recovery <pgid>...                                                                        force recovery of <pgid> first
pg getmap                                                                                          get binary pg map to -o/stdout
pg ls [<pool:int>] [<states>...]                                                                   list pg with specific pool, osd, state
pg ls-by-osd <id|osd.id> [<pool:int>] [<states>...]                                                list pg on osd [osd]
pg ls-by-pool <poolstr> [<states>...]                                                              list pg with pool = [poolname]
pg ls-by-primary <id|osd.id> [<pool:int>] [<states>...]                                            list pg with primary = [osd]
pg map <pgid>                                                                                      show mapping of pg to osds
pg repair <pgid>                                                                                   start repair on <pgid>
pg repeer <pgid>                                                                                   force a PG to repeer
pg scrub <pgid>                                                                                    start scrub on <pgid>
pg stat                                                                                            show placement group status.
progress                                                                                           Show progress of recovery operations
progress clear                                                                                     Reset progress tracking
progress json                                                                                      Show machine readable progress information
prometheus file_sd_config                                                                          Return file_sd compatible prometheus config for mgr cluster
quorum_status                                                                                      report status of monitor quorum
rbd mirror snapshot schedule add <level_spec> <interval> [<start_time>]                            Add rbd mirror snapshot schedule
rbd mirror snapshot schedule list [<level_spec>]                                                   List rbd mirror snapshot schedule
rbd mirror snapshot schedule remove <level_spec> [<interval>] [<start_time>]                       Remove rbd mirror snapshot schedule
rbd mirror snapshot schedule status [<level_spec>]                                                 Show rbd mirror snapshot schedule status
rbd perf image counters [<pool_spec>] [write_ops|write_bytes|write_latency|read_ops|read_bytes|    Retrieve current RBD IO performance counters
 read_latency]                                                                                     
rbd perf image stats [<pool_spec>] [write_ops|write_bytes|write_latency|read_ops|read_bytes|read_  Retrieve current RBD IO performance stats
 latency]                                                                                          
rbd task add flatten <image_spec>                                                                  Flatten a cloned image asynchronously in the background
rbd task add migration abort <image_spec>                                                          Abort a prepared migration asynchronously in the background
rbd task add migration commit <image_spec>                                                         Commit an executed migration asynchronously in the background
rbd task add migration execute <image_spec>                                                        Execute an image migration asynchronously in the background
rbd task add remove <image_spec>                                                                   Remove an image asynchronously in the background
rbd task add trash remove <image_id_spec>                                                          Remove an image from the trash asynchronously in the background
rbd task cancel <task_id>                                                                          Cancel a pending or running asynchronous task
rbd task list [<task_id>]                                                                          List pending or running asynchronous tasks
rbd trash purge schedule add <level_spec> <interval> [<start_time>]                                Add rbd trash purge schedule
rbd trash purge schedule list [<level_spec>]                                                       List rbd trash purge schedule
rbd trash purge schedule remove <level_spec> [<interval>] [<start_time>]                           Remove rbd trash purge schedule
rbd trash purge schedule status [<level_spec>]                                                     Show rbd trash purge schedule status
report [<tags>...]                                                                                 report full status of cluster, optional title tag strings
restful create-key <key_name>                                                                      Create an API key with this name
restful create-self-signed-cert                                                                    Create localized self signed certificate
restful delete-key <key_name>                                                                      Delete an API key with this name
restful list-keys                                                                                  List all API keys
restful restart                                                                                    Restart API server
service dump                                                                                       dump service map
service status                                                                                     dump service state
status                                                                                             show cluster status
telegraf config-set <key> <value>                                                                  Set a configuration value
telegraf config-show                                                                               Show current configuration
telegraf send                                                                                      Force sending data to Telegraf
telemetry off                                                                                      Disable telemetry reports from this cluster
telemetry on [<license>]                                                                           Enable telemetry reports from this cluster
telemetry send [ceph|device...] [<license>]                                                        Force sending data to Ceph telemetry
telemetry show [<channels>...]                                                                     Show last report or report to be sent
telemetry show-all                                                                                 Show report of all channels
telemetry show-device                                                                              Show last device report or device report to be sent
telemetry status                                                                                   Show current configuration
tell <type.id> <args>...                                                                           send a command to a specific daemon
test_orchestrator load_data                                                                        load dummy data into test orchestrator
time-sync-status                                                                                   show time sync status
versions                                                                                           check running versions of ceph daemons
zabbix config-set <key> <value>                                                                    Set a configuration value
zabbix config-show                                                                                 Show current configuration
zabbix discovery                                                                                   Discovering Zabbix data
zabbix send                                                                                        Force sending data to Zabbix
