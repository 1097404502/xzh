
 General usage: 
 ==============
usage: ceph [-h] [-c CEPHCONF] [-i INPUT_FILE] [-o OUTPUT_FILE]
            [--id CLIENT_ID] [--name CLIENT_NAME] [--cluster CLUSTER]
            [--admin-daemon ADMIN_SOCKET] [--admin-socket ADMIN_SOCKET_NOPE]
            [-s] [-w] [--watch-debug] [--watch-info] [--watch-sec]
            [--watch-warn] [--watch-error] [--version] [--verbose] [--concise]
            [-f {json,json-pretty,xml,xml-pretty,plain}]
            [--connect-timeout CLUSTER_TIMEOUT]

Ceph administration tool

optional arguments:
  -h, --help            request mon help
  -c CEPHCONF, --conf CEPHCONF
                        ceph configuration file
  -i INPUT_FILE, --in-file INPUT_FILE
                        input file, or "-" for stdin
  -o OUTPUT_FILE, --out-file OUTPUT_FILE
                        output file, or "-" for stdout
  --id CLIENT_ID, --user CLIENT_ID
                        client id for authentication
  --name CLIENT_NAME, -n CLIENT_NAME
                        client name for authentication
  --cluster CLUSTER     cluster name
  --admin-daemon ADMIN_SOCKET
                        submit admin-socket commands ("help" for help
  --admin-socket ADMIN_SOCKET_NOPE
                        you probably mean --admin-daemon
  -s, --status          show cluster status
  -w, --watch           watch live cluster changes
  --watch-debug         watch debug events
  --watch-info          watch info events
  --watch-sec           watch security events
  --watch-warn          watch warn events
  --watch-error         watch error events
  --version, -v         display version
  --verbose             make verbose
  --concise             make less verbose
  -f {json,json-pretty,xml,xml-pretty,plain}, --format {json,json-pretty,xml,xml-pretty,plain}
  --connect-timeout CLUSTER_TIMEOUT
                        set a timeout for connecting to the cluster

 Monitor commands: 
 =================
[Contacting monitor, timeout after 5 seconds]
auth add <entity> {<caps> [<caps>...]}   add auth info for <entity> from input 
                                          file, or random key if no input is 
                                          given, and/or any caps specified in 
                                          the command
auth caps <entity> <caps> [<caps>...]    update caps for <name> from caps 
                                          specified in the command
auth del <entity>                        delete all caps for <name>
auth export {<entity>}                   write keyring for requested entity, or 
                                          master keyring if none given
auth get <entity>                        write keyring file with requested key
auth get-key <entity>                    display requested key
auth get-or-create <entity> {<caps>      add auth info for <entity> from input 
 [<caps>...]}                             file, or random key if no input given,
                                          and/or any caps specified in the 
                                          command
auth get-or-create-key <entity> {<caps>  get, or add, key for <name> from 
 [<caps>...]}                             system/caps pairs specified in the 
                                          command.  If key already exists, any 
                                          given caps must match the existing 
                                          caps for that key.
auth import                              auth import: read keyring file from -i 
                                          <file>
auth list                                list authentication state
auth print-key <entity>                  display requested key
auth print_key <entity>                  display requested key
auth rm <entity>                         remove all caps for <name>
compact                                  cause compaction of monitor's leveldb 
                                          storage (DEPRECATED)
config-key del <key>                     delete <key>
config-key exists <key>                  check for <key>'s existence
config-key get <key>                     get <key>
config-key list                          list keys
config-key put <key> {<val>}             put <key>, value <val>
config-key rm <key>                      rm <key>
df {detail}                              show cluster free space stats
fs add_data_pool <fs_name> <pool>        add data pool <pool>
fs dump {<int[0-]>}                      dump all CephFS status, optionally 
                                          from epoch
fs flag set enable_multiple <val> {--    Set a global CephFS flag
 yes-i-really-mean-it}                   
fs get <fs_name>                         get info about one filesystem
fs ls                                    list filesystems
fs new <fs_name> <metadata> <data>       make new filesystem using named pools 
                                          <metadata> and <data>
fs reset <fs_name> {--yes-i-really-mean- disaster recovery only: reset to a 
 it}                                      single-MDS map
fs rm <fs_name> {--yes-i-really-mean-it} disable the named filesystem
fs rm_data_pool <fs_name> <pool>         remove data pool <pool>
fs set <fs_name> max_mds|max_file_size|  set mds parameter <var> to <val>
 allow_new_snaps|inline_data|cluster_    
 down|allow_multimds|allow_dirfrags      
 <val> {<confirm>}                       
fs set_default <fs_name>                 set the default to the named filesystem
fsid                                     show cluster FSID/UUID
health {detail}                          show cluster health
heap dump|start_profiler|stop_profiler|  show heap usage info (available only 
 release|stats                            if compiled with tcmalloc)
injectargs <injected_args> [<injected_   inject config arguments into monitor
 args>...]                               
log <logtext> [<logtext>...]             log supplied text to the monitor log
mds add_data_pool <pool>                 add data pool <pool>
mds cluster_down                         take MDS cluster down
mds cluster_up                           bring MDS cluster up
mds compat rm_compat <int[0-]>           remove compatible feature
mds compat rm_incompat <int[0-]>         remove incompatible feature
mds compat show                          show mds compatibility settings
mds deactivate <who>                     stop mds
mds dump {<int[0-]>}                     dump legacy MDS cluster info, 
                                          optionally from epoch
mds fail <who>                           force mds to status failed
mds getmap {<int[0-]>}                   get MDS map, optionally from epoch
mds metadata <who>                       fetch metadata for mds <who>
mds newfs <int[0-]> <int[0-]> {--yes-i-  make new filesystem using pools 
 really-mean-it}                          <metadata> and <data>
mds remove_data_pool <pool>              remove data pool <pool>
mds repaired <rank>                      mark a damaged MDS rank as no longer 
                                          damaged
mds rm <int[0-]>                         remove nonactive mds
mds rm_data_pool <pool>                  remove data pool <pool>
mds rmfailed <who> {<confirm>}           remove failed mds
mds set max_mds|max_file_size|allow_new_ set mds parameter <var> to <val>
 snaps|inline_data|allow_multimds|allow_ 
 dirfrags <val> {<confirm>}              
mds set_max_mds <int[0-]>                set max MDS index
mds set_state <int[0-]> <int[0-20]>      set mds state of <gid> to <numeric-
                                          state>
mds stat                                 show MDS status
mds stop <who>                           stop mds
mds tell <who> <args> [<args>...]        send command to particular mds
mon add <name> <IPaddr[:port]>           add new monitor named <name> at <addr>
mon compact                              cause compaction of monitor's leveldb 
                                          storage
mon dump {<int[0-]>}                     dump formatted monmap (optionally from 
                                          epoch)
mon getmap {<int[0-]>}                   get monmap
mon metadata <id>                        fetch metadata for mon <id>
mon remove <name>                        remove monitor named <name>
mon rm <name>                            remove monitor named <name>
mon scrub                                scrub the monitor stores
mon stat                                 summarize monitor status
mon sync force {--yes-i-really-mean-it}  force sync of and clear monitor store
 {--i-know-what-i-am-doing}              
mon_status                               report status of monitors
node ls {all|osd|mon|mds}                list all nodes in cluster [type]
osd blacklist add|rm <EntityAddr>        add (optionally until <expire> seconds 
 {<float[0.0-]>}                          from now) or remove <addr> from 
                                          blacklist
osd blacklist clear                      clear all blacklisted clients
osd blacklist ls                         show blacklisted clients
osd blocked-by                           print histogram of which OSDs are 
                                          blocking their peers
osd create {<uuid>} {<int[0-]>}          create new osd (with optional UUID and 
                                          ID)
osd crush add <osdname (id|osd.id)>      add or update crushmap position and 
 <float[0.0-]> <args> [<args>...]         weight for <name> with <weight> and 
                                          location <args>
osd crush add-bucket <name> <type>       add no-parent (probably root) crush 
                                          bucket <name> of type <type>
osd crush create-or-move <osdname (id|   create entry or move existing entry 
 osd.id)> <float[0.0-]> <args> [<args>..  for <name> <weight> at/to location 
 .]                                       <args>
osd crush dump                           dump crush map
osd crush get-tunable straw_calc_version get crush tunable <tunable>
osd crush link <name> <args> [<args>...] link existing entry for <name> under 
                                          location <args>
osd crush move <name> <args> [<args>...] move existing entry for <name> to 
                                          location <args>
osd crush remove <name> {<ancestor>}     remove <name> from crush map (
                                          everywhere, or just at <ancestor>)
osd crush rename-bucket <srcname>        rename bucket <srcname> to <dstname>
 <dstname>                               
osd crush reweight <name> <float[0.0-]>  change <name>'s weight to <weight> in 
                                          crush map
osd crush reweight-all                   recalculate the weights for the tree 
                                          to ensure they sum correctly
osd crush reweight-subtree <name>        change all leaf items beneath <name> 
 <float[0.0-]>                            to <weight> in crush map
osd crush rm <name> {<ancestor>}         remove <name> from crush map (
                                          everywhere, or just at <ancestor>)
osd crush rule create-erasure <name>     create crush rule <name> for erasure 
 {<profile>}                              coded pool created with <profile> (
                                          default default)
osd crush rule create-simple <name>      create crush rule <name> to start from 
 <root> <type> {firstn|indep}             <root>, replicate across buckets of 
                                          type <type>, using a choose mode of 
                                          <firstn|indep> (default firstn; indep 
                                          best for erasure pools)
osd crush rule dump {<name>}             dump crush rule <name> (default all)
osd crush rule list                      list crush rules
osd crush rule ls                        list crush rules
osd crush rule rm <name>                 remove crush rule <name>
osd crush set                            set crush map from input file
osd crush set <osdname (id|osd.id)>      update crushmap position and weight 
 <float[0.0-]> <args> [<args>...]         for <name> to <weight> with location 
                                          <args>
osd crush set-tunable straw_calc_        set crush tunable <tunable> to <value>
 version <int>                           
osd crush show-tunables                  show current crush tunables
osd crush tree                           dump crush buckets and items in a tree 
                                          view
osd crush tunables legacy|argonaut|      set crush tunables values to <profile>
 bobtail|firefly|hammer|jewel|optimal|   
 default                                 
osd crush unlink <name> {<ancestor>}     unlink <name> from crush map (
                                          everywhere, or just at <ancestor>)
osd deep-scrub <who>                     initiate deep scrub on osd <who>
osd df {plain|tree}                      show OSD utilization
osd down <ids> [<ids>...]                set osd(s) <id> [<id>...] down
osd dump {<int[0-]>}                     print summary of OSD map
osd erasure-code-profile get <name>      get erasure code profile <name>
osd erasure-code-profile ls              list all erasure code profiles
osd erasure-code-profile rm <name>       remove erasure code profile <name>
osd erasure-code-profile set <name>      create erasure code profile <name> 
 {<profile> [<profile>...]}               with [<key[=value]> ...] pairs. Add a 
                                          --force at the end to override an 
                                          existing profile (VERY DANGEROUS)
osd find <int[0-]>                       find osd <id> in the CRUSH map and 
                                          show its location
osd getcrushmap {<int[0-]>}              get CRUSH map
osd getmap {<int[0-]>}                   get OSD map
osd getmaxosd                            show largest OSD id
osd in <ids> [<ids>...]                  set osd(s) <id> [<id>...] in
osd lost <int[0-]> {--yes-i-really-mean- mark osd as permanently lost. THIS 
 it}                                      DESTROYS DATA IF NO MORE REPLICAS 
                                          EXIST, BE CAREFUL
osd ls {<int[0-]>}                       show all OSD ids
osd lspools {<int>}                      list pools
osd map <poolname> <objectname>          find pg for <object> in <pool> with 
 {<nspace>}                               [namespace]
osd metadata {<int[0-]>}                 fetch metadata for osd {id} (default 
                                          all)
osd out <ids> [<ids>...]                 set osd(s) <id> [<id>...] out
osd pause                                pause osd
osd perf                                 print dump of OSD perf summary stats
osd pg-temp <pgid> {<id> [<id>...]}      set pg_temp mapping pgid:[<id> [<id>...
                                          ]] (developers only)
osd pool create <poolname> <int[0-]>     create pool
 {<int[0-]>} {replicated|erasure}        
 {<erasure_code_profile>} {<ruleset>}    
 {<int>}                                 
osd pool delete <poolname> {<poolname>}  delete pool
 {--yes-i-really-really-mean-it}         
osd pool get <poolname> size|min_size|   get pool parameter <var>
 crash_replay_interval|pg_num|pgp_num|   
 crush_ruleset|hashpspool|nodelete|      
 nopgchange|nosizechange|write_fadvise_  
 dontneed|noscrub|nodeep-scrub|hit_set_  
 type|hit_set_period|hit_set_count|hit_  
 set_fpp|auid|target_max_objects|target_ 
 max_bytes|cache_target_dirty_ratio|     
 cache_target_dirty_high_ratio|cache_    
 target_full_ratio|cache_min_flush_age|  
 cache_min_evict_age|erasure_code_       
 profile|min_read_recency_for_promote|   
 all|min_write_recency_for_promote|fast_ 
 read|hit_set_grade_decay_rate|hit_set_  
 search_last_n|scrub_min_interval|scrub_ 
 max_interval|deep_scrub_interval|       
 recovery_priority|recovery_op_priority| 
 scrub_priority                          
osd pool get-quota <poolname>            obtain object or byte limits for pool
osd pool ls {detail}                     list pools
osd pool mksnap <poolname> <snap>        make snapshot <snap> in <pool>
osd pool rename <poolname> <poolname>    rename <srcpool> to <destpool>
osd pool rm <poolname> {<poolname>} {--  remove pool
 yes-i-really-really-mean-it}            
osd pool rmsnap <poolname> <snap>        remove snapshot <snap> from <pool>
osd pool set <poolname> size|min_size|   set pool parameter <var> to <val>
 crash_replay_interval|pg_num|pgp_num|   
 crush_ruleset|hashpspool|nodelete|      
 nopgchange|nosizechange|write_fadvise_  
 dontneed|noscrub|nodeep-scrub|hit_set_  
 type|hit_set_period|hit_set_count|hit_  
 set_fpp|use_gmt_hitset|debug_fake_ec_   
 pool|target_max_bytes|target_max_       
 objects|cache_target_dirty_ratio|cache_ 
 target_dirty_high_ratio|cache_target_   
 full_ratio|cache_min_flush_age|cache_   
 min_evict_age|auid|min_read_recency_    
 for_promote|min_write_recency_for_      
 promote|fast_read|hit_set_grade_decay_  
 rate|hit_set_search_last_n|scrub_min_   
 interval|scrub_max_interval|deep_scrub_ 
 interval|recovery_priority|recovery_op_ 
 priority|scrub_priority <val> {--yes-i- 
 really-mean-it}                         
osd pool set-quota <poolname> max_       set object or byte limit on pool
 objects|max_bytes <val>                 
osd pool stats {<name>}                  obtain stats from all pools, or from 
                                          specified pool
osd primary-affinity <osdname (id|osd.   adjust osd primary-affinity from 0.0 <=
 id)> <float[0.0-1.0]>                     <weight> <= 1.0
osd primary-temp <pgid> <id>             set primary_temp mapping pgid:<id>|-1 (
                                          developers only)
osd repair <who>                         initiate repair on osd <who>
osd reweight <int[0-]> <float[0.0-1.0]>  reweight osd to 0.0 < <weight> < 1.0
osd reweight-by-pg {<int>} {<float>}     reweight OSDs by PG distribution 
 {<int>} {<poolname> [<poolname>...]}     [overload-percentage-for-
                                          consideration, default 120]
osd reweight-by-utilization {<int>}      reweight OSDs by utilization [overload-
 {<float>} {<int>} {--no-increasing}      percentage-for-consideration, default 
                                          120]
osd rm <ids> [<ids>...]                  remove osd(s) <id> [<id>...] in
osd scrub <who>                          initiate scrub on osd <who>
osd set full|pause|noup|nodown|noout|    set <key>
 noin|nobackfill|norebalance|norecover|  
 noscrub|nodeep-scrub|notieragent|       
 sortbitwise|require_jewel_osds          
osd setcrushmap                          set crush map from input file
osd setmaxosd <int[0-]>                  set new maximum osd value
osd stat                                 print summary of OSD map
osd test-reweight-by-pg {<int>}          dry run of reweight OSDs by PG 
 {<float>} {<int>} {<poolname>            distribution [overload-percentage-for-
 [<poolname>...]}                         consideration, default 120]
osd test-reweight-by-utilization         dry run of reweight OSDs by 
 {<int>} {<float>} {<int>} {--no-         utilization [overload-percentage-for-
 increasing}                              consideration, default 120]
osd thrash <int[0-]>                     thrash OSDs for <num_epochs>
osd tier add <poolname> <poolname> {--   add the tier <tierpool> (the second 
 force-nonempty}                          one) to base pool <pool> (the first 
                                          one)
osd tier add-cache <poolname>            add a cache <tierpool> (the second one)
 <poolname> <int[0-]>                     of size <size> to existing pool 
                                          <pool> (the first one)
osd tier cache-mode <poolname> none|     specify the caching mode for cache 
 writeback|forward|readonly|readforward|  tier <pool>
 proxy|readproxy {--yes-i-really-mean-   
 it}                                     
osd tier remove <poolname> <poolname>    remove the tier <tierpool> (the second 
                                          one) from base pool <pool> (the first 
                                          one)
osd tier remove-overlay <poolname>       remove the overlay pool for base pool 
                                          <pool>
osd tier rm <poolname> <poolname>        remove the tier <tierpool> (the second 
                                          one) from base pool <pool> (the first 
                                          one)
osd tier rm-overlay <poolname>           remove the overlay pool for base pool 
                                          <pool>
osd tier set-overlay <poolname>          set the overlay pool for base pool 
 <poolname>                               <pool> to be <overlaypool>
osd tree {<int[0-]>}                     print OSD tree
osd unpause                              unpause osd
osd unset full|pause|noup|nodown|noout|  unset <key>
 noin|nobackfill|norebalance|norecover|  
 noscrub|nodeep-scrub|notieragent|       
 sortbitwise                             
osd utilization                          get basic pg distribution stats
pg debug unfound_objects_exist|degraded_ show debug info about pgs
 pgs_exist                               
pg deep-scrub <pgid>                     start deep-scrub on <pgid>
pg dump {all|summary|sum|delta|pools|    show human-readable versions of pg map 
 osds|pgs|pgs_brief [all|summary|sum|     (only 'all' valid with plain)
 delta|pools|osds|pgs|pgs_brief...]}     
pg dump_json {all|summary|sum|pools|     show human-readable version of pg map 
 osds|pgs [all|summary|sum|pools|osds|    in json only
 pgs...]}                                
pg dump_pools_json                       show pg pools info in json only
pg dump_stuck {inactive|unclean|stale|   show information about stuck pgs
 undersized|degraded [inactive|unclean|  
 stale|undersized|degraded...]} {<int>}  
pg force_create_pg <pgid>                force creation of pg <pgid>
pg getmap                                get binary pg map to -o/stdout
pg ls {<int>} {active|clean|down|replay| list pg with specific pool, osd, state
 splitting|scrubbing|scrubq|degraded|    
 inconsistent|peering|repair|recovering| 
 backfill_wait|incomplete|stale|         
 remapped|deep_scrub|backfill|backfill_  
 toofull|recovery_wait|undersized|       
 activating|peered [active|clean|down|   
 replay|splitting|scrubbing|scrubq|      
 degraded|inconsistent|peering|repair|   
 recovering|backfill_wait|incomplete|    
 stale|remapped|deep_scrub|backfill|     
 backfill_toofull|recovery_wait|         
 undersized|activating|peered...]}       
pg ls-by-osd <osdname (id|osd.id)>       list pg on osd [osd]
 {<int>} {active|clean|down|replay|      
 splitting|scrubbing|scrubq|degraded|    
 inconsistent|peering|repair|recovering| 
 backfill_wait|incomplete|stale|         
 remapped|deep_scrub|backfill|backfill_  
 toofull|recovery_wait|undersized|       
 activating|peered [active|clean|down|   
 replay|splitting|scrubbing|scrubq|      
 degraded|inconsistent|peering|repair|   
 recovering|backfill_wait|incomplete|    
 stale|remapped|deep_scrub|backfill|     
 backfill_toofull|recovery_wait|         
 undersized|activating|peered...]}       
pg ls-by-pool <poolstr> {active|clean|   list pg with pool = [poolname | poolid]
 down|replay|splitting|scrubbing|scrubq| 
 degraded|inconsistent|peering|repair|   
 recovering|backfill_wait|incomplete|    
 stale|remapped|deep_scrub|backfill|     
 backfill_toofull|recovery_wait|         
 undersized|activating|peered [active|   
 clean|down|replay|splitting|scrubbing|  
 scrubq|degraded|inconsistent|peering|   
 repair|recovering|backfill_wait|        
 incomplete|stale|remapped|deep_scrub|   
 backfill|backfill_toofull|recovery_     
 wait|undersized|activating|peered...]}  
pg ls-by-primary <osdname (id|osd.id)>   list pg with primary = [osd]
 {<int>} {active|clean|down|replay|      
 splitting|scrubbing|scrubq|degraded|    
 inconsistent|peering|repair|recovering| 
 backfill_wait|incomplete|stale|         
 remapped|deep_scrub|backfill|backfill_  
 toofull|recovery_wait|undersized|       
 activating|peered [active|clean|down|   
 replay|splitting|scrubbing|scrubq|      
 degraded|inconsistent|peering|repair|   
 recovering|backfill_wait|incomplete|    
 stale|remapped|deep_scrub|backfill|     
 backfill_toofull|recovery_wait|         
 undersized|activating|peered...]}       
pg map <pgid>                            show mapping of pg to osds
pg repair <pgid>                         start repair on <pgid>
pg scrub <pgid>                          start scrub on <pgid>
pg send_pg_creates                       trigger pg creates to be issued
pg set_full_ratio <float[0.0-1.0]>       set ratio at which pgs are considered 
                                          full
pg set_nearfull_ratio <float[0.0-1.0]>   set ratio at which pgs are considered 
                                          nearly full
pg stat                                  show placement group status.
quorum enter|exit                        enter or exit quorum
quorum_status                            report status of monitor quorum
report {<tags> [<tags>...]}              report full status of cluster, 
                                          optional title tag strings
scrub                                    scrub the monitor stores (DEPRECATED)
status                                   show cluster status
sync force {--yes-i-really-mean-it} {--  force sync of and clear monitor store (
 i-know-what-i-am-doing}                  DEPRECATED)
tell <name (type.id)> <args> [<args>...] send a command to a specific daemon
version                                  show mon daemon version
