from validators.checks import HtmlSuite, TestSuite, ChecklistItem


def create_suites(content: str) -> list[TestSuite]:
    html = HtmlSuite(content)

    html.make_item("The document coding is specified.", html.has_doctype())

    html.make_item_from_emmet("<html> has a language attribute.",
                              'html[lang="DUMMY"]')

    html.make_item_from_emmet("Inside the <html> tag is the <head> tag.",
                              "html>head")

    html.make_item_from_emmet("Inside the <head> tag is the <title> tag.",
                              "html>head>title")

    html.make_item_from_emmet("The <title> tag has content.",
                              "title{DUMMY}")

    html.make_item_from_emmet("Inside the <head> tag is the <meta> tag.",
                              "html>head>meta")

    html.make_item_from_emmet("<meta> has the 'UTF-8' charset attribute.",
                              "meta[charset='UTF-8']")  # TODO case insensitive option

    html.make_item_from_emmet("Inside the <html> tag is the <body> tag.",
                              "html>body")

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
