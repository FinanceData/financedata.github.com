# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1540015154.3032765
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['head', 'translation_link', 'feed_link']


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


def render_head(context,classification=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


def render_translation_link(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        kind = context.get('kind', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
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
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 48, "23": 76, "24": 91, "30": 4, "44": 4, "45": 5, "46": 6, "47": 6, "48": 6, "49": 8, "50": 9, "51": 10, "52": 11, "53": 12, "54": 12, "55": 12, "56": 12, "57": 12, "58": 12, "59": 12, "60": 12, "61": 12, "62": 14, "63": 15, "64": 15, "65": 15, "66": 15, "67": 15, "68": 15, "69": 15, "70": 15, "71": 15, "72": 17, "73": 18, "74": 19, "75": 19, "76": 19, "77": 19, "78": 19, "79": 21, "80": 22, "81": 22, "82": 22, "83": 22, "84": 22, "85": 26, "86": 27, "87": 28, "88": 29, "89": 29, "90": 29, "91": 29, "92": 29, "93": 29, "94": 29, "95": 31, "96": 32, "97": 32, "98": 32, "99": 32, "100": 32, "101": 32, "102": 32, "103": 34, "104": 35, "105": 36, "106": 36, "107": 36, "108": 38, "109": 39, "110": 39, "111": 39, "112": 43, "113": 44, "114": 45, "115": 45, "116": 45, "117": 45, "118": 45, "124": 78, "133": 78, "134": 79, "135": 80, "136": 81, "137": 81, "138": 82, "139": 83, "140": 83, "141": 83, "142": 83, "143": 83, "144": 84, "145": 85, "146": 85, "147": 85, "148": 87, "149": 89, "155": 50, "167": 50, "168": 51, "169": 52, "170": 53, "171": 54, "172": 55, "173": 56, "174": 56, "175": 56, "176": 56, "177": 56, "178": 56, "179": 56, "180": 56, "181": 56, "182": 58, "183": 59, "184": 59, "185": 59, "186": 59, "187": 59, "188": 59, "189": 59, "190": 59, "191": 59, "192": 61, "193": 64, "194": 65, "195": 66, "196": 67, "197": 68, "198": 68, "199": 68, "200": 68, "201": 68, "202": 70, "203": 71, "204": 71, "205": 71, "206": 71, "207": 71, "208": 73, "214": 208}, "uri": "feeds_translations_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
