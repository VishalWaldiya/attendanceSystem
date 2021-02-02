from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Models
from webui.models import MemberList

# Serializers
from .serializers import MemberListSerializer

class MemberListList(APIView):
    """
    List all MemberLists, or create a new MemberList.
    """
    def get(self, request, format=None):
        memberLists = MemberList.objects.all()
        serializer = MemberListSerializer(memberLists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MemberListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberListDetail(APIView):
    """
    Retrieve, update or delete a MemberList instance.
    """
    def get_object(self, pk):
        try:
            return MemberList.objects.get(pk=pk)
        except MemberList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        memberList = self.get_object(pk)
        serializer = MemberListSerializer(memberList)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        memberList = self.get_object(pk)
        serializer = MemberListSerializer(memberList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        MemberList = self.get_object(pk)
        MemberList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)