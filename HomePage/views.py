from django.shortcuts import render, redirect, get_object_or_404
from .models import Card_model,Product_Size_model, Product_Color_model,Comment,SelectFavorite_cloth
from django.db.models import Max
from django.contrib import messages
from django.db.models import Avg
from django.db.models import Sum

def HomePageView(request , size_slug = None, color_slug =None, price = None, rating = None):
    
    
    product_size = Product_Size_model.objects.all()
    product_color = Product_Color_model.objects.all()
    
    card_data = Card_model.objects.all()
    
    
    maximum_price = Card_model.objects.aggregate(Max('Product_price'))['Product_price__max']
    maximum_price = int(maximum_price) if maximum_price else 0




    if  size_slug is not None:
        size = Product_Size_model.objects.get(slug = size_slug)
        card_data = Card_model.objects.filter(Product_size=size)
        
        
    if  color_slug is not None:
        color = Product_Color_model.objects.get(slug = color_slug)
        card_data = Card_model.objects.filter(Product_color=color)
    
        
        
    selected_price = request.GET.get('price')
    
    if selected_price:
        card_data = card_data.filter(Product_price__lte=selected_price)
        
        
        
        
        
    # check faberite data
    
    if request.user.is_authenticated:
        favorites = SelectFavorite_cloth.objects.filter(user=request.user)
        for product in card_data:
            product.is_favorite = favorites.filter(Product=product).exists()

    
    
    return render(request, 'homepage.html',{
        "product_size": product_size,
        "product_color": product_color,
        "card_data": card_data,
        'maximum_price':maximum_price,
        
    })
    
    
    
    
    
    
    
    
  
    
    
    
# def Filter_home_page_star(request, id):
    
    
#     category = get_object_or_404(Card_model, pk=id)
#     data_filter = Card_model.objects.filter(id=category.id)
    
#     # Get all comments for the current product
#     card_comment_filter = Comment.objects.filter(Product=category)
    
#     rating_sum = card_comment_filter.aggregate(Sum('rating'))['rating__sum'] or 0
#     print(rating_sum)    
#     # Calculate average rating
#     rating_avg = card_comment_filter.aggregate(Avg('rating'))['rating__avg'] or 0
#     rating_avg = round(rating_avg, 1)  # No need to divide by 5; ratings are already between 1 and 5
    
#     # Calculate if there is a half star (check if rating_avg has a decimal part)
#     rating_avg_half = rating_avg % 1 != 0

#     # Check if the user has rated this product
#     user_rating = None
#     if request.user.is_authenticated:
#         user_rating = Comment.objects.filter(Product=category, user=request.user).aggregate(Max('rating'))['rating__max']
    
#     return render(request, 'homepage.html', {
#         'category': category, 
#         'data_filter': data_filter, 
#         'card_comment_filter': card_comment_filter, 
#         'rating_avg': rating_avg,
#         'rating_avg_half': rating_avg_half,
#         'user_rating': user_rating
#     })




    

def Product_DetailViews(request, id):
    
    category = get_object_or_404(Card_model, pk=id)
    data_filter = Card_model.objects.filter(id = category.id)
    
    card_comment_filter = Comment.objects.filter(Product=category)
    
    rating_sum = card_comment_filter.aggregate(Sum('rating'))['rating__sum'] or 0
    
    rating_avrage = rating_sum /5
    
    
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Comment.objects.filter(Product=category, user=request.user).aggregate(Max('rating'))['rating__max']

    
    
    
    
  
    return render(request, 'Product_detials.html', {
        
        'category': category, 
        'data_filter': data_filter, 
        'card_comment_filter': card_comment_filter, 
        'rating_sum': rating_sum,
        'rating_avrage': rating_avrage,
        'user_rating': user_rating
        

        
        
        })


def CommentForms_views(request,id):
    
    if request.method == 'POST':
        Product = get_object_or_404(Card_model, pk=id)
        Text = request.POST.get('Text')
        rating = request.POST.get('rating')
        
        
        try:
            Comment.objects.create(
                Product=Product,
                user=request.user,
                Text=Text,
                rating=rating
            )
            messages.success(request, 'Message Addedd Successfully')
            return redirect('product_detail',id=Product.id)
        
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('product_detail', id=Product.id)
        
    else:
        messages.error(request, 'Invalid Request Method')
        return redirect('product_detail')







def faveriteForm(request, id):
    if request.method == 'POST' and request.user.is_authenticated:
        product = get_object_or_404(Card_model, pk=id)
    
        favorite, created = SelectFavorite_cloth.objects.get_or_create(user=request.user, Product=product)
        
       
        favorite.favorite = not favorite.favorite
        favorite.save()
        
        if favorite.favorite:
            messages.success(request, 'Added to favorites!')
        else:
            messages.success(request, 'Removed from favorites!')
            
        return redirect('homepage')

    else:
        messages.error(request, 'Please log in to mark favorites.')
        return redirect('homepage')





def Faverite_items(request,id=None):
    
    if id:
        category = get_object_or_404(SelectFavorite_cloth, pk=id)
   
        favarite_card_filter = SelectFavorite_cloth.objects.filter(favorite=category)
    
    else:
        favarite_card_filter = SelectFavorite_cloth.objects.filter(user=request.user, favorite=True)
  
    return render(request, 'faterite_items.html',{
        
        'favarite_card_filter': favarite_card_filter,
    })








