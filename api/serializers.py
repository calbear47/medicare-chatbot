from rest_framework import serializers

class QuerySerializer(serializers.Serializer):
    """
    Serializer for plan queries.
    """
    query = serializers.CharField(required=True)
    plan_ids = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )

class PDFUploadSerializer(serializers.Serializer):
    """
    Serializer for PDF uploads.
    """
    file = serializers.FileField()
    plan_id = serializers.CharField()
    year = serializers.IntegerField(min_value=2000, max_value=2100)

    def validate_file(self, value):
        """
        Validate the uploaded file is a PDF.
        """
        if not value.name.endswith('.pdf'):
            raise serializers.ValidationError("File must be a PDF")
        if value.size > 10 * 1024 * 1024:  # 10MB limit
            raise serializers.ValidationError("File too large")
        return value