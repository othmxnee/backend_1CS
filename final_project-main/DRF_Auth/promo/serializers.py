from rest_framework import serializers
from .models import Assistant, Cohorte, Etudiant, Mooc, Promo,Chapitre,Fiche,Cours,Devoir,Commentaire, Responsable,Ressource,Niveau,Module

class PromoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'

class ChapitreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapitre
        fields = '__all__'
class MoocModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mooc
        fields = '__all__'
class CoursModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'
class FicheModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiche
        fields = '__all__'
class DevoirModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devoir
        fields = '__all__'
class CommentaireModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'
class RessourceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ressource
        fields = '__all__'
class NiveauModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = '__all__'

class EtudiantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['id', 'fullname', 'email', 'matricule', 'password','promo','niveau','cohorte']

class CohorteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohorte
        fields = '__all__'
class ResponsableModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ['id', 'fullname', 'email', 'matricule', 'password']
class AssistantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = ['id', 'fullname', 'email', 'matricule', 'password']
        
class ModuleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['nom', 'description', 'Niveau', 'responsable', 'assistants']
    
    def validate_assistants(self, value):
        if not value:
            raise serializers.ValidationError("A module must have at least one assistant.")
        return value

    def create(self, validated_data):
        assistants = validated_data.pop('assistants')
        module = Module.objects.create(**validated_data)
        if not assistants:
            raise serializers.ValidationError("A module must have at least one assistant.")
        module.assistants.set(assistants)
        return module

    def update(self, instance, validated_data):
        assistants = validated_data.pop('assistants', None)
        instance.nom = validated_data.get('nom', instance.nom)
        instance.description = validated_data.get('description', instance.description)
        instance.Niveau = validated_data.get('Niveau', instance.Niveau)
        instance.responsable = validated_data.get('responsable', instance.responsable)
        instance.save()

        if assistants is not None:
            if not assistants:
                raise serializers.ValidationError("A module must have at least one assistant.")
            instance.assistants.set(assistants)
        
        return instance
