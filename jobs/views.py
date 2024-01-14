from .models import Job, Candidate, Action
from .serializers import JobSerializer, CandidateSerializer, ActionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class JobList(APIView):

    def get(self, request, pk, format=None):
        candidate = Candidate.objects.get(pk=pk)
        # print(candidate.location + " " + candidate.industry)
        jobs = Job.objects.filter(location=candidate.location, industry=candidate.industry)
        print(jobs)
        serializer = JobSerializer(jobs, many=True)
        # serializer = CandidateSerializer(candidate)
        return Response(serializer.data)


class Act(APIView):
    def post(self, request, pk, job, act, n, format=None):
        candidate = Candidate.objects.get(pk=pk)
        job = Job.objects.get(pk=job)

        action = {
            'candidate': candidate.pk,
            'job': job.pk,
            'actionType': act + " " + n
        }
        serializer = ActionSerializer(data = action)
        if serializer.is_valid():
            serializer.save()
            print(act + " " + n)
            if act == "cta" and n == "2":
                return Response(job.contact)
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
        