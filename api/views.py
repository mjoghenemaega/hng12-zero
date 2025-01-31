from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
import pytz

@api_view(["GET"])
def get_info(request):
    data = {
        "email": "mjoghenemaega@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/mjoghenemaega/hng12-zero"
    }
    return Response(data)
