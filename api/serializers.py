# serializers.py
from rest_framework import serializers
from .models import Patient, Maladie, Prescriptions, Traitement, EtatMaladie


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class MaladieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maladie
        fields = "__all__"


class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = "__all__"


class TraitementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traitement
        fields = "__all__"


class EtatMaladieSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtatMaladie
        fields = "__all__"


class PatientWithPrescriptionsSerializer(serializers.ModelSerializer):
    prescriptions = PrescriptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"


class PatientWithTraitementSerializer(serializers.ModelSerializer):
    traitements = TraitementSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"


class PatientWithEtatMaladieSerializer(serializers.ModelSerializer):
    etat_maladies = EtatMaladieSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"
