from plyer import notification

_items = []

def add_item(item):
    for i in _items:
        if i[0] == item[0]:
            total = i[3] + item[3]
            _items[_items.index(i)] = (item[0], item[1], item[2], item[3], item[4], i[5] + 1, total)
            notification.notify(
                title='Item added to cart',
                message=f'{item[1]} was added to your cart',
                app_icon="img/LogoNegro.ico",
                timeout=10
            )
            return

    _items.append((item[0], item[1], item[2], item[3], item[4], 1, item[3]))
    notification.notify(
        title='Item added to cart',
        message=f'{item[1]} was added to your cart',
        app_icon="img/LogoNegro.ico",
        timeout=10
    )

def get_items():
    return _items

def get_total_price():
    total = 0.0
    for i in _items:
        total += i[6]
    return total

def remove_item(item):
    for i in _items:
        if i[0] == item[0]:
            _items.remove(i)
            return

def clear_items():
    _items.clear()
    notification.notify(
        title='Cart cleared',
        message=f'Your cart was cleared',
        app_icon="img/LogoNegro.ico",
        timeout=10
    )