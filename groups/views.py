from .models import Group
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, Request, status
from .serializers import GroupSerializer


class GroupAssets(APIView):
    def get(self, request):
        # pets = Pet.objects.all()
        # data_pets = []
        # for pet in pets:
        #     data_pets.append(model_to_dict(pet))

        groups = Group.objects.all()

        serializer = GroupSerializer(data=groups, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = GroupSerializer(data=request.data)

        if not serializer.is_valid():
            Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        registerPet = Group.objects.create(**serializer.validated_data)

        serializer_data = GroupSerializer(registerPet)

        return Response(serializer_data.data, status.HTTP_201_CREATED)


class GroupDetails(APIView):
    def get(self, request, group_id):
        group = get_object_or_404(group, id=group_id)
        serializer = GroupSerializer(data=group, partial=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, group_id):
        group = get_object_or_404(group, id=group_id)
        serializer = GroupSerializer(data=group, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        for key, value in serializer.validate_data.items():
            setattr(group, key, value)

        group.save()

        serializer = GroupSerializer(group)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, group_id):
        group = get_object_or_404(group, id=group_id)
        group.delete()
        return Response(status.HTTP_204_NO_CONTENT)
