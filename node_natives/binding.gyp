{
  "targets": [
    
  ],
  'conditions': [
      ['OS=="win"', {
        'targets': [
          {
            "target_name": "addon",
            "sources": [
              "../code/SoftRenderer/*.cpp"
            ],
            "include_dirs" : ["<!(node -e \"require('nan')\")","../code/SoftRenderer/"],
            "libraries": [ "winmm.lib" ]
          },
        ],
      },
      'OS=="mac"', {
        'targets': [
          {
            "target_name": "addon",
            'sources' : [  "<!@(node -p \"require('fs').readdirSync('../code/SoftRenderer').map(f=>'../code/SoftRenderer/'+f).join(' ')\")" ],
            "include_dirs" : ["<!(node -e \"require('nan')\")","../code/SoftRenderer/"],
          },
        ],
      }],
    ],
}
