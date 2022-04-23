from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from torch import double
import yfinance as yf

@login_required
def all_stocks(request):
    stock_tickers = {
        "Infosys Ltd.":"INFY.NS",
        "Relicance Industries Ltd." :"RELIANCE.NS",
        "HDFC Bank Ltd.": "HDFCBANK.NS",
        "ICICI Bank Ltd": "ICICIBANK.NS",
        "Adani Green Energy Ltd.": "ADANIGREEN.NS",
        "State Bank Of India": "SBIN.NS",
        "Kotak Mahindra Bank Ltd.": "KOTAKBANK.NS",
        "ITC Ltd.": "ITC.NS",
        "Axis Bank Ltd.": "AXISBANK.NS",
        "Larsen & Toubro Ltd.": "LT.NS",
        
        "Amazon.com, Inc.": "AMZN",
        "Microsoft Corporation": "MSFT",
        "Zoom Video Communications, Inc.": "ZM",
        "Tesla, Inc": "TSLA",
        "Netflix, Inc.": "NFLX",
        "Facebook Inc.": "FB",
        "Apple Inc.": "AAPL",
        "Alphabet Inc.": "GOOG",
        "Cisco Systems, Inc.": "CSCO",
        "NVIDIA Corporation": "NVDA",
        "Adobe Inc.": "ADBE",

        "Bitcoin USD": "BTC-USD",
        "Ethereum USD": "ETH-USD",
        "Binance Coin USD": "BNB-USD",
        "XRP USD": "XRP-USD",
        "Dogecoin USD": "DOGE-USD"
    }
    final_data = []
    for stock_name, stock_ticker in stock_tickers.items():
        stock = yf.Ticker(stock_ticker)
        stock_data = stock.info
        stock_difference = stock_data['regularMarketOpen'] - stock_data['regularMarketPreviousClose']
        stock_difference = "{:.2f}".format(stock_difference)
        stock_difference_percent = (float(stock_difference) * 100) / float(stock_data['regularMarketPreviousClose'])
        stock_difference_percent = "{:.2f}".format(stock_difference_percent)
        data = {
            'stock_name': stock_name,
            'ticker_name': stock_ticker,
            'previous_close_price': stock_data['regularMarketPreviousClose'],
            'current_market_price': stock_data['regularMarketOpen'],
            'difference': float(stock_difference),
            'percentage_change': stock_difference_percent,
            'current_day_high': stock_data['regularMarketDayHigh'],
            'current_day_low': stock_data['regularMarketDayLow'],
            'currency': stock_data['currency'],
            'last_one_year_high': stock_data['fiftyTwoWeekHigh'],
            'last_one_year_low': stock_data['fiftyTwoWeekLow'],
            'logo_url': stock_data['logo_url'],
        }
        final_data.append(data)
    return render(request, 'stockprice_live/stock.html', {'data': final_data})

@login_required
def indian_stocks(request):
    stock_tickers = {
        "Infosys Ltd.":"INFY.NS",
        "Relicance Industries Ltd." :"RELIANCE.NS",
        "HDFC Bank Ltd.": "HDFCBANK.NS",
        "ICICI Bank Ltd": "ICICIBANK.NS",
        "Adani Green Energy Ltd.": "ADANIGREEN.NS",
        "State Bank Of India": "SBIN.NS",
        "Kotak Mahindra Bank Ltd.": "KOTAKBANK.NS",
        "ITC Ltd.": "ITC.NS",
        "Axis Bank Ltd.": "AXISBANK.NS",
        "Larsen & Toubro Ltd.": "LT.NS",
    }
    final_data = []
    for stock_name, stock_ticker in stock_tickers.items():
        stock = yf.Ticker(stock_ticker)
        stock_data = stock.info
        stock_difference = stock_data['regularMarketOpen'] - stock_data['regularMarketPreviousClose']
        stock_difference = "{:.2f}".format(stock_difference)
        stock_difference_percent = (float(stock_difference) * 100) / float(stock_data['regularMarketPreviousClose'])
        stock_difference_percent = "{:.2f}".format(stock_difference_percent)
        data = {
            'stock_name': stock_name,
            'ticker_name': stock_ticker,
            'previous_close_price': stock_data['regularMarketPreviousClose'],
            'current_market_price': stock_data['regularMarketOpen'],
            'difference': float(stock_difference),
            'percentage_change': stock_difference_percent,
            'current_day_high': stock_data['regularMarketDayHigh'],
            'current_day_low': stock_data['regularMarketDayLow'],
            'currency': stock_data['currency'],
            'last_one_year_high': stock_data['fiftyTwoWeekHigh'],
            'last_one_year_low': stock_data['fiftyTwoWeekLow'],
            'logo_url': stock_data['logo_url'],
        }
        final_data.append(data)
    return render(request, 'stockprice_live/stock.html', {'data': final_data})

