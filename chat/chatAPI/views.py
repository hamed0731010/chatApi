from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


class ChatView(ViewSet):

    def get_members(self, request, user_id):
        
        #TODO return all members associated with the user
        
        return Response({}, status=status.HTTP_200_OK)