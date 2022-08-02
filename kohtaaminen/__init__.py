"""Meeting, rendezvous, confluence (Finnish: kohtaaminen) mark up, down, and up again."""
# [[[fill git_describe()]]]
__version__ = '2022.8.2+parent.4c17cf8f'
# [[[end]]] (checksum: eaa209e5e7a90c217df25f8d1c12f751)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
