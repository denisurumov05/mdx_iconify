import xml.etree.ElementTree as etree

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension


class IconifyInlineProcessor(InlineProcessor):
    def __init__(self, pattern, md, config):
        super().__init__(pattern, md)
        self.config = config

    def handleMatch(self, m, data):
        config = self.config.get('patterns', {}).get(m.group(1))

        if not config:
            return (None, None, None)

        prefix = config.get('prefix', '')
        suffix = config.get('suffix', '')
        check_suffix = config.get('check_suffix', True)
        width = config.get('width', self.config.get('width', ''))
        height = config.get('height', self.config.get('height', ''))

        if check_suffix and m.group(2).endswith(suffix):
            suffix = ''

        el = etree.Element('img')
        el.set('src', prefix + m.group(2) + suffix)
        el.set('alt', m.group(0))

        if width:
            el.set('width', width)
        if height:
            el.set('height', height)

        el.text = m.group(1)
        return el, m.start(0), m.end(0)


class IconifyExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'width' : ['', 'Default width for all icons.'],
            'height' : ['', 'Default height for all icons.'],
            'patterns' : [{}, 'Patterns to match, organized as {"namespace": {"prefix": <str>, "suffix": <str>, "check_suffix": <bool>]}.']
        }
        super(IconifyExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        ICONIFY_PATTERN = r':i:(.*?):(.*?):'
        md.inlinePatterns.register(IconifyInlineProcessor(ICONIFY_PATTERN, md, self.getConfigs()), 'img', 175)

def makeExtension(*args, **kwargs):
    return IconifyExtension(*args, **kwargs)
