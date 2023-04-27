from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


def price_bar_plot(result):
    matplotlib.use('agg')
    x = [result[0]]
    y = []
    for elem in result[1:-1]:
        y_elem, x_elem = elem.split('\n')
        x.append(x_elem)
        y.append(int(y_elem))
    y.append(int(result[-1]))
    raw_data = {'x': x, 'y': y}
    sns.set(style="darkgrid")
    plt.figure(figsize=(10, 7))
    plot = sns.barplot(
        x='x',
        y='y',
        data = raw_data,
        estimator=sum,
        errorbar=None,
        color='#69b3a2',
        )
    plt.xticks(rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Average_price')
    imgdata = StringIO()
    plot.figure.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data