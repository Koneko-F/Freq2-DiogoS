def calculate_total_price(cart):
    precoTotal = 0
    itens = []
    
    for key in cart:
        itens.append(key)
        
    for item in itens:
        precoTotal += cart[item]
        
    return precoTotal

