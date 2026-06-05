In this exercise you summarise a year of rainfall measurements with
[pandas](https://pandas.pydata.org/) and draw the result as a bar chart with
[matplotlib](https://matplotlib.org/).

Each measurement is a `[month, rainfall]` pair, where `month` is an integer from
`1` (January) to `12` (December) and `rainfall` is an amount in millimetres.
There can be any number of measurements per month, in any order.

### Assignment

Write a function `rainfall_chart(records)` that:

1. computes the **total** rainfall per month and returns it as a list of twelve
   integers, ordered from January to December. Months without any measurement
   get a total of `0`.
2. draws a **bar chart** of those monthly totals (the month on the horizontal
   axis, the total rainfall on the vertical axis) and shows it with
   `plt.show()`.

### Example

```python
>>> rainfall_chart([[1, 12], [1, 8], [2, 5], [2, 5], [3, 20]])
[20, 10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

(and a bar chart is drawn)

> When you submit, the judge captures the chart your code draws and shows it
> back to you in the feedback below the test results, so you can see exactly
> what your code produced.
