from django.shortcuts import render
from app1.models import Worker, Products, Clients, Order
import math


# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def index2_page(request):
    return render(request, 'index2.html')

#def company_page(request):
 #   all_company = Company.objects.all()
  #  return render(request, 'company.html', {'data' : all_company})

def workers_page(request):
    all_workers = Worker.objects.all()
    context = {
        'workers': all_workers,
    }
    return render(request, 'workers.html', context)

def products_page(request):
    all_products = Products.objects.all()
    context = {
        'products': all_products,
    }
    return render(request, 'products.html', context)

def client_page(request):
    all_clients = Clients.objects.all()
    context = {
        'clients': all_clients,
    }
    return render(request, 'clients.html', context)

def order_page(request):
    all_order = Order.objects.all()
    context = {
        'order': all_order,
    }
    return render(request, 'order.html', context)

def tasks(request):
    all_products = Products.objects.all()
    optimal_zapas = []
    optimal_zakaz = []
    prognoz = []
    count = []
    c = 0
    for i in all_products:
        sr1 = i.demand_per_year / 12
        sr2 = i.restocking_time / 30
        res = sr1 * sr2
        optimal_zapas.append(round(res))
        s = i.price_of_1_item
        h = i.cost_of_storing_1_product_during_the_year
        d = i.demand_per_year
        eoq = round(math.sqrt((2*d*s)/h))
        optimal_zakaz.append(eoq)
        now = i.demand_this_month
        last = i.demand_last_month
        a = 0.4
        res1 = a * now + (1-a) * last
        prognoz.append(round(res1))
        count.append(c)
        c += 1

    st = 'Перша задача - задача оптимального рівня запасу. Для цього нам потрібно знати середньомісячний попит на товар та час за який можна поповнити запаси.'
  
    str = []
    stra = []
    strb = []
    for i in range(len(count)):
        str1=f'*Товар:{all_products[i].name}'
        str2=f'***Cередньомісячний попит на {all_products[i].name}: {round(all_products[i].demand_per_year / 12)}'
        str3=f'***Час за який можна поповнити запаси: {round(all_products[i].restocking_time / 30,2)} місяці'
        str4=f'Маючи такі дані, вирішуємо задачу оптимального рівня запасу. Результат: {optimal_zapas[i]}'
        str5=f'Аналізуючи результат, можна сказати, що для управління запасами слід підтримувати запаси товару лише на рівні щонайменше {optimal_zapas[i]} одиниць. Це означає, що при досягненні запасів до цього рівня слід розміщувати нове замовлення для поповнення запасів.'
        str6=f'Враховуючи середньомісячний попит та час постачання товару, оптимальний рівень запасу дозволить забезпечити безперервну наявність товару та мінімізувати ризики нестачі запасів.'
        str7 = '------------------------------------------------------------------------------------------------'
        str.append(str1) 
        str.append(str2)
        str.append(str3)
        str.append(str4)
        str.append(str5)
        str.append(str6)
        if i < len(count) - 1:
            str.append(str7)

    st1 = 'Друга задача - задача оптимального замовлення. Для цього нам потрібно знати ціну за одиницю товару, ціну зберігання 1 товару протягом року та попит за рік.'
    for i in range(len(count)):
        str1=f'*Товар:{all_products[i].name}'
        str2=f'***Ціна за одиницю товару: {all_products[i].price_of_1_item}'
        str3=f'***Ціна зберігання 1 товару протягом року: {all_products[i].cost_of_storing_1_product_during_the_year}'
        str4=f'***Річний попит: {all_products[i].demand_per_year}'
        str5=f'Маючи такі дані, вирішуємо задачу оптимального замовлення. Результат: {optimal_zakaz[i]}'
        str6=f'Аналізуючи результат, можна сказати, що це кількість товару, яку слід замовляти щоразу, щоб мінімізувати загальні витрати на купівлю та зберігання товару.'
        str7 = '------------------------------------------------------------------------------------------------'
        stra.append(str1) 
        stra.append(str2)
        stra.append(str3)
        stra.append(str4)
        stra.append(str5)
        stra.append(str6)
        if i < len(count) - 1:
            stra.append(str7)

    st2 = 'Третя задача - прогнозування попиту на наступний місяць. Вхідні дані - це попит за два останні місяці.'
    for i in range(len(count)):
        str1=f'*Товар:{all_products[i].name}'
        str2=f'***Попит на перший місяць: {all_products[i].demand_this_month}'
        str3=f'***Попит на другий місяць: {all_products[i].demand_last_month}'
        str5=f'Маючи такі дані, вирішуємо задачу прогнозування попиту на наступний місяць. Результат: {prognoz[i]}'
        str6=f'Аналізуючи результат, можна сказати, число {prognoz[i]}, отримане в результаті вирішення завдання прогнозування попиту на наступний місяць, вказує на очікуваний обсяг попиту на цей товар наступного місяця. Це означає, що на основі наявних даних про попит за два останні місяці та інші фактори, обраний алгоритм прогнозування передбачає, що попит становитиме приблизно {prognoz[i]} одиниць товару.'
        str7 = '------------------------------------------------------------------------------------------------'
        strb.append(str1) 
        strb.append(str2)
        strb.append(str3)
        strb.append(str5)
        strb.append(str6)
        if i < len(count) - 1:
            strb.append(str7)
  
    context = {
        'products': all_products,
        'optimal_zapas': optimal_zapas,
        'optimal_zakaz': optimal_zakaz,
        'prognoz':prognoz,
        'count': count,
        'str1': str,
        'st': st,
        'stra': stra,
        'st1': st1,
        'strb': strb,
        'st2': st2,
    }
    return render(request, 'tasks.html', context)