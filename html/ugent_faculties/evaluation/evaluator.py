from validators.checks import HtmlSuite, CssSuite, TestSuite, ChecklistItem, at_least, all_of


def create_suites(content: str) -> list[TestSuite]:
    html = HtmlSuite(content)

    title = html.element('title')

    html.make_item("The title has the right content.",
                   title.exists(),
                   title.has_content("Bèta-faculties UGent"))

    body = html.element("body")
    table = body.get_child("table")

    # body>table
    html.make_item("The <body> tag has a table.", table.exists())

    # All table rows
    table_rows = table.get_children("tr", direct=False)

    # Table has at least one row
    html.make_item("The table has 4 rows.", table_rows.exactly(4))

    # First row has a header, the header is correct
    header = ["Name (English)", "Name (Dutch)", "Abbreviation"]
    html.make_item("The first row has a header with the required text.",
                   table_rows[0].get_children("th").exactly(3),  # Check that the FIRST row is a header
                   table.has_table_header(header)  # Check that the header matches up
                   )

    # The second row is correct
    second_row = ["Faculty of Sciences",
                  "Faculteit Wetenschappen",
                  "FWE"]
    html.make_item("The second row contains the required data.",
                   table_rows[1].table_row_has_content(second_row))

    # The third row is correct
    third_row = ["Faculty of Engineering and Architecture",
                 "Faculteit Ingenieurswetenschappen en Architectuur",
                 "FEA"]
    html.make_item("The third row contains the required data.",
                   table_rows[2].table_row_has_content(third_row))

    # The fourth row is correct
    fourth_row = ["Faculty of Bioscience Engineering",
                  "Faculteit Bio-ingenieurswetenschappen",
                  "FBW"]
    html.make_item("The fourth row contains the required data.",
                   table_rows[3].table_row_has_content(fourth_row))

    html.translations["nl"] = [
        "De titel heeft de juiste inhoud.",
        "De <body> tag heeft een tabel.",
        "De tabel heeft 4 rijen.",
        "De eerste rij heeft een hoofding met de juiste tekst.",
        "De tweede rij bevat de juiste tekst.",
        "De derde rij bevat de juiste tekst.",
        "De vierde rij bevat de juiste tekst."
    ]

    return [html]
