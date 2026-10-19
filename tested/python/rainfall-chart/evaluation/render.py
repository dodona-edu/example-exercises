import base64
import os

# noinspection PyUnresolvedReferences
from evaluation_utils import EvaluationResult, Message


def render(context):
    """Render the chart the student drew as an inline image in the feedback.

    Just before this oracle runs, the test harness saved the current matplotlib
    figure to ``chart.png`` in the execution directory. We read those bytes
    back, base64-encode them and hand them to Dodona as an HTML message. Dodona
    keeps ``<img src="data:image/png;base64,...">`` through its sanitiser, so the
    chart renders straight into the feedback table.
    """
    chart_path = os.path.join(context.execution_directory, "chart.png")

    if not os.path.isfile(chart_path) or os.path.getsize(chart_path) == 0:
        return EvaluationResult(
            result=False,
            readable_expected="a rendered chart",
            readable_actual="no chart was produced",
            messages=[Message(
                "Your code did not leave a matplotlib figure for the judge to "
                "render. Make sure rainfall_chart draws a bar chart.",
                "text",
            )],
        )

    with open(chart_path, "rb") as chart_file:
        encoded = base64.b64encode(chart_file.read()).decode("ascii")

    image = (
        f'<img src="data:image/png;base64,{encoded}" '
        f'alt="Your rainfall chart" style="max-width: 100%; height: auto;">'
    )

    return EvaluationResult(
        result=True,
        readable_expected="a rendered chart",
        readable_actual="a rendered chart",
        messages=[Message(image, "html")],
    )
