from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=35,blank = False)
    surname = models.CharField(max_length=35,blank = False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.surname} {self.name}"
    
class Products(models.Model):
    name = models.CharField(max_length=50,blank = False)
    price = models.IntegerField(default=0)
    count_in_stock = models.IntegerField(default=0)
    company_name = models.CharField(max_length=100,blank = False, null=True)
    demand_per_year = models.IntegerField(default=0)#продажный спрос за год
    price_of_1_item = models.IntegerField(default=0)#стоимость покупки 1 товара
    cost_of_storing_1_product_during_the_year = models.DecimalField(default=0, max_digits=8, decimal_places=1)#стоимость хранения 1 товара в течении года
    restocking_time = models.IntegerField(default=0)#время пополнения запасов
    demand_this_month = models.IntegerField(default=0)#спрос за этот месяц
    demand_last_month = models.IntegerField(default=0)#спрос за прошлый месяц


    def __str__(self):
        return f"{self.name}"
    
#class Company(models.Model):
 #   name = models.CharField(max_length=35,blank = False)

  #  def __str__(self):
   #     return f"{self.name}"
    
class Clients(models.Model):
    name = models.CharField(max_length=35,blank = False)
    surname = models.CharField(max_length=35,blank = False)
    age = models.IntegerField(default=0)
    #products = models.ManyToManyField(Products)
    #company = models.ManyToManyField(Company)
    #worker = models.ForeignKey(Worker, on_delete = models.CASCADE,related_name='related_name', default=1)

    def __str__(self):
       return f"{self.surname} {self.name}"
    
class Order(models.Model):
    client = models.ForeignKey(Clients,on_delete = models.CASCADE, default=1)
    product = models.ForeignKey(Products,on_delete = models.CASCADE, default=1)
    count_of_products = models.IntegerField(default=0)
    worker = models.ForeignKey(Worker,on_delete = models.CASCADE, default=1)

    def __str__(self):
        return f"Замовлення для {self.client}"

