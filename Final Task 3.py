
import matplotlib.pyplot as plt
keys = ["product_name", "quantity", "price", "date"]

"""
1. read_sales_data(file_path), которая принимает путь к файлу и возвращает список продаж. Продажи в свою очередь
являются словарями с ключами product_name, quantity, price, date (название, количество, цена, дата).
"""


def read_sales_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        input_list = file.read().splitlines()
        output_list = [dict(zip(keys, list(line.split(", ")))) for line in input_list]
    return output_list


"""
2. total_sales_per_product(sales_data), которая принимает список продаж и возвращает словарь,
 где ключ - название продукта, а значение - общая сумма продаж этого продукта.
 """


def total_sales_per_product(sales_data):
    result_dict = {}
    dict_list = list(
        {sale.get("product_name"): int(sale.get("price")) * int(sale.get("quantity"))} for sale in sales_data)
    for d in dict_list:
        for key, value in d.items():
            if key in result_dict:
                result_dict[key] += value
            else:
                result_dict[key] = value
    return result_dict


"""
3. sales_over_time(sales_data), которая принимает список продаж и возвращает словарь,
 где ключ - дата, а значение общая сумма продаж за эту дату.
 """


def sales_over_time(sales_data):
    result_dict = {}
    dict_list = list(
        {
            sale.get("date"): int(sale.get("price")) * int(sale.get("quantity"))
        }
        for sale in sales_data
    )
    for d in dict_list:
        for key, value in d.items():
            if key in result_dict:
                result_dict[key] += value
            else:
                result_dict[key] = value
    return result_dict


current_file_path = input()
sales_data_list = read_sales_data(current_file_path)
total_sales_per_product_dict = total_sales_per_product(sales_data_list)
sales_over_time_dict = sales_over_time(sales_data_list)

# print(sales_data_list)
print(total_sales_per_product_dict)
print(sales_over_time_dict)

"""
1. Определить, какой продукт принес наибольшую выручку.
"""

max_prod_rev = max(total_sales_per_product_dict, key=total_sales_per_product_dict.get)
print(f"Продукт, который принес наибольшую выручку - {max_prod_rev}.")

"""
2.Определить, в какой день была наибольшая сумма продаж.
 """

max_date_rev = max(sales_over_time_dict,key=sales_over_time_dict.get)
print(f"День, в который была наибольшая сумма продаж - {max_date_rev}.")

"""
1. Построить график общей суммы продаж по каждому продукту.
"""
ttl_sum_vals_list = list(total_sales_per_product_dict.values())
ttl_sum_label_list = list(total_sales_per_product_dict.keys())

plt.figure(figsize=(10,5))
p1 = plt.barh(ttl_sum_label_list[0], ttl_sum_vals_list[0], label=ttl_sum_label_list[0], color='#9155d4' )
p2 = plt.barh(ttl_sum_label_list[1], ttl_sum_vals_list[1], label=ttl_sum_label_list[1], color='#ab5bba' )
p3 = plt.barh(ttl_sum_label_list[2], ttl_sum_vals_list[2], label=ttl_sum_label_list[2], color='#c462a1' )
p4 = plt.barh(ttl_sum_label_list[3], ttl_sum_vals_list[3], label=ttl_sum_label_list[3], color='#de6887' )
p5 = plt.barh(ttl_sum_label_list[4], ttl_sum_vals_list[4], label=ttl_sum_label_list[4], color='#f76f6e' )

plt.xlabel("Сумма продаж")
plt.title('Общая сумма продаж по каждому продукту')
plt.grid(axis='x')
plt.show()

"""
2. Построить график общей суммы продаж по дням.
"""

ttl_date_vals_list = list(sales_over_time_dict.values())
ttl_date_label_list = list(sales_over_time_dict.keys())

plt.figure(figsize=(10,5))
plt.bar(ttl_date_label_list, ttl_date_vals_list, label="Сумма продаж", color='#f76f6e' )
plt.xlabel("Дата")
plt.ylabel("Сумма продаж")
plt.title('Общая сумма продаж по дням')
plt.legend()
plt.grid( axis='y')
plt.rc('grid', linestyle=':', color='grey', linewidth= 1 )
plt.show()