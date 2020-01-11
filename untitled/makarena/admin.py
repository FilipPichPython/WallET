from django.contrib import admin
from .models import Fund
from .models import Category
from .models import Income
from .models import Expense
from .models import User


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'value', 'sender', 'category_name', 'description')
    list_filter = ('category_name','value', 'date')
    search_fields = ('sender', 'description')


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    sum = 'sum_of_founds'


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'value', 'category_name', 'description')
    list_filter = ('category_name', 'value', 'date')
    search_fields = ('date', 'description')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    category_name = 'category_name'

