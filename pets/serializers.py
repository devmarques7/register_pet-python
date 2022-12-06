from rest_framework import serializers
from .models import PetSex, Pet
from groups.models import Group
from traits.models import Trait
from groups.serializers import GroupSerializer
from traits.serializers import TraitsSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=PetSex.choices, default=PetSex.DEFAULT)
    group = GroupSerializer()
    traits = TraitsSerializer(many=True)

    def create(self, validated_data: dict) -> Pet:
        group_dict = validated_data.pop("group")
        traits_dict = validated_data.pop("traits")

        group_instance, _ = Group.objects.get_or_create(**group_dict)
        pet_instance_ = Pet.objects.create(**validated_data, group=group_instance)

        for trait in traits_dict:
            traits_instance, _ = Trait.objects.get_or_create(**trait)
            pet_instance_.traits.add(traits_instance)
        return pet_instance_

    def update(self, instance: Pet, validated_data: dict) -> Pet:
        group_dict = validated_data.pop("group", None)
        traits_dict = validated_data.pop("traits", None)

        list_of_traits = []

        if traits_dict:
            for trait in traits_dict:
                traits_instance, _ = Trait.objects.get_or_create(**trait)
                list_of_traits.append(traits_instance)
            instance.traits.set(list_of_traits)

        if group_dict:
            group_instance, _ = Group.objects.get_or_create(**group_dict)
            instance.group = group_instance

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
