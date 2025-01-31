from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
import pytz

@api_view(["GET"])
def get_info(request):
    data = {
        "email": "your-email@example.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/yourusername/your-repo"
    }
    return Response(data)
