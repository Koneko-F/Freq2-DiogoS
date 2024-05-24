def apply_discount(cart, discount):
    shopList = cart
    itens = []
    discount /= 100
    
    for key in cart:
        itens.append(key)
    
    for item in itens:
        shopList[item] *= discount
            
    return shopList