from django.contrib import admin
from .models import Fund
from .models import Category
from .models import Income
from .models import Expense
from .models import User


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'value', 'sender')
    list_filter = ('category', 'date')
    search_fields = ('sender', 'date', 'category')


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    sum = 'sum_of_founds'


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'value')
    list_filter = ('category', 'date')
    search_fields = ('date', 'category')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')


admin.site.register(Category)
