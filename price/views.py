from django.shortcuts import render
from rest_framework.views import APIView


from django.db import connection
cursor = connection.cursor()

class AveragePrice(APIView):
    def get(self, request, *args, **kwargs):
        cursor.execute(
            """
            SELECT sub_query.day, avg(sub_query.price) 
            FROM (
                SELECT px.orig_code, port.parent_slug "origin", px.dest_code, 
                    port_1.parent_slug "destination",
                    px.day, px.price 
                FROM prices px
                JOIN ports port ON px.orig_code=port.code
                JOIN ports port_1 ON px.dest_code=port_1.code 
                ) sub_query 
            WHERE sub_query.day between {} AND {}'
            AND (sub_query.orig_code = {} OR sub_query.origin = {})  
            AND (sub_query.dest_code = {} OR sub_query.destination = {})
            group by sub_query.day 
            order by sub_query.day
            """
            .format(self.kwargs["date_from"], 
                        self.kwargs["date_to"], 
                        self.kwargs['origin'],
                        self.kwargs['origin'],
                        self.kwargs['destination'],
                        self.kwargs['destination'],
                        ))

        print(cursor.fetchall())
