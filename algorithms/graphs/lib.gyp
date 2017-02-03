{                                                                                     
    "includes": [
        './common.gypi',
    ],
    "targets":                                                                        
    [                                                                                 
        {                                                                             
            "target_name": "libgraphs",                                                     
            "type": "shared_library",
            "sources": [                                                              
                "graph.h",
                "graph.c",
                "search.h",
                "search.c",
            ],                                                                        
            "include_dirs": [
                "./",
            ],
        },                                                                            
    ],                                                                                
}                                                                                     
