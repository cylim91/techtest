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


class CheckHashView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # gets hash from RandomHashView
        hash      = RandomHashView.get(self, request).data
        last_char = hash[-1]

        if last_char.isdigit() and int(last_char) % 2 == 0:
            return Response({'hash': hash, 'result': 'not odd'}, status=400)
        else:
            return Response({'hash': hash, 'result': 'odd'}, status=200)
