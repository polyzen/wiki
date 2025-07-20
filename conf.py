# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from importlib.util import find_spec

# -- Project information -----------------------------------------------------

project = 'Wiki'

# -- General configuration ---------------------------------------------------

extensions = [
  'myst_parser',
  'sphinxext.opengraph',
]

# Extension only used for deployments
if find_spec('sphinxext') is None:
    extensions.remove('sphinxext.opengraph')

exclude_patterns = ['_build']
source_suffix = { '.md': 'markdown' }
templates_path = ['_templates']

# -- Options for MyST --------------------------------------------------------

myst_enable_extensions = [
    'colon_fence',
    'deflist',
]

# -- Options for Open Graph --------------------------------------------------

ogp_site_url = 'https://wiki.lacto.se'
ogp_type = 'article'

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_theme_options = {
    'source_repository': 'https://gitlab.com/polyzen/wiki',
    'source_branch': 'master',
    'source_directory': '/',
}
html_title = project
html_favicon = '_static/favicon.svg'
html_static_path = ['_static']
html_use_index = False
html_copy_source = False

# -- Options for link checker ------------------------------------------------

linkcheck_ignore = ['https://tt-rss.org']
