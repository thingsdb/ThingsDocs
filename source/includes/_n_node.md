## node

Returns information about the connected node.

Value | Description
------- | -----------
archive_files | Number of archive files. May decrease after a full store during *away* mode.
archived_in_memory | Number of events which are archived in memory.
cached_names | Number of [names](#names) cached in memory.
client_port | Listening for client TCP socket connections on this port.
db_stored_event_id | Last stored event ID in full database store.
events_in_queue | Events which are pending in the queue.
global_committed_event_id | Lowest known committed event ID by all nodes.
global_stored_event_id | Lowest known stored event ID by all nodes.
hostname | Hostname of the node.
ip_support | Enabled IP support. May be IPv4/IPv6 or both.
libcleri_version | Cleri language parser library version.
libpcre2_version | PCRE regular expression library version.
libqpack_version | QPack data protocol library version.
libuv_version | UV asynchronous library version.
local_committed_event_id | Last committed event ID on the node.
local_stored_event_id | Last stored event ID on disk. Store takes place when in *away* mode.
log_level | Current log level for the node. May be changed at runtime using [set_log_level(..)](#set_log_level)
next_event_id | Next free event ID.
next_thing_id | Next free things ID.
node_id | The `id` which is assigned to the node.
node_port | Listening for node TCP socket connections on this port.
status | Current status of the ThingsDB node.
storage_path | Path used for storing ThingsDB data.
syntax_version | Language or syntax version. A new version of ThingsDB might also have a new language version.
uptime | Uptime of the node in seconds.
version | Version of ThingsDB,
zone | Zone which is assigned to this node. May be changed in the ThingsDB configuration file.

This function does *not* generate an [event](#events).
