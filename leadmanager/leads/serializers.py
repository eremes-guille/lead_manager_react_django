from rest_framework import serializers
from leads.models import Lead

# Lead Serializer
class LeadSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'