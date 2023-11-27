from rest_framework import serializers
from .models import Users, Pets, Vaccine, Records

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class PetSerializerGET(serializers.ModelSerializer):
    user_id = UserSerializer()
    class Meta:
        model = Pets
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'

class RecordSerializerGET(serializers.ModelSerializer):
    pet_id = PetSerializerGET()
    class Meta:
        model = Records
        fields = '__all__'

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'

class VaccineSerializerGET(serializers.ModelSerializer):
    pet_id = PetSerializerGET()
    record_id = RecordSerializer()
    class Meta:
        model = Vaccine
        fields = '__all__'