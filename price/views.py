from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.

class AveragePrice(APIView):
    def get(self, request, *args, **kwargs):
        pass


class DatasetValidate(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body.decode())
        accesible, _ = check_sas_uri_accessible(json_data.get("link"))

        if accesible:
            return Response(
                {
                    "success": True,
                },
                status=status.HTTP_200_OK,
            )
        raise ValidationError({"message": "Error Accessing URI"})
