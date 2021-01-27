Add custom icons from URL or path
=================================

Simple extension to easily add icons.

## Example

```python
import markdown
from mdx_iconify import IconifyExtension

md = 'Iconify :i:qgis:svgbase/worldmap:'

html = markdown.markdown(md, extensions=[IconifyExtension(
    width='1.2rem', 
    height='1.2rem',
    patterns={
        'qgis': {
            'prefix': 'https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/', 
            'suffix': '.svg',
            'check_suffix': True,
        }
    }
)])

print(html)
# <p>Iconify <img alt=":i:qgis:svgbase/worldmap:" height="1.2rem" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/svgbase/worldmap.svg" width="1.2rem" /></p>

```