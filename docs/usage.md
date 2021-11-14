# Example Usage

Export zip file with conventions adhering html and media tree:
```console
$ kohtaaminen translate tests/fixtures/basic/export.zip
analyzing zip file listing of (tests/fixtures/basic/export.zip)
unpacking zip file below (/var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii)
traversing folder (/var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii)
* /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii
* /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH
  - /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/1-Scope_2656469003.html
  - /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/2-References_2656501774.html
  - /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/3-All-Good-Things-Come-in-Threes_2656469010.html
  - /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/Start_2656468993.html
  - /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/index.html
* /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/attachments
* /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/attachments/2656469010
  - /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/attachments/2656469010/2656469021.jpg
* /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/images
* /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/images/icons
  - /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/images/icons/bullet_blue.gif
* /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/styles
  - /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/styles/site.css
translating html tree from (tests/fixtures/basic/export.zip) into markdown tree below kohtaaminen-md
- /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/1-Scope_2656469003.html
- /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/2-References_2656501774.html
- /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/3-All-Good-Things-Come-in-Threes_2656469010.html
- /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/Start_2656468993.html
- /var/folders/7n/j4v9j0797kn4qrv4hkqs5gkh0000gn/T/tmp_18l00ii/KOH/index.html *
imported 1 distinct asset:
- attachments/2656469010/2656469021.jpg
markdown tree is below (kohtaaminen-md)
```

Result folder looks like this:
```console
$ tree kohtaaminen-md
kohtaaminen-md
├── 1-Scope_2656469003.md
├── 2-References_2656501774.md
├── 3-All-Good-Things-Come-in-Threes_2656469010.md
├── Start_2656468993.md
├── attachments
│   └── 2656469010
│       └── 2656469021.jpg
└── index.md

2 directories, 6 files
```

Ask for version:
```console
$ kohtaaminen version
Meeting, rendezvous, confluence (Finnish kohtaaminen) mark up, down, and up again version 2021.11.14
```

Asking for general help:
```console
$ kohtaaminen
Usage: kohtaaminen [OPTIONS] COMMAND [ARGS]...

  Meeting, rendezvous, confluence (Finnish kohtaaminen) mark up, down, and up
  again.

  Given a zip file containing a tree of html and media files following certain
  conventions, the tool produces a markdown media tree below `kohtaaminen-md`.

Options:
  -V, --version  Display the kohtaaminen version and exit
  -h, --help     Show this message and exit.

Commands:
  translate  Translate from zip file containing a tree of html and media...
  version    Display the kohtaaminen version and exit
```

Asking for help on translation:
```console
$ kohtaaminen translate --help
Usage: kohtaaminen translate [OPTIONS] [SOURCE]

  Translate from zip file containing a tree of html and media files to a
  folder with markdown.

Arguments:
  [SOURCE]  [default: STDIN]

Options:
  -i, --input <sourcepath>  Path to input file (default is reading from
                            standard in)
  -h, --help                Show this message and exit.
```
