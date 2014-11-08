{
    "includes": [
        './common.gypi',
    ],
    "targets":
    [
        {
            "target_name": "test_graph",
            "type": "executable",
            "dependencies": [
                "./lib.gyp:libgraphs",
            ],
            "sources": [
                "test_graph.c",
                "test_search.c",
            ],
            "include_dirs": [
                "./",
            ],
            'link_settings': {
                'libraries': [
                ],
#              'library_dirs': [
#              ],
            },
        },
    ],
}

