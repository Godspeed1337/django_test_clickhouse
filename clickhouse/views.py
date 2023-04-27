from django.shortcuts import render, HttpResponse
from clickhouse.services.connect import CLIENT
import uuid
from clickhouse.services.graph import price_bar_plot


def add(request):
    if request.method == 'POST':
        data_tupple = (uuid.uuid1().int >> 64,
                       request.POST.get('value'),
                       request.POST.get('metric'))
        CLIENT.command(f"INSERT INTO test_table (*) VALUES {data_tupple}")
    return render(request, "clickhouse/add.html")


def average(request):
    result = CLIENT.command('SELECT avg(metric) FROM test_table')
    return HttpResponse(result)


def graph(request):
    result = CLIENT.command('SELECT toYear(date) AS year, round(avg(price)) AS price FROM uk_price_paid GROUP BY year ORDER BY year;')
    img = price_bar_plot(result)
    return render(request, "clickhouse/stat.html", {'price_bar_plot': img})