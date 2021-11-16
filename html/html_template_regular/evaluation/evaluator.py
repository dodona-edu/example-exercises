from validators.checks import HtmlSuite, TestSuite, ChecklistItem


def create_suites(content: str) -> list[TestSuite]:
    html = HtmlSuite(content)

    el_html = html.element("html")
    el_head = el_html.get_child("head")
    # el_meta = html.element("html>head>meta") # Same but with Emmet syntax
    # el_meta = html.get_child('head').get_child('meta') # Same but with Emmet syntax
    el_meta = el_head.get_child('meta')
    # el_title = html.element("html>head>title") # Same but with Emmet syntax
    el_title = el_head.get_child("title")
    el_body = el_html.get_child("body")

    html.make_item("The document coding is specified.", html.has_doctype())

    html.make_item("<html> has a language attribute.",
                   el_html.attribute_exists('lang'))

    html.make_item("Inside the <html> tag is the <head> tag.",
                   el_head.exists())

    html.make_item("Inside the <head> tag is the <title> tag.",
                   el_title.exists())

    html.make_item("The <title> tag has content.",
                   html.element('title').has_content())

    html.make_item("Inside the <head> tag is the <meta> tag.",
                   el_meta.exists())

    html.make_item("<meta> has the 'UTF-8' charset attribute.",
                   html.element('meta', charset=True).attribute_exists('charset', "UTF-8", case_insensitive=True))

    html.make_item("Inside the <html> tag is the <body> tag.",
                   el_body.exists())

    html.translations["nl"] = [
        "De document codering is gespecifieerd.",
        "<html> heeft een taal attribuut.",
        "Binnen de <html> tag zit de <head> tag.",
        "Binnen de <head> tag zit de <title> tag.",
        "De <title> tag bevat tekst.",
        "Binnen de <head> tag zit de <meta> tag.",
        "<meta> heeft het UTF-8 charset attribuut.",
        "Binnen de <html> tag zit de <body> tag."
    ]

    return [html]
