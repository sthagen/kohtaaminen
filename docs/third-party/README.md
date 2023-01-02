# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/kohtaaminen/blob/default/sbom.json) with SHA256 checksum ([3fbdf822 ...](https://git.sr.ht/~sthagen/kohtaaminen/blob/default/sbom.json.sha256 "sha256:3fbdf82236ff17d3dbebaa3fcb7955af6ec964a35e9144ddbfe50ec2353a0549")).
<!--[[[end]]] (checksum: bea4ab5ff80094d94f5dfee1c9284ddb)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                     | Version                                               | License     | Author                            | Description (from packaging data)                                  |
|:---------------------------------------------------------|:------------------------------------------------------|:------------|:----------------------------------|:-------------------------------------------------------------------|
| [mdformat-gfm](https://github.com/hukkinj1/mdformat-gfm) | [0.3.5](https://pypi.org/project/mdformat-gfm/0.3.5/) | MIT License | Taneli Hukkinen                   | Mdformat plugin for GitHub Flavored Markdown compatibility         |
| [pypandoc](https://github.com/JessicaTegner/pypandoc)    | [1.10](https://pypi.org/project/pypandoc/1.10/)       | MIT License | b'Juho Veps\xc3\xa4l\xc3\xa4inen' | Thin wrapper for pandoc.                                           |
| [typer](https://github.com/tiangolo/typer)               | [0.7.0](https://pypi.org/project/typer/0.7.0/)        | MIT License | Sebastián Ramírez                 | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: f37fd37b44cd36e012fe1be11d28a98b)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                        | Version                                                  | License     | Author          | Description (from packaging data)                         |
|:--------------------------------------------------------------------------------------------|:---------------------------------------------------------|:------------|:----------------|:----------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                                               | [8.1.3](https://pypi.org/project/click/8.1.3/)           | BSD License | Armin Ronacher  | Composable command line interface toolkit                 |
| [markdown-it-py](https://github.com/executablebooks/markdown-it-py/blob/master/README.md)   | [2.1.0](https://pypi.org/project/markdown-it-py/2.1.0/)  | MIT License | Chris Sewell    | Python port of markdown-it. Markdown parsing, done right! |
| [mdformat](https://github.com/executablebooks/mdformat/blob/master/README.md)               | [0.7.16](https://pypi.org/project/mdformat/0.7.16/)      | MIT License | Taneli Hukkinen | CommonMark compliant Markdown formatter                   |
| [mdit-py-plugins](https://github.com/executablebooks/mdit-py-plugins/blob/master/README.md) | [0.3.3](https://pypi.org/project/mdit-py-plugins/0.3.3/) | MIT License | Chris Sewell    | Collection of plugins for markdown-it-py                  |
| [mdurl](https://github.com/executablebooks/mdurl/blob/master/README.md)                     | [0.1.2](https://pypi.org/project/mdurl/0.1.2/)           | MIT License | Taneli Hukkinen | Markdown URL utilities                                    |
| [tomli](https://github.com/hukkin/tomli/blob/master/README.md)                              | [2.0.1](https://pypi.org/project/tomli/2.0.1/)           | MIT License | Taneli Hukkinen | A lil' TOML parser                                        |
<!--[[[end]]] (checksum: aea85e007d6e95cd41f634706e1b3701)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
mdformat-gfm==0.3.5
  - markdown-it-py [required: Any, installed: 2.1.0]
    - mdurl [required: ~=0.1, installed: 0.1.2]
  - mdformat [required: >=0.7.5,<0.8.0, installed: 0.7.16]
    - markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.1.0]
      - mdurl [required: ~=0.1, installed: 0.1.2]
    - tomli [required: >=1.1.0, installed: 2.0.1]
  - mdformat-tables [required: >=0.4.0, installed: 0.4.1]
    - mdformat [required: >=0.7.5,<0.8.0, installed: 0.7.16]
      - markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.1.0]
        - mdurl [required: ~=0.1, installed: 0.1.2]
      - tomli [required: >=1.1.0, installed: 2.0.1]
  - mdit-py-plugins [required: >=0.2.0,<0.4.0, installed: 0.3.3]
    - markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.1.0]
      - mdurl [required: ~=0.1, installed: 0.1.2]
pypandoc==1.10
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 1e64b625dc83a221a4c7995372d74e72)-->
