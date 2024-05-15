import csv

from equipment.serializers import GPSerializer
from rest_framework.response import Response


def copy():
    with open('../GP.csv') as f:
        csvreader = csv.DictReader(f)
        count = 0
        for item in csvreader:
            print(item)
        # for row in csvreader:
        #     serializer = GPSerializer(data=row)
        #     if serializer.is_valid():
        #         serializer.save()
        #     else:
        #         print(serializer.errors)
        # return Response(serializer.data, status=201)

copy()