# coding=utf-8
from django import template
from django.utils import translation

register = template.Library()


def burmese_numerals(parser, token):
    nodelist = parser.parse(('end_burmese_numerals',))
    parser.delete_first_token()
    return UpperNode(nodelist)


class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        if translation.get_language() == "my":
            return convert_num_to_mm(output)
        else:
            return output


@register.filter
def num_to_mm(value):  # convert english numerals into myanmar numerals
    if translation.get_language() == "my":
        return convert_num_to_mm(value)
    else:
        return value


def convert_num_to_mm(value):
    if value:
        intab = u"0123456789"
        outtab = u"၀၁၂၃၄၅၆၇၈၉"
        intab = [ord(char) for char in intab]
        translate_table = dict(zip(intab, outtab))
        return unicode(value).translate(translate_table)
    else:
        return value


register.tag('burmese_numerals', burmese_numerals)
