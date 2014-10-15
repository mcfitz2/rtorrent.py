import datetime
def timestamp(value):
    return datetime.datetime.fromtimestamp(value)
def str(value):
    return value or None
mapping = { 
    "torrents":{ 
        "accepting_seeders":{
            "name":"d.accepting_seeders", 
            "type":str
        },
        "filename":{
            "name":"d.base_filename", 
            "type":str
        },
        "path":{
            "name":"d.base_path", 
            "type":str
        },
        "bytes_done":{
            "name":"d.bytes_done", 
            "type":int
        },
        "chunk_size":{
            "name":"d.chunk_size", 
            "type":int
        },
        "complete":{
            "name":"d.complete", 
            "type":bool
        },
        "bytes_complete":{
            "name":"d.completed_bytes", 
            "type":int
        },
        "chunks_complete":{
            "name":"d.completed_chunks", 
            "type":int
        },
        "creation_date":{
            "name":"d.creation_date", 
            "type":timestamp
        },
        "category":{
            "name":"d.custom1", 
            "type":str
        },
        "destination":{
            "name":"d.custom2", 
            "type":str
        },
        "custom1":{
            "name":"d.custom1", 
            "type":str
        },
        "custom2":{
            "name":"d.custom2", 
            "type":str
        },
        "custom3":{
            "name":"d.custom3", 
            "type":str
        },
        "custom4":{
            "name":"d.custom4", 
            "type":str
        },
        "custom5":{
            "name":"d.custom5", 
            "type":str
        },
        "directory":{
            "name":"d.directory", 
            "type":str
        },
        "directory_base":{
            "name":"d.directory_base", 
            "type":str
        },
        "rate_down":{
            "name":"d.down.rate", 
            "type":int
        },
        "down_total":{
            "name":"d.down.total", 
            "type":int
        },
        "group_name":{
            "name":"d.group.name", 
            "type":int
        },
        "hash":{
            "name":"d.hash", 
            "type":str
        },
        "hashing":{
            "name":"d.hashing", 
            "type":bool
        },
        "hashing_failed":{
            "name":"d.hashing_failed", 
            "type":bool
        },
        "incomplete":{
            "name":"d.incomplete", 
            "type":bool
        },
        "active":{
            "name":"d.is_active", 
            "type":bool
        },
        "hash_checked":{
            "name":"d.is_hash_checked", 
            "type":bool
        },
        "hash_checking":{
            "name":"d.is_hash_checking", 
            "type":bool
        },
        "multi_file":{
            "name":"d.is_multi_file", 
            "type":bool
        },
        "not_partially_done":{
            "name":"d.is_not_partially_done", 
            "type":bool
        },
       "open":{
           "name":"d.is_open", 
           "type":bool
       },
        "partially_done":{
            "name":"d.is_partially_done", 
            "type":bool
        },
        "private":{
            "name":"d.is_private", 
            "type":bool
        },
        "bytes_left":{
            "name":"d.left_bytes", 
            "type":int
        },
        "load_date":{
            "name":"d.load_date", 
            "type":timestamp
        },
        "loaded_file":{
            "name":"d.loaded_file", 
            "type":str
        },
        "local_id":{
            "name":"d.local_id", 
            "type":str
        },
        "message":{
            "name":"d.message", 
            "type":str
        },
        "name":{
            "name":"d.name", 
            "type":str
        },
        "peers_connected":{
            "name":"d.peers_connected", 
            "type":int
        },
        "priority":{
            "name":"d.priority", 
            "type":int
        },
        "ratio":{
            "name":"d.ratio", 
            "type":int
        },
        "size_bytes":{
            "name":"d.size_bytes", 
            "type":int
        },
        "size_chunks":{
            "name":"d.size_chunks", 
            "type":int
        },
        "size_files":{
            "name":"d.size_files", 
            "type":int
        },
        "state":{
            "name":"d.state", 
            "type":int
        },
        "state_changed":{
            "name":"d.state_changed", 
            "type":int
        },
        "state_counter":{
            "name":"d.state_counter", 
            "type":str
        },
        "torrent_file":{
            "name":"d.tied_to_file", 
            "type":str
        },
        "finished_at":{
            "name":"d.timestamp.finished", 
            "type":timestamp
        },
        "started_at":{
            "name":"d.timestamp.started", 
            "type":timestamp
        },
#        "tracker_url":{
#            "name":"d.tracker_announce", 
#            "type":str
#        },
        "rate_up":{
            "name":"d.up.rate", 
            "type":int
        },
        "up_total":{
            "name":"d.up.total", 
            "type":int
        },
    }, 
    "files":{
        "completed_chunks":{
            "name":"f.completed_chunks", 
            "type":str
        },
        "created":{"name":"f.is_created", "type":str},
        "open":{"name":"f.is_open", "type":str},
        "last_touched":{"name":"f.last_touched", "type":str},
        "offset":{"name":"f.offset", "type":str},
        "path":{"name":"f.path", "type":str},
        "path_components":{"name":"f.path_components", "type":str},
        "path_depth":{"name":"f.path_depth", "type":str},
        "priority":{"name":"f.priority", "type":str},
        "size_bytes":{"name":"f.size_bytes", "type":str},
        "size_chunks":{"name":"f.size_chunks", "type":str},
    },
    "peers":{
        "address":{"name":"p.address", "type":str},
        "banned":{"name":"p.banned", "type":str},
        "client_version":{"name":"p.client_version", "type":str},
        "completed_percent":{"name":"p.completed_percent", "type":str},
        "down_rate":{"name":"p.down_rate", "type":str},
        "down_total":{"name":"p.down_total", "type":str},
        "id":{"name":"p.id", "type":str},
        "id_html":{"name":"p.id_html", "type":str},
        "encrypted":{"name":"p.is_encrypted", "type":str},
        "incoming":{"name":"p.is_incoming", "type":str},
        "obfuscated":{"name":"p.is_obfuscated", "type":str},
        "snubbed":{"name":"p.is_snubbed", "type":str},
        "options_str":{"name":"p.options_str", "type":str},
        "peer_rate":{"name":"p.peer_rate", "type":str},
        "peer_total":{"name":"p.peer_total", "type":str},
        "port":{"name":"p.port", "type":str},
        "snubbed":{"name":"p.snubbed", "type":str},
        "p.up_rate":{"name":"p.up_rate", "type":str},
        "p.up_total":{"name":"p.up_total", "type":str},
    },
    "trackers":{
        "group":{"name":"t.group", "type":str},
        "id":{"name":"t.id", "type":str},
        "enabled":{"name":"t.is_enabled", "type":str},
        "open":{"name":"t.is_open", "type":str},
        "min_interval":{"name":"t.min_interval", "type":str},
        "normal_interval":{"name":"t.normal_interval", "type":str},
        "scrape_complete":{"name":"t.scrape_complete", "type":str},
        "scrape_downloaded":{"name":"t.scrape_downloaded", "type":str},
        "scrape_incomplete":{"name":"t.scrape_incomplete", "type":str},
        "scrape_time_last":{"name":"t.scrape_time_last", "type":str},
        "type":{"name":"t.type", "type":str},
        "url":{"name":"t.url", "type":str},
        
    }
}

