# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1524295799.9837017
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['feed_link', 'head', 'translation_link']


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


def render_feed_link(context,classification):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
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
        messages = context.get('messages', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 48, "23": 76, "24": 91, "30": 50, "42": 50, "43": 51, "44": 52, "45": 53, "46": 54, "47": 55, "48": 56, "49": 56, "50": 56, "51": 56, "52": 56, "53": 56, "54": 56, "55": 56, "56": 56, "57": 58, "58": 59, "59": 59, "60": 59, "61": 59, "62": 59, "63": 59, "64": 59, "65": 59, "66": 59, "67": 61, "68": 64, "69": 65, "70": 66, "71": 67, "72": 68, "73": 68, "74": 68, "75": 68, "76": 68, "77": 70, "78": 71, "79": 71, "80": 71, "81": 71, "82": 71, "83": 73, "89": 4, "103": 4, "104": 5, "105": 6, "106": 6, "107": 6, "108": 8, "109": 9, "110": 10, "111": 11, "112": 12, "113": 12, "114": 12, "115": 12, "116": 12, "117": 12, "118": 12, "119": 12, "120": 12, "121": 14, "122": 15, "123": 15, "124": 15, "125": 15, "126": 15, "127": 15, "128": 15, "129": 15, "130": 15, "131": 17, "132": 18, "133": 19, "134": 19, "135": 19, "136": 19, "137": 19, "138": 21, "139": 22, "140": 22, "141": 22, "142": 22, "143": 22, "144": 26, "145": 27, "146": 28, "147": 29, "148": 29, "149": 29, "150": 29, "151": 29, "152": 29, "153": 29, "154": 31, "155": 32, "156": 32, "157": 32, "158": 32, "159": 32, "160": 32, "161": 32, "162": 34, "163": 35, "164": 36, "165": 36, "166": 36, "167": 38, "168": 39, "169": 39, "170": 39, "171": 43, "172": 44, "173": 45, "174": 45, "175": 45, "176": 45, "177": 45, "183": 78, "192": 78, "193": 79, "194": 80, "195": 81, "196": 81, "197": 82, "198": 83, "199": 83, "200": 83, "201": 83, "202": 83, "203": 84, "204": 85, "205": 85, "206": 85, "207": 87, "208": 89, "214": 208}, "uri": "feeds_translations_helper.tmpl"}
__M_END_METADATA
"""
