# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1524296235.1159015
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_form', 'comment_link']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

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


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        isso = _mako_get_namespace(context, 'isso')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        livefyre = _mako_get_namespace(context, 'livefyre')
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
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        comment_system = context.get('comment_system', UNDEFINED)
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        livefyre = _mako_get_namespace(context, 'livefyre')
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


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        comment_system = context.get('comment_system', UNDEFINED)
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        livefyre = _mako_get_namespace(context, 'livefyre')
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


"""
__M_BEGIN_METADATA
{"uri": "comments_helper.tmpl", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "line_map": {"23": 5, "26": 6, "29": 9, "32": 8, "35": 4, "38": 3, "41": 7, "44": 0, "49": 2, "50": 3, "51": 4, "52": 5, "53": 6, "54": 7, "55": 8, "56": 9, "57": 27, "58": 45, "59": 63, "65": 47, "77": 47, "78": 48, "79": 49, "80": 49, "81": 49, "82": 50, "83": 51, "84": 51, "85": 51, "86": 52, "87": 53, "88": 53, "89": 53, "90": 54, "91": 55, "92": 55, "93": 55, "94": 56, "95": 57, "96": 57, "97": 57, "98": 58, "99": 59, "100": 59, "101": 59, "102": 60, "103": 61, "104": 61, "105": 61, "111": 11, "123": 11, "124": 12, "125": 13, "126": 13, "127": 13, "128": 14, "129": 15, "130": 15, "131": 15, "132": 16, "133": 17, "134": 17, "135": 17, "136": 18, "137": 19, "138": 19, "139": 19, "140": 20, "141": 21, "142": 21, "143": 21, "144": 22, "145": 23, "146": 23, "147": 23, "148": 24, "149": 25, "150": 25, "151": 25, "157": 29, "169": 29, "170": 30, "171": 31, "172": 31, "173": 31, "174": 32, "175": 33, "176": 33, "177": 33, "178": 34, "179": 35, "180": 35, "181": 35, "182": 36, "183": 37, "184": 37, "185": 37, "186": 38, "187": 39, "188": 39, "189": 39, "190": 40, "191": 41, "192": 41, "193": 41, "194": 42, "195": 43, "196": 43, "197": 43, "203": 197}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
