from django.shortcuts import render
import twstock
from twstock import stock
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from datetime import datetime

# Create your views here.
def index(request):

    stock = twstock.Stock('2330')                             # 擷取台積電股價
    stocknumber = stock.sid
    stockname = twstock.codes['2330'].name
    ma_p = stock.moving_average(stock.price, 5)       # 計算五日均價
    ma_c = stock.moving_average(stock.capacity, 5)    # 計算五日均量
    ma_p_cont = stock.continuous(ma_p)                # 計算五日均價持續天數
    ma_br = stock.ma_bias_ratio(5, 10)                # 計算五日、十日乖離值

    x = stock.date    # [ x.strftime('%Y-%m-%d') for x in stock.date ]
    y = stock.price

    z = stock.open

    # create a new plot with a title and axis labels
    p = figure(title=stockname, x_axis_type='datetime', x_axis_label='Date', y_axis_label='Stock Price')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="close price", line_width=2)
    p.line(x, z, legend="open price", line_width=2, color="red")

    script, div = components(p)

    context = {
        'stock': stock,
        'stocknumber': stocknumber,
        'stockname': stockname,
        'ma_p': ma_p,
        'ma_c': ma_c,
        'ma_c_cont': ma_p_cont,
        'ma_br': ma_br,
        'script': script,
        'div': div,
    }
    return render(request, 'stockdata/index.html', context)
