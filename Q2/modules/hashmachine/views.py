from rest_framework          import generics
from rest_framework.response import Response
from .utils.common_utils     import multithread_get_random_hash

import time
import hashlib


class RandomHashView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # wait for one second
        time.sleep(1)
        time_now = time.time()
        hash = hashlib.sha256(str(time_now).encode('utf-8')).hexdigest()
        return Response(hash)


class GetOddHashView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # gets hash from RandomHashView
        hash      = RandomHashView.get(self, request).data
        last_char = hash[-1]

        # keep asking for a new hash until the last character is a digit and is odd
        while not (last_char.isdigit() and int(last_char) % 2 == 1):
            hash      = RandomHashView.get(self, request).data
            last_char = hash[-1]

        return Response(hash, status=200)


class OptimizingOddHashView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):

        hash = ''

        while not hash:
            hash = multithread_get_random_hash(self, request, RandomHashView)

        return Response(hash, status=200)