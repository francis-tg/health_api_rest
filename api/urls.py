# urls.py
from django.urls import path
from .views import (
    PatientListCreateView,
    PatientRetrieveUpdateDestroyView,
    MaladieListCreateView,
    MaladieRetrieveUpdateDestroyView,
    PrescriptionsListCreateView,
    PrescriptionsRetrieveUpdateDestroyView,
    TraitementListCreateView,
    TraitementRetrieveUpdateDestroyView,
    EtatMaladieListCreateView,
    EtatMaladieRetrieveUpdateDestroyView,
    PatientWithPrescriptionsView,
    PatientWithTraitementView,
    PatientWithEtatMaladieView,
)

urlpatterns = [
    path("patients/", PatientListCreateView.as_view(), name="patient-list-create"),
    path(
        "patients/<int:pk>/",
        PatientRetrieveUpdateDestroyView.as_view(),
        name="patient-retrieve-update-destroy",
    ),
    path("maladies/", MaladieListCreateView.as_view(), name="maladie-list-create"),
    path(
        "maladies/<int:pk>/",
        MaladieRetrieveUpdateDestroyView.as_view(),
        name="maladie-retrieve-update-destroy",
    ),
    path(
        "prescriptions/",
        PrescriptionsListCreateView.as_view(),
        name="prescriptions-list-create",
    ),
    path(
        "prescriptions/<int:pk>/",
        PrescriptionsRetrieveUpdateDestroyView.as_view(),
        name="prescriptions-retrieve-update-destroy",
    ),
    path(
        "traitements/",
        TraitementListCreateView.as_view(),
        name="traitement-list-create",
    ),
    path(
        "traitements/<int:pk>/",
        TraitementRetrieveUpdateDestroyView.as_view(),
        name="traitement-retrieve-update-destroy",
    ),
    path(
        "etatmaladies/",
        EtatMaladieListCreateView.as_view(),
        name="etatmaladie-list-create",
    ),
    path(
        "etatmaladies/<int:pk>/",
        EtatMaladieRetrieveUpdateDestroyView.as_view(),
        name="etatmaladie-retrieve-update-destroy",
    ),
    path(
        "patients/<int:pk>/prescriptions/",
        PatientWithPrescriptionsView.as_view(),
        name="patient-prescriptions",
    ),
    path(
        "patients/<int:pk>/traitements/",
        PatientWithTraitementView.as_view(),
        name="patient-traitement",
    ),
    path(
        "patients/<int:pk>/etatmaladies/",
        PatientWithEtatMaladieView.as_view(),
        name="patient-etatmaladie",
    ),
]
