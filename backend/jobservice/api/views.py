from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobData
from .serilizer import JobDataSerializer

# View to handle list and creation of jobs
class JobDataListView(APIView):
    def get(self, request):
        jobs = JobData.objects.all()
        serializer = JobDataSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to handle retrieving, updating, and deleting a single job
class JobDataDetailView(APIView):
    def get(self, request, pk):
        try:
            job = JobData.objects.get(pk=pk)
        except JobData.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = JobDataSerializer(job)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            job = JobData.objects.get(pk=pk)
        except JobData.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = JobDataSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            job = JobData.objects.get(pk=pk)
            job.delete()
            return Response({"message": "Job deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except JobData.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)




from .scraper import run_spider

class ScrapeJobView(APIView):
    def post(self, request):
        # Extract the start URL from the request
        start_url = request.data.get('start_url')

        if not start_url:
            return Response({"error": "start_url is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Run the spider and get the scraped data
            scraped_data = run_spider(start_url)
            return Response({"data": scraped_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
