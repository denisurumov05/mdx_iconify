import unittest

from markdown import Markdown
from mdx_iconify import IconifyExtension

class TestComments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        iconify = IconifyExtension(
            width='1.2rem', 
            height='1.2rem',
            patterns={
                'qgis': {
                    'prefix': 'https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/', 
                    'suffix': '.svg',
                    'check_suffix': True,
                }
            }
        )
        cls.md = Markdown(extensions=[iconify])

    def test_simple(self):
        md_input = 'Iconify :i:qgis:svgbase/worldmap:'
        md_output = '<p>Iconify <img alt=":i:qgis:svgbase/worldmap:" height="1.2rem" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/svgbase/worldmap.svg" width="1.2rem" /></p>'
        self.assertEqual(self.md.convert(md_input), md_output)
    
    def test_not_existant(self):
        md_input = 'Iconify :i:nope:svgbase/worldmap:'
        md_output = '<p>Iconify :i:nope:svgbase/worldmap:</p>'
        self.assertEqual(self.md.convert(md_input), md_output)

    def test_check_suffix(self):
        md_input = 'Iconify :i:qgis:svgbase/worldmap.svg:'
        md_output = '<p>Iconify <img alt=":i:qgis:svgbase/worldmap.svg:" height="1.2rem" src="https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/svgbase/worldmap.svg" width="1.2rem" /></p>'
        self.assertEqual(self.md.convert(md_input), md_output)

if __name__ == '__main__':
    unittest.main()
