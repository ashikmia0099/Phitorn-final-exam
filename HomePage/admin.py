from django.contrib import admin
from .models import Product_Size_model,Product_Color_model,Card_model,Comment,SelectFavorite_cloth


class Product_SizeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('size',)}
    list_display = ['size', 'slug']
    
    
    

class Product_colorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('color',)}
    list_display = ['color', 'slug']


admin.site.register(Product_Size_model, Product_SizeAdmin)
admin.site.register(Product_Color_model, Product_colorAdmin)
admin.site.register(Card_model)
admin.site.register(Comment)
admin.site.register(SelectFavorite_cloth)

