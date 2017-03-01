# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1488385374.869988
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_link_script', 'comment_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        disqus = _mako_get_namespace(context, 'disqus')
        muut = _mako_get_namespace(context, 'muut')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link(link, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        livefyre = _mako_get_namespace(context, 'livefyre')
        disqus = _mako_get_namespace(context, 'disqus')
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        comment_system = context.get('comment_system', UNDEFINED)
        muut = _mako_get_namespace(context, 'muut')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        facebook = _mako_get_namespace(context, 'facebook')
        isso = _mako_get_namespace(context, 'isso')
        disqus = _mako_get_namespace(context, 'disqus')
        muut = _mako_get_namespace(context, 'muut')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_form(url, title, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "comments_helper.tmpl", "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "line_map": {"23": 4, "26": 9, "29": 8, "32": 3, "35": 5, "38": 7, "41": 6, "44": 0, "49": 2, "50": 3, "51": 4, "52": 5, "53": 6, "54": 7, "55": 8, "56": 9, "57": 27, "58": 45, "59": 63, "65": 29, "77": 29, "78": 30, "79": 31, "80": 31, "81": 31, "82": 32, "83": 33, "84": 33, "85": 33, "86": 34, "87": 35, "88": 35, "89": 35, "90": 36, "91": 37, "92": 37, "93": 37, "94": 38, "95": 39, "96": 39, "97": 39, "98": 40, "99": 41, "100": 41, "101": 41, "102": 42, "103": 43, "104": 43, "105": 43, "111": 47, "123": 47, "124": 48, "125": 49, "126": 49, "127": 49, "128": 50, "129": 51, "130": 51, "131": 51, "132": 52, "133": 53, "134": 53, "135": 53, "136": 54, "137": 55, "138": 55, "139": 55, "140": 56, "141": 57, "142": 57, "143": 57, "144": 58, "145": 59, "146": 59, "147": 59, "148": 60, "149": 61, "150": 61, "151": 61, "157": 11, "169": 11, "170": 12, "171": 13, "172": 13, "173": 13, "174": 14, "175": 15, "176": 15, "177": 15, "178": 16, "179": 17, "180": 17, "181": 17, "182": 18, "183": 19, "184": 19, "185": 19, "186": 20, "187": 21, "188": 21, "189": 21, "190": 22, "191": 23, "192": 23, "193": 23, "194": 24, "195": 25, "196": 25, "197": 25, "203": 197}}
__M_END_METADATA
"""
