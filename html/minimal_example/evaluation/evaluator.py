from validators.checks import HtmlSuite, TestSuite


def create_suites(content: str) -> list[TestSuite]:
    html = HtmlSuite(content)

    body = html.element("body")
    table = body.get_child('table', direct=True)

    html.make_item("The body has a table. (regular)", table.exists())
    html.make_item("The table has two rows. (regular)", table.get_children('tr').at_least(2))

    html.make_item_from_emmet("The body has a table. (Emmet)", "body>table")
    html.make_item_from_emmet("The table has two rows. (Emmet)", "body>table>tr*2")

    html.translations["nl"] = [
        "De body heeft een tabel. (normaal)",
        "De tabel heeft twee rijen. (normaal)",
        "De body heeft een tabel. (Emmet)",
        "De tabel heeft twee rijen. (Emmet)"
    ]

    return [html]
