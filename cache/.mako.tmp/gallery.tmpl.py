# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493746872.4000971
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap3/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'sourcelink', 'extra_js', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        def content():
            return render_content(context)
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ul>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i>&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" /></a>\n')
            __M_writer('</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/flowr.plugin.js"></script>\n<script>\njsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\n$("#gallery_container").flowr({\n        data : jsonContent,\n        height : ')
        __M_writer(str(thumbnail_size))
        __M_writer('*.6,\n        padding: 5,\n        rows: -1,\n        render : function(params) {\n            // Just return a div, string or a dom object, anything works fine\n            img = $("<img />").attr({\n                \'src\': params.itemData.url_thumb,\n                \'width\' : params.width,\n                \'height\' : params.height\n            }).css(\'max-width\', \'100%\');\n            link = $( "<a></a>").attr({\n                \'href\': params.itemData.url,\n                \'class\': \'image-reference\'\n            });\n            div = $("<div />").addClass(\'image-block\').attr({\n                \'title\': params.itemData.title,\n                \'data-toggle\': "tooltip",\n            });\n            link.append(img);\n            div.append(link);\n            div.hover(div.tooltip());\n            return div;\n        },\n        itemWidth : function(data) { return data.size.w; },\n        itemHeight : function(data) { return data.size.h; },\n        complete : function(params) {\n            if( jsonContent.length > params.renderedItems ) {\n                nextRenderList = jsonContent.slice( params.renderedItems );\n            }\n        }\n    });\n$("a.image-reference").colorbox({rel:"gal", maxWidth:"100%",maxHeight:"100%",scalePhotos:true});\n$(\'a.image-reference[href="\'+window.location.hash.substring(1,1000)+\'"]\').click();\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    .image-block {\n        display: inline-block;\n    }\n    .flowr_row {\n        width: 100%;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap3/templates/gallery.tmpl", "uri": "gallery.tmpl", "line_map": {"128": 27, "129": 29, "130": 30, "131": 30, "132": 30, "133": 30, "134": 30, "135": 31, "136": 31, "137": 31, "138": 31, "139": 33, "140": 36, "141": 37, "142": 37, "148": 5, "23": 4, "26": 3, "32": 0, "161": 55, "171": 55, "172": 58, "173": 58, "174": 61, "175": 61, "181": 41, "60": 2, "61": 3, "62": 4, "191": 42, "192": 42, "67": 5, "198": 192, "72": 39, "77": 52, "190": 41, "82": 95, "88": 7, "106": 7, "107": 8, "108": 8, "109": 9, "110": 10, "111": 10, "112": 10, "113": 12, "114": 13, "115": 14, "116": 14, "117": 17, "118": 18, "119": 19, "120": 20, "121": 20, "122": 20, "123": 20, "124": 20, "125": 22, "126": 24, "127": 26}}
__M_END_METADATA
"""
