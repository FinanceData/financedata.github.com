# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486952045.3018186
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap3/templates/pagination_helper.tmpl'
_template_uri = 'pagination_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['page_navigation']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_navigation(context,current_page,page_links,prevlink,nextlink,prev_next_links_reversed,surrounding=5):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        abs = context.get('abs', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<nav aria-label="Page navigation">\n  <ul class="pagination">\n')
        if prev_next_links_reversed:
            if nextlink:
                __M_writer('      <li><a href="')
                __M_writer(str(nextlink))
                __M_writer('" aria-label="')
                __M_writer(str(messages("Older posts")))
                __M_writer('"><span aria-hidden="true">&laquo;</span></a></li>\n')
            else:
                __M_writer('      <li class="disabled"><a href="#" aria-label="')
                __M_writer(str(messages("Older posts")))
                __M_writer('"><span aria-hidden="true">&laquo;</span></a></li>\n')
        else:
            if prevlink:
                __M_writer('      <li><a href="')
                __M_writer(str(prevlink))
                __M_writer('" aria-label="')
                __M_writer(str(messages("Newer posts")))
                __M_writer('"><span aria-hidden="true">&laquo;</span></a></li>\n')
            else:
                __M_writer('      <li class="disabled"><a href="#" aria-label="')
                __M_writer(str(messages("Newer posts")))
                __M_writer('"><span aria-hidden="true">&laquo;</span></a></li>\n')
        for i, link in enumerate(page_links):
            if abs(i - current_page) <= surrounding or i == 0 or i == len(page_links) - 1:
                __M_writer('      <li ')
                __M_writer(str(' class="active"' if i == current_page else ''))
                __M_writer('><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(i + 1))
                __M_writer(str(' <span class="sr-only">(current)</span>' if i == current_page else ''))
                __M_writer('</a></li>\n')
            elif i == current_page - surrounding - 1 or i == current_page + surrounding + 1:
                __M_writer('      <li class="disabled"><a href="#" aria-label="…"><span aria-hidden="true">…</span></a></li>\n')
        if prev_next_links_reversed:
            if prevlink:
                __M_writer('      <li><a href="')
                __M_writer(str(prevlink))
                __M_writer('" aria-label="')
                __M_writer(str(messages("Newer posts")))
                __M_writer('"><span aria-hidden="true">&raquo;</span></a></li>\n')
            else:
                __M_writer('      <li class="disabled"><a href="#" aria-label="')
                __M_writer(str(messages("Newer posts")))
                __M_writer('"><span aria-hidden="true">&raquo;</span></a></li>\n')
        else:
            if nextlink:
                __M_writer('      <li><a href="')
                __M_writer(str(nextlink))
                __M_writer('" aria-label="')
                __M_writer(str(messages("Older posts")))
                __M_writer('"><span aria-hidden="true">&raquo;</span></a></li>\n')
            else:
                __M_writer('      <li class="disabled"><a href="#" aria-label="')
                __M_writer(str(messages("Older posts")))
                __M_writer('"><span aria-hidden="true">&raquo;</span></a></li>\n')
        __M_writer('  </ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 40, "27": 2, "35": 2, "36": 5, "37": 6, "38": 7, "39": 7, "40": 7, "41": 7, "42": 7, "43": 8, "44": 9, "45": 9, "46": 9, "47": 11, "48": 12, "49": 13, "50": 13, "51": 13, "52": 13, "53": 13, "54": 14, "55": 15, "56": 15, "57": 15, "58": 18, "59": 19, "60": 20, "61": 20, "62": 20, "63": 20, "64": 20, "65": 20, "66": 20, "67": 20, "68": 21, "69": 22, "70": 25, "71": 26, "72": 27, "73": 27, "74": 27, "75": 27, "76": 27, "77": 28, "78": 29, "79": 29, "80": 29, "81": 31, "82": 32, "83": 33, "84": 33, "85": 33, "86": 33, "87": 33, "88": 34, "89": 35, "90": 35, "91": 35, "92": 38, "98": 92}, "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap3/templates/pagination_helper.tmpl", "uri": "pagination_helper.tmpl"}
__M_END_METADATA
"""
