# Monthly rainfall chart

Python (pandas + matplotlib) TESTed exercise: the student writes
`rainfall_chart(records)`, which aggregates rainfall measurements per month with
pandas, returns the twelve monthly totals (graded by value comparison in the
"Monthly totals" tab), and draws a matplotlib bar chart.

This is the counterpart to the `data-visualization` example: it shows the *other*
way to surface a chart in the feedback. Here the function does **not** return the
`Figure` — it just draws and calls `plt.show()`. Under the judge's headless Agg
backend `plt.show()` is a no-op that leaves the figure in place, so the test
suite grabs the implicit current figure with `plt.gcf().savefig('chart.png')` and
a custom check oracle (`evaluation/render.py`) base64-encodes it into an HTML
`<img>` message, which renders inline in the Dodona feedback table (the "Your
chart" tab).
