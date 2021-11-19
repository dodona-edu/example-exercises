# Import all necessary modules (same for every exercise)
from validators.checks import HtmlSuite, CssSuite, TestSuite, ChecklistItem


def create_suites(content: str) -> list[TestSuite]:
    # Create test suite for HTML with basic validator included
    html = HtmlSuite(content)

    # Description first, Emmet syntax thereafter, `>` means direct child
    html.make_item_from_emmet("Inside the <html> tag is the <head> tag.",
                              "html>head")

    html.make_item_from_emmet("Inside the <head> tag is the <meta> tag.",
                              "head>meta")

    html.make_item_from_emmet("Inside the <head> tag is the <title> tag.",
                              "head>title")

    html.make_item_from_emmet("Inside the <html> tag is the <body> tag.",
                              "html>body")

    # Select the body element in the students' submission
    body = html.element("body")
    # Get the first direct child of body
    a_link = body.get_child('a')

    html.make_item("Added the tag responsible for the link to the page.",
                   a_link.exists())  # Check if the link exists

    # One description can have multiple checks separated by a comma
    html.make_item("A path to which the link refers is indicated; "
                   "the path can be selected by any.",
                   a_link.attribute_exists('href'),  # Check if there is a reference
                   a_link.has_child()  # Check if the link has any child
                   )

    # Find an img element, which is a direct child of an a-tag, which is a direct child of an body-tag
    # with attributes src an alt
    img = html.element("body>a>img", src=True, alt=True)

    html.make_item("Added an image as a link; a path to the image is indicated; "
                   "specified alternative text for the image.",
                   img.exists())

    html.make_item("The image is correct.",
                   img.attribute_contains("src", "https://dodona.ugent.be/icon.png"),
                   img.attribute_exists("alt", "Dodona logo"))

    html.make_item("The link is correct.",
                   a_link.attribute_contains("href", "https://dodona.ugent.be/nl/support-us/"))

    html.translations["nl"] = [
        "Binnen de <html> tag zit de <head> tag.",
        "Binnen de <head> tag zit de <meta> tag.",
        "Binnen de <head> tag zit de <title> tag.",
        "Binnen de <html> tag zit de <body> tag.",
        "De tag die verantwoordelijk is voor de link naar de pagina is toegevoegd.",
        "Het adres waar de link naar verwijst is aanwezig; "
        "het adres kan bereikt worden door op iets te klikken.",
        "Een afbeelding is als link toegevoegd; er is een link naar een afbeelding aanwezig; "
        "alternatieve tekst voor de afbeelding is gespecifieerd.",
        "De afbeelding is correct.",
        "De link is correct."
    ]

    return [html]