@login_required
def global_stocks(request):
    stock_tickers = {
        "Amazon.com, Inc.": "AMZN",
        "Microsoft Corporation": "MSFT",
        "Zoom Video Communications, Inc.": "ZM",
        "Tesla, Inc": "TSLA",
        "Netflix, Inc.": "NFLX",
        "Facebook Inc.": "FB",
        "Apple Inc.": "AAPL",
        "Alphabet Inc.": "GOOG",
        "Cisco Systems, Inc.": "CSCO",
        "NVIDIA Corporation": "NVDA",
        "Adobe Inc.": "ADBE"
    }
    final_data = []
    for stock_name, stock_ticker in stock_tickers.items():
        stock = yf.Ticker(stock_ticker)
        stock_data = stock.info
        stock_difference = stock_data['regularMarketOpen'] - stock_data['regularMarketPreviousClose']
        stock_difference = "{:.2f}".format(stock_difference)
        stock_difference_percent = (float(stock_difference) * 100) / float(stock_data['regularMarketPreviousClose'])
        stock_difference_percent = "{:.2f}".format(stock_difference_percent)
        data = {
            'stock_name': stock_name,
            'ticker_name': stock_ticker,
            'previous_close_price': stock_data['regularMarketPreviousClose'],
            'current_market_price': stock_data['regularMarketOpen'],
            'difference': float(stock_difference),
            'percentage_change': stock_difference_percent,
            'current_day_high': stock_data['regularMarketDayHigh'],
            'current_day_low': stock_data['regularMarketDayLow'],
            'currency': stock_data['currency'],
            'last_one_year_high': stock_data['fiftyTwoWeekHigh'],
            'last_one_year_low': stock_data['fiftyTwoWeekLow'],
            'logo_url': stock_data['logo_url'],
        }
        final_data.append(data)
    return render(request, 'stockprice_live/stock.html', {'data': final_data})

@login_required
def crypto_currency(request):
    stock_tickers = {
        "Bitcoin USD": "BTC-USD",
        "Ethereum USD": "ETH-USD",
        "Binance Coin USD": "BNB-USD",
        "XRP USD": "XRP-USD",
        "Dogecoin USD": "DOGE-USD"
    }
    final_data = []
    for stock_name, stock_ticker in stock_tickers.items():
        stock = yf.Ticker(stock_ticker)
        stock_data = stock.info
        stock_difference = stock_data['regularMarketOpen'] - stock_data['regularMarketPreviousClose']
        stock_difference = "{:.2f}".format(stock_difference)
        stock_difference_percent = (float(stock_difference) * 100) / float(stock_data['regularMarketPreviousClose'])
        stock_difference_percent = "{:.2f}".format(stock_difference_percent)
        data = {
            'stock_name': stock_name,
            'ticker_name': stock_ticker,
            'previous_close_price': stock_data['regularMarketPreviousClose'],
            'current_market_price': stock_data['regularMarketOpen'],
            'difference': float(stock_difference),
            'percentage_change': stock_difference_percent,
            'current_day_high': stock_data['regularMarketDayHigh'],
            'current_day_low': stock_data['regularMarketDayLow'],
            'currency': stock_data['currency'],
            'last_one_year_high': stock_data['fiftyTwoWeekHigh'],
            'last_one_year_low': stock_data['fiftyTwoWeekLow'],
            'logo_url': stock_data['logo_url'],
        }
        final_data.append(data)
    return render(request, 'stockprice_live/stock.html', {'data': final_data})