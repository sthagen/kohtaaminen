"""Meeting, rendezvous, confluence (Finnish: kohtaaminen) mark up, down, and up again."""
# [[[fill git_describe()]]]
__version__ = '2022.8.2+parent.39e50623'
# [[[end]]] (checksum: 4893823d414c2d277f8cb05be925f1b3)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
