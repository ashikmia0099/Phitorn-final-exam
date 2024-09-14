from django.db import models
from django.contrib.auth.models import User



gender_select = [
    ('Male', 'Male'),
    ('Female','Female'),
    ('Kids','Kids'),
]



class Product_Size_model(models.Model):
    
    size = models.CharField( max_length=10, blank=True, null= True)
    slug = models.SlugField(max_length=10, blank=True, null= True)

    class Meta:
        verbose_name_plural = 'Product Size'
        
    
    def __str__(self):
        return self.size
    


class Product_Color_model(models.Model):
    
    color = models.CharField( max_length=10, blank=True, null= True)
    slug = models.SlugField(max_length=10, blank=True, null= True)

    class Meta:
        verbose_name_plural = 'Product Color'
        
    
    
    def __str__(self):
        return self.color
    




class Card_model(models.Model):
    Product_Name = models.CharField(max_length=100, blank=True, null= True)
    Product_size = models.ForeignKey(Product_Size_model,  on_delete=models.CASCADE)
    Product_color = models.ForeignKey(Product_Color_model,  on_delete=models.CASCADE)
    Product_price = models.CharField(max_length=5, blank=True, null= True)
    Select_gender = models.CharField( choices=gender_select, max_length=10, blank=True, null= True)
    images = models.ImageField(upload_to='HomePage/media/', blank=True, null=True)
    
    
    class Meta:
        verbose_name_plural = 'Card Data'
        
        
    

class Comment(models.Model):
    
    Product = models.ForeignKey(Card_model, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.TextField(blank=True, null= True)
    rating = models.IntegerField()
    
    
    
    
    class Meta:
        verbose_name_plural = 'Comment'
        


class SelectFavorite_cloth(models.Model):
    
    Product = models.ForeignKey(Card_model, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)
    
    
    class Meta:
        verbose_name_plural = 'Select Favorite Cloth'
        
        
        


