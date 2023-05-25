from rest_framework          import generics
from rest_framework.response import Response
import time
import hashlib


class RandomHashView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # wait for one second
        time.sleep(1)
        time_now = time.time()
        hash = hashlib.sha256(str(time_now).encode('utf-8')).hexdigest()
        return Response(hash)