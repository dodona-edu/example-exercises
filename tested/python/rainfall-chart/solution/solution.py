import pandas as pd
import matplotlib.pyplot as plt

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def rainfall_chart(records):
    """Return the total rainfall per month and draw a bar chart of it.

    records is a list of [month, rainfall] pairs, where month is an integer
    from 1 (January) to 12 (December) and rainfall is an amount in mm. The
    returned list always has twelve integers, one per month from January to
    December; months without any measurement get a total of 0.
    """
    frame = pd.DataFrame(records, columns=["month", "rainfall"])
    per_month = frame.groupby("month")["rainfall"].sum()
    totals = [int(per_month.get(month, 0)) for month in range(1, 13)]

    plt.figure(figsize=(8, 4))
    plt.bar(MONTHS, totals, color="#1a82c4")
    plt.title("Total rainfall per month")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.tight_layout()
    plt.show()

    return totals


if __name__ == "sandbox":
    sample = [[1, 49], [2, 41], [3, 38], [4, 52], [5, 57], [6, 72],
              [7, 73], [8, 79], [9, 66], [10, 60], [11, 67], [12, 62]]
    print(rainfall_chart(sample))
