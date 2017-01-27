# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485545381.4692662
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        prevlink = context.get('prevlink', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        posts = context.get('posts', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        front_index_header = context.get('front_index_header', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
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
        parent = context.get('parent', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        date_format = context.get('date_format', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context)
        prevlink = context.get('prevlink', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        posts = context.get('posts', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        front_index_header = context.get('front_index_header', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
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


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"130": 14, "135": 15, "136": 16, "137": 17, "138": 17, "139": 17, "140": 19, "141": 20, "142": 20, "143": 20, "144": 22, "145": 23, "146": 24, "147": 24, "148": 24, "149": 26, "150": 26, "23": 2, "152": 26, "153": 29, "26": 3, "155": 30, "156": 30, "29": 4, "158": 30, "159": 31, "160": 32, "161": 32, "162": 32, "35": 0, "164": 35, "165": 35, "166": 35, "167": 35, "168": 35, "169": 35, "170": 35, "171": 35, "172": 36, "173": 37, "174": 37, "157": 30, "176": 39, "177": 41, "178": 42, "179": 43, "180": 43, "181": 44, "182": 45, "183": 46, "184": 46, "185": 48, "186": 51, "187": 52, "151": 26, "189": 53, "190": 53, "191": 54, "192": 54, "65": 2, "66": 3, "67": 4, "68": 5, "198": 15, "73": 12, "175": 37, "78": 55, "209": 198, "163": 34, "84": 7, "94": 7, "95": 8, "96": 8, "97": 9, "98": 10, "99": 10, "100": 10, "188": 52, "106": 14, "154": 30}}
__M_END_METADATA
"""
