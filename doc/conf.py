from documenteer.sphinxconfig.stackconf import build_package_configs

_g=globals()
_g.update(build_package_configs(
    project_name='TSSW Developer Guide',version="current"))

extensions.append('sphinx.ext.autosectionlabel')
autosectionlabel_prefix_document=True

intersphinx_mapping['dm_developer_guide'] = ('https://developer.lsst.io', None)
