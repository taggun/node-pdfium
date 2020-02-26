{
  'includes': [
      './common.gypi'
  ],
  'target_defaults': {
    'defines' : [
      'PNG_PREFIX',
      'PNGPREFIX_H',
      'PNG_USE_READ_MACROS',
    ],
    'include_dirs': [
    '<!(node -e "require(\'nan\')")'
#      '<(DEPTH)/third_party/pdfium',
#      '<(DEPTH)/third_party/pdfium/third_party/freetype/include',
    ],
    'conditions': [
      ['OS=="linux"', {
        'conditions': [
          ['target_arch=="x64"', {
            'defines' : [ '_FX_CPU_=_FX_X64_', ],
            'cflags': [ '-fPIC', ],
          }],
          ['target_arch=="ia32"', {
            'defines' : [ '_FX_CPU_=_FX_X86_', ],
          }],
        ],
      }]
    ],
    'msvs_disabled_warnings': [
      4005, 4018, 4146, 4333, 4345, 4267
    ]
  },
  'targets': [
    {
      'target_name': 'node_pdfium',
      'dependencies' : [
        './third_party/pdfium/pdfium.gyp:pdfium'
      ],
      'sources': [
        # is like "ls -1 src/*.cc", but gyp does not support direct patterns on
        # sources
        '<!@(["python", "tools/getSourceFiles.py", "src", "cc"])'
      ]
    },
  ]
}
