def check_availability(cart, inventory):
    itensCart = []
    itensInv = []
    
    for key in cart:
        itensCart.append(key)
    
    for key in inventory:
        itensInv.append(key)
    
    for key in itensCart:
        if key not in itensInv:
            return False
    
    return True