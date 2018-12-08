import datetime
from stock import (get_stock_basics,
                    get_report_data, get_profit_data,
                    get_operation_data, get_growth_data,
                    get_debtpaying_data, get_cashflow_data)
from stock.downloader import load_historys
import numpy as np
from .models import *


def stock_basics():
    stock_basics = get_stock_basics()

    stock_basics_list = [StockBasics(
            code = code,
            name = data['name'],
            industry = data['industry'],
            area = data['area'],
            pe = data['pe'],
            outstanding = data['outstanding'],
            totals = data['totals'],
            totalAssets = data['totalAssets'],
            liquidAssets = data['liquidAssets'],
            fixedAssets = data['fixedAssets'],
            reserved = data['reserved'],
            reservedPerShare = data['reservedPerShare'],
            eps = data['eps'],
            bvps = data['bvps'],
            pb = data['pb'],
            timeToMarket = str(data['timeToMarket']),
        ) for code, data in stock_basics.iterrows()]
    # 先清空
    StockBasics.objects.all().delete()
    # 再保存
    StockBasics.objects.bulk_create(stock_basics_list)
    
    
def history():
    start_date = (datetime.date.today()-datetime.timedelta(days=30*6)).strftime("%Y-%m-%d")
    historys = load_historys(start_date)

    history_list = []
    for history in historys:
        for day, data in history.iterrows():
            history_list.append(History(
                code = data['code'],
                day = str(day),
                open = data['open'],
                close = data['close'],
                high = data['high'],
                low = data['low'],
                vol = data['volume'],
            ))
    # 先清空
    History.objects.all().delete()
    # 再保存
    History.objects.bulk_create(history_list)


def report_data(year, quarter):
    report_data = get_report_data(year, quarter)

    report_data_list = [ReportData(
            code = data['code'],
            name = data['name'],
            eps = data['eps'],
            eps_yoy = data['eps_yoy'],
            bvps = data['bvps'],
            roe = data['roe'],
            epcf = data['epcf'],
            net_profits = data['net_profits'],
            profits_yoy = data['profits_yoy'],
            distrib = data['distrib'],
            report_date = data['report_date'],
        ) for index, data in report_data.iterrows()]
    # 先清空
    ReportData.objects.all().delete()
    # 再保存
    ReportData.objects.bulk_create(report_data_list)


def profit_data(year, quarter):
    profit_data = get_profit_data(year, quarter)

    profit_data_list = [ProfitData(
            code = data['code'],
            name = data['name'],
            roe = data['roe'],
            net_profit_ratio = data['net_profit_ratio'],
            gross_profit_rate = data['gross_profit_rate'],
            net_profits = data['net_profits'],
            eps = data['eps'],
            business_income = data['business_income'],
            bips = data['bips'],
        ) for index, data in profit_data.iterrows()]
    # 先清空
    ProfitData.objects.all().delete()
    # 再保存
    ProfitData.objects.bulk_create(profit_data_list)


def operation_data(year, quarter):
    operation_data = get_operation_data(year, quarter)

    operation_data_list = [OperationData(
            code = data['code'],
            name = data['name'],
            arturnover = data['arturnover'],
            arturndays = data['arturndays'],
            inventory_turnover = data['inventory_turnover'],
            inventory_days = data['inventory_days'],
            currentasset_turnover = data['currentasset_turnover'],
            currentasset_days = data['currentasset_days'],
        ) for index, data in operation_data.iterrows()]
    # 先清空
    OperationData.objects.all().delete()
    # 再保存
    OperationData.objects.bulk_create(operation_data_list)


def growth_data(year, quarter):
    growth_data = get_growth_data(year, quarter)

    growth_data_list = [GrowthData(
            code = data['code'],
            name = data['name'],
            mbrg = data['mbrg'],
            nprg = data['nprg'],
            nav = data['nav'],
            targ = data['targ'],
            epsg = data['epsg'],
            seg = data['seg'],
        ) for index, data in growth_data.iterrows()]
    # 先清空
    GrowthData.objects.all().delete()
    # 再保存
    GrowthData.objects.bulk_create(growth_data_list)


def debtpaying_data(year, quarter):
    debtpaying_data = get_debtpaying_data(year, quarter)

    debtpaying_data_list = [DebtpayingData(
            code = data['code'],
            name = data['name'],
            currentratio = data['currentratio'],
            quickratio = data['quickratio'],
            cashratio = data['cashratio'],
            icratio = data['icratio'],
            sheqratio = data['sheqratio'],
            adratio = data['adratio'],
        ) for index, data in debtpaying_data.iterrows()]
    # 先清空
    DebtpayingData.objects.all().delete()
    # 再保存
    DebtpayingData.objects.bulk_create(debtpaying_data_list)


def cashflow_data(year, quarter):
    cashflow_data = get_cashflow_data(year, quarter)

    cashflow_data_list = [CashflowData(
            code = data['code'],
            name = data['name'],
            cf_sales = data['cf_sales'],
            rateofreturn = data['rateofreturn'],
            cf_nm = data['cf_nm'],
            cf_liabilities = data['cf_liabilities'],
            cashflowratio = data['cashflowratio'],
        ) for index, data in cashflow_data.iterrows()]
    # 先清空
    CashflowData.objects.all().delete()
    # 再保存
    CashflowData.objects.bulk_create(cashflow_data_list)
