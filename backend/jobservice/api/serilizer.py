from rest_framework import serializers
from .models import JobData

class JobDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobData
        fields = [
            'id',  # Auto-generated ID
            'job_title',
            'location',
            'posted_at',
            'updated_at',
            'location_type',
            'compensation',
            'employment_type',
            'skills',
            'job_details'
        ]
