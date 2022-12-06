from .models import Trait
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, Request, status
from .serializers import TraitsSerializer


class TraitAssets(APIView):
    def get(self, request):
        # pets = Pet.objects.all()
        # data_pets = []
        # for pet in pets:
        #     data_pets.append(model_to_dict(pet))

        traits = Trait.objects.all()

        serializer = TraitsSerializer(data=traits, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = TraitsSerializer(data=request.data)

        if not serializer.is_valid():
            Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        registerPet = Trait.objects.create(**serializer.validated_data)

        serializer_data = TraitsSerializer(registerPet)

        return Response(serializer_data.data, status.HTTP_201_CREATED)


class TraitDetails(APIView):
    def get(self, request, trait_id):
        trait = get_object_or_404(trait, id=trait_id)
        serializer = TraitsSerializer(data=trait, partial=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, trait_id):
        trait = get_object_or_404(trait, id=trait_id)
        serializer = TraitsSerializer(data=trait, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        for key, value in serializer.validate_data.items():
            setattr(trait, key, value)

        trait.save()

        serializer = TraitsSerializer(trait)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, trait_id):
        trait = get_object_or_404(trait, id=trait_id)
        trait.delete()
        return Response(status.HTTP_204_NO_CONTENT)
