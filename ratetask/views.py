from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import connection
cursor = connection.cursor()

class AverageDailyPrice(APIView):
    def get(self, request, *args, **kwargs):
        cursor.execute(
            """
            SELECT sub_query.day, ROUND(AVG(sub_query.price::numeric), 2)
            FROM (
                SELECT px.orig_code, port.parent_slug "origin", px.dest_code, 
                    port_1.parent_slug "destination",
                    px.day, px.price 
                FROM prices px
                JOIN ports port ON px.orig_code=port.code
                JOIN ports port_1 ON px.dest_code=port_1.code 
                ) sub_query 
            WHERE sub_query.day BETWEEN '{}' AND '{}'
            AND (sub_query.orig_code = '{}' OR sub_query.origin = '{}')  
            AND (sub_query.dest_code = '{}' OR sub_query.destination = '{}')
            GROUP BY sub_query.day 
            ORDER BY sub_query.day
            """
            .format(self.kwargs["date_from"], 
                        self.kwargs["date_to"], 
                        self.kwargs['origin'],
                        self.kwargs['origin'],
                        self.kwargs['destination'],
                        self.kwargs['destination']
                        ))
        res = cursor.fetchall()

        keys = ("day", "average_price")

        # convert list of tuples to list
        res = [dict(zip(keys, values)) for values in res]
        
        return Response(res, status=status.HTTP_200_OK)
