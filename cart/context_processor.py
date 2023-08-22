from .models import *
from .views import *


def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = Cartlist.objects.filter(cart_id=c_id(request))
            cti = item.objects.all().filter(cart=ct[:1])  # Corrected line
            for c in cti:
                item_count += c.quan
        except Cartlist.DoesNotExist:
            item_count = 0
        return {'itc': item_count}  # Return a dictionary with a proper key-value pair
