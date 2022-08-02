# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/laskea/blob/default/sbom.json) with SHA256 checksum ([c5ed1fce ...](https://raw.githubusercontent.com/sthagen/laskea/default/sbom.json.sha256 "sha256:c5ed1fce48787e6ce9f8e4bbce942f07948d5681ad1650f15ad3b1c979b81a13")).
<!--[[[end]]] (checksum: 7586bb8c1459b2259ca7477129bd3146)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                     | Version                                               | License     | Author                            | Description (from packaging data)                                  |
|:---------------------------------------------------------|:------------------------------------------------------|:------------|:----------------------------------|:-------------------------------------------------------------------|
| [mdformat-gfm](https://github.com/hukkinj1/mdformat-gfm) | [0.3.5](https://pypi.org/project/mdformat-gfm/0.3.5/) | MIT License | Taneli Hukkinen                   | Mdformat plugin for GitHub Flavored Markdown compatibility         |
| [pypandoc](https://github.com/NicklasTegner/pypandoc)    | [1.8.1](https://pypi.org/project/pypandoc/1.8.1/)     | MIT License | b'Juho Veps\xc3\xa4l\xc3\xa4inen' | Thin wrapper for pandoc.                                           |
| [typer](https://github.com/tiangolo/typer)               | [0.4.2](https://pypi.org/project/typer/0.4.2/)        | MIT License | Sebastián Ramírez                 | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 0b61165d56e89e146429b5fc62e0eacb)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                           | Version                                                       | License                              | Author              | Description (from packaging data)                                                                       |
|:-----------------------------------------------------------------------------------------------|:--------------------------------------------------------------|:-------------------------------------|:--------------------|:--------------------------------------------------------------------------------------------------------|
| [attrs](https://www.attrs.org/)                                                                | [21.4.0](https://pypi.org/project/attrs/21.4.0/)              | MIT License                          | Hynek Schlawack     | Classes Without Boilerplate                                                                             |
| [certifi](https://github.com/certifi/python-certifi)                                           | [2022.6.15](https://pypi.org/project/certifi/2022.6.15/)      | Mozilla Public License 2.0 (MPL 2.0) | Kenneth Reitz       | Python package for providing Mozilla's CA Bundle.                                                       |
| [charset-normalizer](https://github.com/ousret/charset_normalizer)                             | [2.0.12](https://pypi.org/project/charset-normalizer/2.0.12/) | MIT License                          | Ahmed TAHRI @Ousret | The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet. |
| [click](https://palletsprojects.com/p/click/)                                                  | [8.1.3](https://pypi.org/project/click/8.1.3/)                | BSD License                          | Armin Ronacher      | Composable command line interface toolkit                                                               |
| [idna](https://github.com/kjd/idna)                                                            | [3.3](https://pypi.org/project/idna/3.3/)                     | BSD License                          | Kim Davies          | Internationalized Domain Names in Applications (IDNA)                                                   |
| [requests](https://requests.readthedocs.io)                                                    | [2.28.0](https://pypi.org/project/requests/2.28.0/)           | Apache Software License              | Kenneth Reitz       | Python HTTP for Humans.                                                                                 |
| [six](https://github.com/benjaminp/six)                                                        | [1.16.0](https://pypi.org/project/six/1.16.0/)                | MIT License                          | Benjamin Peterson   | Python 2 and 3 compatibility utilities                                                                  |
| [typing-extensions](https://github.com/python/typing/blob/master/typing_extensions/README.rst) | [4.2.0](https://pypi.org/project/typing-extensions/4.2.0/)    | Python Software Foundation License   | UNKNOWN             | Backported and Experimental Type Hints for Python 3.7+                                                  |
| [urllib3](https://urllib3.readthedocs.io/)                                                     | [1.26.9](https://pypi.org/project/urllib3/1.26.9/)            | MIT License                          | Andrey Petrov       | HTTP library with thread-safe connection pooling, file post, and more.                                  |
| [wrapt](https://github.com/GrahamDumpleton/wrapt)                                              | [1.14.1](https://pypi.org/project/wrapt/1.14.1/)              | BSD License                          | Graham Dumpleton    | Module for decorators, wrappers and monkey patching.                                                    |
<!--[[[end]]] (checksum: e9615c18969f2d168527de583ecbcecf)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="https://raw.githubusercontent.com/sthagen/pilli/default/docs/third-party/package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
mdformat-gfm==0.3.5
  - markdown-it-py [required: Any, installed: 2.1.0]
    - mdurl [required: ~=0.1, installed: 0.1.1]
  - mdformat [required: >=0.7.5,<0.8.0, installed: 0.7.14]
    - importlib-metadata [required: >=3.6.0, installed: 4.11.4]
      - zipp [required: >=0.5, installed: 3.8.0]
    - markdown-it-py [required: >=1.0.0b2,<3.0.0, installed: 2.1.0]
      - mdurl [required: ~=0.1, installed: 0.1.1]
    - tomli [required: >=1.1.0, installed: 2.0.1]
  - mdformat-tables [required: >=0.4.0, installed: 0.4.1]
    - mdformat [required: >=0.7.5,<0.8.0, installed: 0.7.14]
      - importlib-metadata [required: >=3.6.0, installed: 4.11.4]
        - zipp [required: >=0.5, installed: 3.8.0]
      - markdown-it-py [required: >=1.0.0b2,<3.0.0, installed: 2.1.0]
        - mdurl [required: ~=0.1, installed: 0.1.1]
      - tomli [required: >=1.1.0, installed: 2.0.1]
  - mdit-py-plugins [required: >=0.2.0,<0.4.0, installed: 0.3.0]
    - markdown-it-py [required: >=1.0.0,<3.0.0, installed: 2.1.0]
      - mdurl [required: ~=0.1, installed: 0.1.1]
pypandoc==1.8.1
typer==0.4.2
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 5aa5c6972224d972f96156d5c1ddb088)-->
