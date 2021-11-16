from validators.checks import HtmlSuite, CssSuite, TestSuite, ChecklistItem, at_least, all_of


def create_suites(content: str) -> list[TestSuite]:
    html = HtmlSuite(content)

    ul = html.element('ul')
    lis = ul.get_children('li')
    links = ul.get_children('a', direct=False)

    html.make_item("Het is een ongeordende lijst.",
                   ul.exists())

    html.make_item("De lijst bevat drie lijst items.",
                   lis.exactly(3))

    html.make_item("De lijst bevat drie links.",
                   links.exactly(3))

    names = [
        "Faculteit Wetenschappen (FWE)",
        "Faculteit Ingenieurswetenschappen en Architectuur (FEA)",
        "Faculteit Bio-ingenieurswetenschappen (FBW)"
    ]

    websites = ["https://www.ugent.be/we/nl",
                "https://www.ugent.be/ea/nl",
                "https://www.ugent.be/bw/nl"]

    html.make_item("De drie lijst items bevatten de juiste inhoud.",
                   lis.exactly(3),
                   links.exactly(3),
                   [li.get_child('a').has_content(name) for li, name in zip(lis, names)])

    html.make_item("De drie lijst items bevatten elk een link.",
                   lis.exactly(3),
                   links.exactly(3),
                   [li.get_child('a').attribute_exists('href') for li in lis])

    html.make_item("De drie lijst items bevatten elk de juiste link.",
                   lis.exactly(3),
                   links.exactly(3),
                   [li.get_child('a').attribute_exists('href', web) for li, web in zip(lis, websites)])

    html.translations["en"] = [
        "The list is unordered."
        "The list contains three list items.",
        "The list contains three links.",
        "The three list items contain the right content.",
        "Each list item of the three list items contain a link.",
        "Each list item of the three list items contain the right link."
    ]

    return [html]
