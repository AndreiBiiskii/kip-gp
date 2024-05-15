import csv

from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from equipment.models import GP, Contractor, Worker, Kait, Approve, Kip
from equipment.serializers import GPSerializer, KaitSerializer, KipSerializer, ContractorSerializer, WorkerSerializer, \
    ApproveSerializer, KipSerializerCopy
from rest_framework import mixins


class CopyAPIView(APIView):
    def get(self, request):
        with open('./kait.csv') as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                serializer = KaitSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()

        with open('./contractor.csv') as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                serializer = ContractorSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()

        with open('./GP.csv') as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                serializer = GPSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()

        with open('./worker.csv') as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                serializer = WorkerSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()

        with open('./approve.csv') as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                serializer = ApproveSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()

        with open('./copy1.csv') as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                try:
                    row['poz_GP'] = (GP.objects.get(number=row['poz_GP'])).id
                except:
                    row['poz_GP'] = None
                try:
                    row['executor_3'] = (Contractor.objects.get(name=row['executor_3'])).id

                except:
                    row['executor_3'] = None
                try:
                    row['executor_1'] = (Kait.objects.get(name=row['executor_1'])).id
                except:
                    row['executor_1'] = None
                try:
                    row['executor_2'] = (Worker.objects.get(name=row['executor_2'])).id
                except:
                    row['executor_2'] = None
                try:
                    row['person_approving'] = (Approve.objects.get(name=row['person_approving'])).id
                except:
                    row['person_approving'] = None
                serializer = KipSerializerCopy(data=row)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
        return Response('bin')


class GPAPIView(generics.ListAPIView):
    queryset = GP.objects.all()
    serializer_class = GPSerializer


class KaitAPIView(generics.ListAPIView):
    queryset = Kait.objects.all()
    serializer_class = KaitSerializer


class KipAPIViewSet(viewsets.ModelViewSet):
    queryset = Kip.objects.all()
    serializer_class = KipSerializer


class KipAPIViewDetail(APIView):
    def get(self, request):
        queryset = Kip.objects.filter(serial_number__icontains=self.request.GET.get('number'))
        serializer = KipSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
