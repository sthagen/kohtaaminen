# Example Usage

Export zip file with conventions adhering html and media tree:
```console
$ kohtaaminen translate tests/fixtures/basic/export.zip
analyzing zip file listing of (tests/fixtures/basic/export.zip)
unpacking zip file below (/tmp/secure/T/tmp_18l00ii)
traversing folder (/tmp/secure/T/tmp_18l00ii)
* /tmp/secure/T/tmp_18l00ii
* /tmp/secure/T/tmp_18l00ii/KOH
  - /tmp/secure/T/tmp_18l00ii/KOH/1-Scope_2656469003.html
  - /tmp/secure/T/tmp_18l00ii/KOH/2-References_2656501774.html
  - /tmp/secure/T/tmp_18l00ii/KOH/3-All-Good-Things-Come-in-Threes_2656469010.html
  - /tmp/secure/T/tmp_18l00ii/KOH/Start_2656468993.html
  - /tmp/secure/T/tmp_18l00ii/KOH/index.html
* /tmp/secure/T/tmp_18l00ii/KOH/attachments
* /tmp/secure/T/tmp_18l00ii/KOH/attachments/2656469010
  - /tmp/secure/T/tmp_18l00ii/KOH/attachments/2656469010/2656469021.jpg
* /tmp/secure/T/tmp_18l00ii/KOH/images
* /tmp/secure/T/tmp_18l00ii/KOH/images/icons
  - /tmp/secure/T/tmp_18l00ii/KOH/images/icons/bullet_blue.gif
* /tmp/secure/T/tmp_18l00ii/KOH/styles
  - /tmp/secure/T/tmp_18l00ii/KOH/styles/site.css
translating html tree from (tests/fixtures/basic/export.zip) into markdown tree below kohtaaminen-md
- /tmp/secure/T/tmp_18l00ii/KOH/1-Scope_2656469003.html
- /tmp/secure/T/tmp_18l00ii/KOH/2-References_2656501774.html
- /tmp/secure/T/tmp_18l00ii/KOH/3-All-Good-Things-Come-in-Threes_2656469010.html
- /tmp/secure/T/tmp_18l00ii/KOH/Start_2656468993.html
- /tmp/secure/T/tmp_18l00ii/KOH/index.html *
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
