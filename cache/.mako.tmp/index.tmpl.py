# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1488385375.119067
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content_header', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        front_index_header = context.get('front_index_header', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context)
        front_index_header = context.get('front_index_header', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/index.tmpl", "line_map": {"201": 53, "196": 48, "193": 45, "23": 4, "141": 14, "146": 15, "147": 16, "148": 17, "149": 17, "150": 17, "151": 19, "152": 20, "153": 20, "26": 2, "155": 22, "156": 23, "29": 3, "158": 24, "159": 24, "160": 26, "161": 26, "162": 26, "35": 0, "164": 29, "165": 30, "166": 30, "167": 30, "168": 30, "169": 30, "170": 31, "171": 32, "172": 32, "173": 32, "174": 34, "157": 24, "176": 35, "177": 35, "178": 35, "179": 35, "180": 35, "181": 35, "182": 35, "183": 36, "184": 37, "185": 37, "186": 37, "187": 39, "188": 41, "189": 42, "190": 43, "191": 43, "192": 44, "65": 2, "66": 3, "67": 4, "68": 5, "197": 51, "198": 52, "199": 52, "194": 46, "73": 12, "202": 54, "175": 35, "78": 55, "209": 203, "163": 26, "84": 7, "203": 54, "94": 7, "95": 8, "96": 8, "97": 9, "98": 10, "99": 10, "100": 10, "195": 46, "106": 15, "154": 20, "117": 14, "200": 53}}
__M_END_METADATA
"""
