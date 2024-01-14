# views.py
from rest_framework import generics
from .models import Patient, Maladie, Prescriptions, Traitement, EtatMaladie
from .serializers import (
    PatientSerializer,
    MaladieSerializer,
    PrescriptionsSerializer,
    TraitementSerializer,
    EtatMaladieSerializer,
    PatientWithPrescriptionsSerializer,
    PatientWithTraitementSerializer,
    PatientWithEtatMaladieSerializer,
    
)


class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientWithPrescriptionsView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientWithPrescriptionsSerializer


class PatientWithTraitementView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientWithTraitementSerializer


class PatientWithEtatMaladieView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientWithEtatMaladieSerializer


class MaladieListCreateView(generics.ListCreateAPIView):
    queryset = Maladie.objects.all()
    serializer_class = MaladieSerializer


class MaladieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maladie.objects.all()
    serializer_class = MaladieSerializer


class PrescriptionsListCreateView(generics.ListCreateAPIView):
    queryset = Prescriptions.objects.all()
    serializer_class = PrescriptionsSerializer


class PrescriptionsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescriptions.objects.all()
    serializer_class = PrescriptionsSerializer


class TraitementListCreateView(generics.ListCreateAPIView):
    queryset = Traitement.objects.all()
    serializer_class = TraitementSerializer


class TraitementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Traitement.objects.all()
    serializer_class = TraitementSerializer


class EtatMaladieListCreateView(generics.ListCreateAPIView):
    queryset = EtatMaladie.objects.all()
    serializer_class = EtatMaladieSerializer


class EtatMaladieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EtatMaladie.objects.all()
    serializer_class = EtatMaladieSerializer
