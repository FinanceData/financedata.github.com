# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527496260.1836493
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['translation_link', 'feed_link', 'head']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_translation_link(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        other_languages = context.get('other_languages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if has_other_languages and other_languages:
            __M_writer('        <div class="translationslist translations">\n            <h3 class="translationslist-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for language, classification, name in other_languages:
                __M_writer('            <p><a href="')
                __M_writer(str(_link(kind, classification, language)))
                __M_writer('" rel="alternate">')
                __M_writer(str(messages("LANGUAGE", language)))
                __M_writer('\n')
                if kind != 'archive':
                    __M_writer('                (')
                    __M_writer(filters.html_escape(str(name)))
                    __M_writer(')\n')
                __M_writer('            </a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_feed_link(context,classification):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for language in sorted(translations):
                if generate_atom or generate_rss:
                    __M_writer('                <p class="feedlink">\n')
                    if generate_atom:
                        __M_writer('                        <a href="')
                        __M_writer(str(_link(kind + "_atom", classification, language)))
                        __M_writer('" hreflang="')
                        __M_writer(str(language))
                        __M_writer('" type="application/atom+xml">')
                        __M_writer(str(messages('Atom feed', language)))
                        __M_writer(' (')
                        __M_writer(str(language))
                        __M_writer(')</a>\n')
                    if generate_rss:
                        __M_writer('                        <a href="')
                        __M_writer(str(_link(kind + "_rss", classification, language)))
                        __M_writer('" hreflang="')
                        __M_writer(str(language))
                        __M_writer('" type="application/rss+xml">')
                        __M_writer(str(messages('RSS feed', language)))
                        __M_writer(' (')
                        __M_writer(str(language))
                        __M_writer(')</a>\n')
                    __M_writer('                </p>\n')
        else:
            if generate_atom or generate_rss:
                __M_writer('            <p class="feedlink">\n')
                if generate_atom:
                    __M_writer('                    <a href="')
                    __M_writer(str(_link(kind + "_atom", classification)))
                    __M_writer('" type="application/atom+xml">')
                    __M_writer(str(messages('Atom feed')))
                    __M_writer('</a>\n')
                if generate_rss:
                    __M_writer('                    <a href="')
                    __M_writer(str(_link(kind + "_rss", classification)))
                    __M_writer('" type="application/rss+xml">')
                    __M_writer(str(messages('RSS feed')))
                    __M_writer('</a>\n')
                __M_writer('            </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,classification=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        if len(translations) > 1:
            for language in sorted(translations):
                if classification:
                    if generate_atom:
                        __M_writer('                    <link rel="alternate" type="application/atom+xml" title="Atom for ')
                        __M_writer(str(kind))
                        __M_writer(' ')
                        __M_writer(filters.html_escape(str(classification)))
                        __M_writer(' (')
                        __M_writer(str(language))
                        __M_writer(')" href="')
                        __M_writer(str(_link(kind + "_atom", classification, language)))
                        __M_writer('">\n')
                    if generate_rss and not rss_link:
                        __M_writer('                    <link rel="alternate" type="application/rss+xml" title="RSS for ')
                        __M_writer(str(kind))
                        __M_writer(' ')
                        __M_writer(filters.html_escape(str(classification)))
                        __M_writer(' (')
                        __M_writer(str(language))
                        __M_writer(')" href="')
                        __M_writer(str(_link(kind + "_rss", classification, language)))
                        __M_writer('">\n')
                else:
                    if generate_atom:
                        __M_writer('                    <link rel="alternate" type="application/atom+xml" title="Atom (')
                        __M_writer(str(language))
                        __M_writer(')" href="')
                        __M_writer(str(_link("index_atom", None, language)))
                        __M_writer('">\n')
                    if generate_rss and not rss_link:
                        __M_writer('                    <link rel="alternate" type="application/rss+xml" title="RSS (')
                        __M_writer(str(language))
                        __M_writer(')" href="')
                        __M_writer(str(_link("rss", None, language)))
                        __M_writer('">\n')
        else:
            if classification:
                if generate_atom:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(classification)))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_atom", classification)))
                    __M_writer('">\n')
                if generate_rss and not rss_link:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(classification)))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_rss", classification)))
                    __M_writer('">\n')
            else:
                if generate_atom:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                    __M_writer(str(_link("index_atom", None)))
                    __M_writer('">\n')
                if generate_rss and not rss_link:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                    __M_writer(str(_link("rss", None)))
                    __M_writer('">\n')
        if has_other_languages and other_languages:
            for language, classification, _ in other_languages:
                __M_writer('            <link rel="alternate" hreflang="')
                __M_writer(str(language))
                __M_writer('" href="')
                __M_writer(str(_link(kind, classification, language)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 2, "22": 48, "23": 76, "24": 91, "30": 78, "39": 78, "40": 79, "41": 80, "42": 81, "43": 81, "44": 82, "45": 83, "46": 83, "47": 83, "48": 83, "49": 83, "50": 84, "51": 85, "52": 85, "53": 85, "54": 87, "55": 89, "61": 50, "73": 50, "74": 51, "75": 52, "76": 53, "77": 54, "78": 55, "79": 56, "80": 56, "81": 56, "82": 56, "83": 56, "84": 56, "85": 56, "86": 56, "87": 56, "88": 58, "89": 59, "90": 59, "91": 59, "92": 59, "93": 59, "94": 59, "95": 59, "96": 59, "97": 59, "98": 61, "99": 64, "100": 65, "101": 66, "102": 67, "103": 68, "104": 68, "105": 68, "106": 68, "107": 68, "108": 70, "109": 71, "110": 71, "111": 71, "112": 71, "113": 71, "114": 73, "120": 4, "134": 4, "135": 5, "136": 6, "137": 6, "138": 6, "139": 8, "140": 9, "141": 10, "142": 11, "143": 12, "144": 12, "145": 12, "146": 12, "147": 12, "148": 12, "149": 12, "150": 12, "151": 12, "152": 14, "153": 15, "154": 15, "155": 15, "156": 15, "157": 15, "158": 15, "159": 15, "160": 15, "161": 15, "162": 17, "163": 18, "164": 19, "165": 19, "166": 19, "167": 19, "168": 19, "169": 21, "170": 22, "171": 22, "172": 22, "173": 22, "174": 22, "175": 26, "176": 27, "177": 28, "178": 29, "179": 29, "180": 29, "181": 29, "182": 29, "183": 29, "184": 29, "185": 31, "186": 32, "187": 32, "188": 32, "189": 32, "190": 32, "191": 32, "192": 32, "193": 34, "194": 35, "195": 36, "196": 36, "197": 36, "198": 38, "199": 39, "200": 39, "201": 39, "202": 43, "203": 44, "204": 45, "205": 45, "206": 45, "207": 45, "208": 45, "214": 208}, "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl", "uri": "feeds_translations_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
