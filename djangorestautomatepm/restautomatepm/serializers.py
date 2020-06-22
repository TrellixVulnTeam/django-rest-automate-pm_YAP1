from rest_framework import serializers
from restautomatepm.models import Projects, Phases, Log

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Projects 
        fields = ['id', 'name', 'description', 'complete', 'status', 'lastupdated', 'company']
class PhasesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Phases
        fields = ['id', 'name', 'description', 'complete', 'active', 'lastupdated', 'start', 'end', 'projectId']

class LogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Log
        fields = ['id', 'description', 'notes', 'timestamp', 'projectId']
