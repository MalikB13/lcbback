from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .apps import ChatbotConfig
from .serializers import MessageSerializer
from .models import Message

# Create your views here.

class MessageView(APIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get(self, request):
        if request.method == 'GET':
            # sentence is the query we want to get the prediction for
            params = request.GET.get('sentence')
            print(request.GET)

            # predict method used to get the prediction
            print(params)
            response = ChatbotConfig.answer(self, sentence=str(params))

            # returning JSON response
            print(response)
            return JsonResponse(response)
