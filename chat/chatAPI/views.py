from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import User,Message
from django.db.models import Q
class ChatView(ViewSet):

    def get_members(self, request, user_id):
        send_messages = Message.objects.filter(sender=user_id)
        receive_messages= Message.objects.filter(receiver=user_id)
        receiver= send_messages.values_list('receiver',flat=True)
        sender= receive_messages.values_list('sender',flat=True)
        users_connection=receiver.union(sender)
        #TODO return all members associated with the user
        final=[]
        users_connections=User.objects.filter(id__in=users_connection)
        for user in users_connections :
            unreaded_messages= Message.objects.filter(sender=user).filter(receiver=user_id,is_read=False).count()
            dic={'username':user.username,'id':user.id,'first_name':user.first_name ,'last_name':user.last_name,'unreaded_messages':unreaded_messages}
            final.append(dic)
        return Response(final, status=status.HTTP_200_OK)