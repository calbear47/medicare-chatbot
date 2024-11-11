from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging
from .serializers import QuerySerializer, PDFUploadSerializer
from pdf_processor.extraction import PDFExtractor
from pdf_processor.rag_chain import RAGChain

logger = logging.getLogger(__name__)

@api_view(['POST'])
async def query_plans(request):
    """
    Endpoint to query Medicare plan information.
    """
    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        try:
            rag_chain = RAGChain()
            result = await rag_chain.query(
                question=serializer.validated_data['query'],
                plan_ids=serializer.validated_data.get('plan_ids')
            )
            return Response({
                'response': result.response,
                'sources': result.source_documents,
                'confidence': result.confidence_score
            })
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return Response(
                {'error': 'Failed to process query'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def upload_pdf(request):
    """
    Endpoint to upload and process new PDF documents.
    """
    serializer = PDFUploadSerializer(data=request.data)
    if serializer.is_valid():
        try:
            file_obj = serializer.validated_data['file']
            plan_id = serializer.validated_data['plan_id']
            year = serializer.validated_data['year']

            extractor = PDFExtractor()
            extracted_plan = extractor.extract_from_file(
                file_obj.temporary_file_path(),
                plan_id,
                year
            )

            return Response({
                'message': 'PDF processed successfully',
                'plan_id': plan_id,
                'sections_found': list(extracted_plan.sections.keys())
            })
        except Exception as e:
            logger.error(f"Error processing PDF: {str(e)}")
            return Response(
                {'error': 'Failed to process PDF'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def health_check(request):
    """
    Basic health check endpoint.
    """
    return Response({'status': 'healthy'})