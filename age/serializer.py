from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    iin = serializers.CharField(max_length=12, min_length=12)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ["iin", "age"]
    
    def create(self, validated_data):
        iin = validated_data['iin']
        if len(iin) == 12:
            # проверка месяца на нахождение в диапозоне от 1 до 12 включительно
            if int(iin[2:4]) in range(1, 13):
                return Person.objects.create(**validated_data)
            else:
                raise serializers.ValidationError("Invalid IIN!")

    def get_age(self, person):
        return person.age
