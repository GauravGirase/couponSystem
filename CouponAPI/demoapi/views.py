from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Code
from .serializers import CodeSerializer
from CouponAPI.constants import RESPONSE_MESSAGES, RESPONSE_MESSAGES_TYPE


@api_view(['GET', 'POST'])
def coupans_list(request):
    """
    List all coupans, or create a new coupans.
    """
    if request.method == 'GET':
        codes = Code.objects.all()
        serializer = CodeSerializer(codes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def code_detail(request, pk):
    """
    Retrieve or delete a coupans.
    """
    try:
        code = Code.objects.get(pk=pk)
    except Code.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CodeSerializer(code)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def code_redeem(request, code):
    """
    Retrieve and user can redeem their one time coupan.
    """
    try:
        code = Code.objects.get(code=code)
        if code.active:
            code.active = False
            code.save()
        return Response({RESPONSE_MESSAGES_TYPE[1][0]: RESPONSE_MESSAGES[2][2]}, status=status.HTTP_400_BAD_REQUEST)
    except Code.DoesNotExist:
        return Response({RESPONSE_MESSAGES_TYPE[1][0]: RESPONSE_MESSAGES[1][0]}, status=status.HTTP_404_NOT_FOUND)

    return Response({RESPONSE_MESSAGES_TYPE[0][1]: RESPONSE_MESSAGES[0][1]})
