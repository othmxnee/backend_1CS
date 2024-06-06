
from django.http import JsonResponse
from rest_framework import generics

from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import csv

from .models import Assistant, Cohorte, Etudiant, Promo,Chapitre,Mooc,Cours,Fiche,Devoir,Commentaire, Responsable,Ressource,Niveau,Module


from .serializers import AssistantModelSerializer, CohorteModelSerializer, EtudiantModelSerializer, PromoModelSerializer,ChapitreModelSerializer,MoocModelSerializer,CoursModelSerializer,FicheModelSerializer,DevoirModelSerializer,CommentaireModelSerializer, ResponsableModelSerializer,RessourceModelSerializer,NiveauModelSerializer,ModuleModelSerializer
#Promo:
class PromoView(generics.ListCreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoModelSerializer
    def perform_create(self, serializer):
        # Save the Promo instance first
        promo = serializer.save()

        # Create a Cohorte instance related to the Promo
        Cohorte.objects.create(
           nom=promo.nom,  # Use the name of the Promo
            size=0,         # Set the initial size to 0 or another default value
            promo=promo   # Set the initial size to 0 or another default value
        )


class SinglePromoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PromoModelSerializer
    def get_queryset(self):
        return Promo.objects.filter(pk = self.kwargs['pk'])

#chapitre:

class ChapitreView(generics.ListCreateAPIView):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreModelSerializer

class SingleChapitreView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChapitreModelSerializer
    def get_queryset(self):
        return Chapitre.objects.filter(pk = self.kwargs['pk'])

#Moocs:

class MoocView(generics.ListCreateAPIView):
    queryset = Mooc.objects.all()
    serializer_class = MoocModelSerializer

class SingleMoocView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoocModelSerializer
    def get_queryset(self):
        return Mooc.objects.filter(pk = self.kwargs['pk'])

#Cours:

class CoursView(generics.ListCreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursModelSerializer

class SingleCoursView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoursModelSerializer
    def get_queryset(self):
        return Cours.objects.filter(pk = self.kwargs['pk'])

#Fiche_td_tp:

class FicheView(generics.ListCreateAPIView):
    queryset = Fiche.objects.all()
    serializer_class = FicheModelSerializer

class SingleFicheView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FicheModelSerializer
    def get_queryset(self):
        return Fiche.objects.filter(pk = self.kwargs['pk'])

#Devoir:

class DevoirView(generics.ListCreateAPIView):
    queryset = Devoir.objects.all()
    serializer_class = DevoirModelSerializer

class SingleDevoirView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DevoirModelSerializer
    def get_queryset(self):
        return Devoir.objects.filter(pk = self.kwargs['pk'])

#Commentaire_sur_cours:

class CommentaireView(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireModelSerializer

class SingleCommentaireView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentaireModelSerializer
    def get_queryset(self):
        return Commentaire.objects.filter(pk = self.kwargs['pk'])

#Ressource:

class RessourceView(generics.ListCreateAPIView):
    queryset = Ressource.objects.all()
    serializer_class = RessourceModelSerializer

class SingleRessourceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RessourceModelSerializer
    def get_queryset(self):
        return Ressource.objects.filter(pk = self.kwargs['pk'])


#Niveau:

class NiveauView(generics.ListCreateAPIView):
    queryset = Niveau.objects.all()
    serializer_class = NiveauModelSerializer

class SingleNiveauView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NiveauModelSerializer
    def get_queryset(self):
        return Niveau.objects.filter(pk = self.kwargs['pk'])

#Module:

class ModuleView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleModelSerializer

class SingleModuleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ModuleModelSerializer
    def get_queryset(self):
        return Module.objects.filter(pk = self.kwargs['pk'])
    
class CSVUploadViewEtudiant(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.data:
            return Response({"error": "No file was provided."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.data['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)

        # Skip the header row
        next(reader, None)

        # Check if all emails end with @esi-sba.dz
        for row in reader:
            _, email, _ = row
            if not email.endswith('@esi-sba.dz'):
                return Response({"error": "All emails must end with @esi-sba.dz"}, status=status.HTTP_400_BAD_REQUEST)

        # Reset the reader because it was exhausted in the check above
        file.seek(0)
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader, None)  # Skip the header row again

        # Process CSV data
        for row in reader:
            fullname, email, matricule = row
            
            Etudiant.objects.update_or_create(
                matricule=matricule,
                defaults={
                    'fullname': fullname,
                    'email': email,
                    'password':  matricule
                }
            )

        return Response({"success": "File uploaded successfully"}, status=status.HTTP_201_CREATED)




    #etudiant
class EtudiantView(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantModelSerializer


class SingleEtudiantView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EtudiantModelSerializer
    def get_queryset(self):
        return Etudiant.objects.filter(pk = self.kwargs['pk'])
class CohorteView(generics.ListCreateAPIView):
    queryset = Cohorte.objects.all()
    serializer_class = CohorteModelSerializer

class SingleCohorteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CohorteModelSerializer
    def get_queryset(self):
        return Cohorte.objects.filter(pk = self.kwargs['pk'])
class ProfView(generics.ListCreateAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantModelSerializer


class SingleProfView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssistantModelSerializer
    def get_queryset(self):
        return Assistant.objects.filter(pk = self.kwargs['pk'])

class ResponsableView(generics.ListCreateAPIView):
    queryset = Responsable.objects.all()
    serializer_class = ResponsableModelSerializer


class SingleResponsableView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResponsableModelSerializer
    def get_queryset(self):
        return Responsable.objects.filter(pk = self.kwargs['pk'])