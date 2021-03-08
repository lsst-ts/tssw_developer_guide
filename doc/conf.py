from documenteer.conf.pipelinespkg import *

project = "TSSW Developer Guide"
html_theme_options["logotext"] = project
html_title = project
html_short_title = project

extensions.append('sphinx.ext.autosectionlabel')
autosectionlabel_prefix_document=True

intersphinx_mapping['dm_developer_guide'] = ('https://developer.lsst.io', None)
