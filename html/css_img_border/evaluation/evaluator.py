from validators.checks import HtmlSuite, CssSuite, TestSuite, ChecklistItem


def create_suites(content: str) -> list[TestSuite]:
    css = CssSuite(content, check_recommended=False)

    img_element = css.element("img")
    css.make_item("The image has an orange dashed border with the right width.",
                  img_element.exists(),
                  img_element.has_styling("border-style", "dashed"),
                  img_element.has_styling("border-width", "10px"),
                  img_element.has_color("border-color", "orange")
                  )

    css.make_item("The image has the right width.",
                  img_element.exists(),
                  img_element.has_styling("width", "100px"))

    css.translations["nl"] = [
        "De afbeelding heeft een oranje gestreepte rand met de juiste breedte."
        "De afbeelding heeft de juiste breedte.",
    ]

    return [css]
