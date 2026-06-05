# Pokémon stats

Demonstrates a TESTed Python exercise that combines CSV reading with **pandas**, data aggregation, and chart generation with **matplotlib**. Tests inspect both the analytic return values and properties of the returned `matplotlib.figure.Figure` (title, axis labels, bar count, bar heights, tick labels) using language-specific Python expressions. The "Chart" tab additionally saves the returned figure and renders it inline in the feedback table via a custom check oracle (`evaluation/render.py`), which base64-encodes the PNG into an HTML `<img>` message.

The exercise relies on `pandas` and `matplotlib` being available in the judge's Docker image — confirm both are installed before running.
