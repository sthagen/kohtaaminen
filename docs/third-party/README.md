# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/kohtaaminen/blob/default/sbom/cdx.json) with SHA256 checksum ([e6804b07 ...](https://git.sr.ht/~sthagen/kohtaaminen/blob/default/sbom/cdx.json.sha256 "sha256:e6804b0719bc771774e245975121b2269dc6990f12596c8981ded38e0cb7e21f")).
<!--[[[end]]] (checksum: 9a4dd266c064489bf83ea812878117ec)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                     | Version                                               | License     | Author                            | Description (from packaging data)                                  |
|:---------------------------------------------------------|:------------------------------------------------------|:------------|:----------------------------------|:-------------------------------------------------------------------|
| [mdformat-gfm](https://github.com/hukkinj1/mdformat-gfm) | [0.3.5](https://pypi.org/project/mdformat-gfm/0.3.5/) | MIT License | Taneli Hukkinen                   | Mdformat plugin for GitHub Flavored Markdown compatibility         |
| [pypandoc](https://github.com/JessicaTegner/pypandoc)    | [1.11](https://pypi.org/project/pypandoc/1.11/)       | MIT License | b'Juho Veps\xc3\xa4l\xc3\xa4inen' | Thin wrapper for pandoc.                                           |
| [typer](https://github.com/tiangolo/typer)               | [0.7.0](https://pypi.org/project/typer/0.7.0/)        | MIT License | Sebastián Ramírez                 | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: e7112c5691a0f0cf900b938ec0f624bb)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                  | Version                                                  | License     | Author                                            | Description (from packaging data)                         |
|:----------------------------------------------------------------------|:---------------------------------------------------------|:------------|:--------------------------------------------------|:----------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                         | [8.1.3](https://pypi.org/project/click/8.1.3/)           | BSD License | Armin Ronacher                                    | Composable command line interface toolkit                 |
| [markdown-it-py](https://github.com/executablebooks/markdown-it-py)   | [2.1.0](https://pypi.org/project/markdown-it-py/2.1.0/)  | MIT License | Chris Sewell <chrisj_sewell@hotmail.com>          | Python port of markdown-it. Markdown parsing, done right! |
| [mdformat](https://github.com/executablebooks/mdformat)               | [0.7.16](https://pypi.org/project/mdformat/0.7.16/)      | MIT License | Taneli Hukkinen <hukkin@users.noreply.github.com> | CommonMark compliant Markdown formatter                   |
| [mdformat_tables](https://github.com/executablebooks/mdformat-tables) | [0.4.1](https://pypi.org/project/mdformat_tables/0.4.1/) | MIT License | Chris Sewell                                      | An mdformat plugin for rendering tables.                  |
| [mdit-py-plugins](https://github.com/executablebooks/mdit-py-plugins) | [0.3.3](https://pypi.org/project/mdit-py-plugins/0.3.3/) | MIT License | Chris Sewell <chrisj_sewell@hotmail.com>          | Collection of plugins for markdown-it-py                  |
| [mdurl](https://github.com/executablebooks/mdurl)                     | [0.1.2](https://pypi.org/project/mdurl/0.1.2/)           | MIT License | Taneli Hukkinen <hukkin@users.noreply.github.com> | Markdown URL utilities                                    |
| [tomli](https://github.com/hukkin/tomli)                              | [2.0.1](https://pypi.org/project/tomli/2.0.1/)           | MIT License | Taneli Hukkinen <hukkin@users.noreply.github.com> | A lil' TOML parser                                        |
<!--[[[end]]] (checksum: 3fc0e2ad4e283b885011628fe8edf568)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
mdformat-gfm==0.3.5
├── markdown-it-py [required: Any, installed: 2.1.0]
│   └── mdurl [required: ~=0.1, installed: 0.1.2]
├── mdformat [required: >=0.7.5,<0.8.0, installed: 0.7.16]
│   ├── markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.1.0]
│   │   └── mdurl [required: ~=0.1, installed: 0.1.2]
│   └── tomli [required: >=1.1.0, installed: 2.0.1]
├── mdformat-tables [required: >=0.4.0, installed: 0.4.1]
│   └── mdformat [required: >=0.7.5,<0.8.0, installed: 0.7.16]
│       ├── markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.1.0]
│       │   └── mdurl [required: ~=0.1, installed: 0.1.2]
│       └── tomli [required: >=1.1.0, installed: 2.0.1]
└── mdit-py-plugins [required: >=0.2.0,<0.4.0, installed: 0.3.3]
    └── markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.1.0]
        └── mdurl [required: ~=0.1, installed: 0.1.2]
pypandoc==1.11
typer==0.7.0
└── click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 414669fdae7e8161884a00d4a8ceee3d)-->
