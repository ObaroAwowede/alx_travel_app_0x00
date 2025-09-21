from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def listings_list(request):
    """
    Returns a list of all travel listings.
    """
    data = [
        {'id': 1, 'title': 'Beautiful Beach House', 'location': 'Mombasa'},
        {'id': 2, 'title': 'Mountain Cabin', 'location': 'Nairobi'},
    ]
    return Response(data)