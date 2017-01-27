# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485549254.2272182
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['meta_translations', 'mathjax_script', 'twitter_card_information', 'open_graph_metadata', 'html_tags', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and ((not post.skip_untranslated) or post.is_translation_available(langname)):
                    __M_writer('                <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.is_mathjax:
            if use_katex:
                __M_writer('            <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.js"></script>\n            <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/contrib/auto-render.min.js"></script>\n')
                if katex_auto_render:
                    __M_writer('                <script>\n                    renderMathInElement(document.body,\n                        {\n                            ')
                    __M_writer(str(katex_auto_render))
                    __M_writer('\n                        }\n                    );\n                </script>\n')
                else:
                    __M_writer('                <script>\n                    renderMathInElement(document.body);\n                </script>\n')
            else:
                __M_writer('            <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n')
                if mathjax_config:
                    __M_writer('            ')
                    __M_writer(str(mathjax_config))
                    __M_writer('\n')
                else:
                    __M_writer('            <script type="text/x-mathjax-config">\n            MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n            </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        url_replacer = context.get('url_replacer', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_open_graph:
            __M_writer('    <meta property="og:site_name" content="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n    <meta property="og:title" content="')
            __M_writer(filters.html_escape(str(post.title()[:70])))
            __M_writer('">\n    <meta property="og:url" content="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
            if post.description():
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.description()[:200])))
                __M_writer('">\n')
            else:
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
                __M_writer('">\n')
            if post.previewimage:
                __M_writer('    <meta property="og:image" content="')
                __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer('">\n')
            __M_writer('    <meta property="og:type" content="article">\n')
            if post.date.isoformat():
                __M_writer('    <meta property="article:published_time" content="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('">\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('           <meta property="article:tag" content="')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('        <ul itemprop="keywords" class="tags">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('            <li><a class="tag p-category" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.prev_post or post.next_post:
            __M_writer('        <ul class="pager hidden-print">\n')
            if post.prev_post:
                __M_writer('            <li class="previous">\n                <a href="')
                __M_writer(str(post.prev_post.permalink()))
                __M_writer('" rel="prev" title="')
                __M_writer(filters.html_escape(str(post.prev_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Previous post")))
                __M_writer('</a>\n            </li>\n')
            if post.next_post:
                __M_writer('            <li class="next">\n                <a href="')
                __M_writer(str(post.next_post.permalink()))
                __M_writer('" rel="next" title="')
                __M_writer(filters.html_escape(str(post.next_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Next post")))
                __M_writer('</a>\n            </li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/post_helper.tmpl", "uri": "post_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 11, "23": 23, "24": 40, "25": 69, "26": 85, "27": 116, "33": 3, "41": 3, "42": 4, "43": 5, "44": 6, "45": 7, "46": 7, "47": 7, "48": 7, "49": 7, "55": 87, "62": 87, "63": 88, "64": 89, "65": 90, "66": 92, "67": 93, "68": 96, "69": 96, "70": 100, "71": 101, "72": 105, "73": 106, "74": 107, "75": 108, "76": 108, "77": 108, "78": 109, "79": 110, "85": 71, "90": 71, "91": 72, "92": 73, "93": 73, "94": 73, "95": 74, "96": 75, "97": 75, "98": 75, "99": 76, "100": 77, "101": 77, "102": 77, "103": 79, "104": 80, "105": 80, "106": 80, "107": 81, "108": 82, "109": 82, "110": 82, "116": 42, "126": 42, "127": 43, "128": 44, "129": 44, "130": 44, "131": 45, "132": 45, "133": 46, "134": 46, "135": 47, "136": 48, "137": 48, "138": 48, "139": 49, "140": 50, "141": 50, "142": 50, "143": 52, "144": 53, "145": 53, "146": 53, "147": 55, "148": 60, "149": 61, "150": 61, "151": 61, "152": 63, "153": 64, "154": 65, "155": 65, "156": 65, "162": 13, "168": 13, "169": 14, "170": 15, "171": 16, "172": 17, "173": 18, "174": 18, "175": 18, "176": 18, "177": 18, "178": 21, "184": 25, "189": 25, "190": 26, "191": 27, "192": 28, "193": 29, "194": 30, "195": 30, "196": 30, "197": 30, "198": 30, "199": 30, "200": 33, "201": 34, "202": 35, "203": 35, "204": 35, "205": 35, "206": 35, "207": 35, "208": 38, "214": 208}}
__M_END_METADATA
"""
