# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/kohtaaminen/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([798b8f29 ...](https://git.sr.ht/~sthagen/kohtaaminen/blob/default/etc/sbom/cdx.json.sha256 "sha256:798b8f2991e20351ae6b998df09d2c5e02e65e7b4e9120493dde3a946e96532d")).
<!--[[[end]]] (checksum: a9f42dcb631e4b37e9ac3eb3c9a8b5f1)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                     | Version                                               | License     | Author            | Description (from packaging data)                                  |
|:---------------------------------------------------------|:------------------------------------------------------|:------------|:------------------|:-------------------------------------------------------------------|
| [mdformat-gfm](https://github.com/hukkinj1/mdformat-gfm) | [0.3.5](https://pypi.org/project/mdformat-gfm/0.3.5/) | MIT License | Taneli Hukkinen   | Mdformat plugin for GitHub Flavored Markdown compatibility         |
| [pypandoc](https://github.com/JessicaTegner/pypandoc)    | [1.12](https://pypi.org/project/pypandoc/1.12/)       | MIT License | Juho Vepsäläinen  | Thin wrapper for pandoc.                                           |
| [typer](https://github.com/tiangolo/typer)               | [0.9.0](https://pypi.org/project/typer/0.9.0/)        | MIT License | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: c65f70819409168c2c77d02a012af08e)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                  | Version                                                    | License                            | Author                                                                                | Description (from packaging data)                         |
|:----------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:----------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                         | [8.1.6](https://pypi.org/project/click/8.1.6/)             | BSD License                        | Pallets <contact@palletsprojects.com>                                                 | Composable command line interface toolkit                 |
| [markdown-it-py](https://github.com/executablebooks/markdown-it-py)   | [2.2.0](https://pypi.org/project/markdown-it-py/2.2.0/)    | MIT License                        | Chris Sewell <chrisj_sewell@hotmail.com>                                              | Python port of markdown-it. Markdown parsing, done right! |
| [mdformat](https://github.com/executablebooks/mdformat)               | [0.7.16](https://pypi.org/project/mdformat/0.7.16/)        | MIT License                        | Taneli Hukkinen <hukkin@users.noreply.github.com>                                     | CommonMark compliant Markdown formatter                   |
| [mdformat_tables](https://github.com/executablebooks/mdformat-tables) | [0.4.1](https://pypi.org/project/mdformat_tables/0.4.1/)   | MIT License                        | Chris Sewell                                                                          | An mdformat plugin for rendering tables.                  |
| [mdit-py-plugins](https://github.com/executablebooks/mdit-py-plugins) | [0.3.5](https://pypi.org/project/mdit-py-plugins/0.3.5/)   | MIT License                        | Chris Sewell <chrisj_sewell@hotmail.com>                                              | Collection of plugins for markdown-it-py                  |
| [mdurl](https://github.com/executablebooks/mdurl)                     | [0.1.2](https://pypi.org/project/mdurl/0.1.2/)             | MIT License                        | Taneli Hukkinen <hukkin@users.noreply.github.com>                                     | Markdown URL utilities                                    |
| [tomli](https://github.com/hukkin/tomli)                              | [2.0.1](https://pypi.org/project/tomli/2.0.1/)             | MIT License                        | Taneli Hukkinen <hukkin@users.noreply.github.com>                                     | A lil' TOML parser                                        |
| [typing_extensions](https://github.com/python/typing_extensions)      | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+    |
<!--[[[end]]] (checksum: 7ca6971e25765354952f0dec73193369)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
mdformat-gfm==0.3.5
├── markdown-it-py [required: Any, installed: 2.2.0]
│   └── mdurl [required: ~=0.1, installed: 0.1.2]
├── mdformat [required: >=0.7.5,<0.8.0, installed: 0.7.16]
│   ├── markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.2.0]
│   │   └── mdurl [required: ~=0.1, installed: 0.1.2]
│   └── tomli [required: >=1.1.0, installed: 2.0.1]
├── mdformat-tables [required: >=0.4.0, installed: 0.4.1]
│   └── mdformat [required: >=0.7.5,<0.8.0, installed: 0.7.16]
│       ├── markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.2.0]
│       │   └── mdurl [required: ~=0.1, installed: 0.1.2]
│       └── tomli [required: >=1.1.0, installed: 2.0.1]
└── mdit-py-plugins [required: >=0.2.0,<0.4.0, installed: 0.3.5]
    └── markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.2.0]
        └── mdurl [required: ~=0.1, installed: 0.1.2]
pypandoc==1.12
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 7edf5aae174ad1b18c35b3807bcbdb21)-->
