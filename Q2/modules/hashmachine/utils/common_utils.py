from concurrent.futures import ThreadPoolExecutor


def call_api(data, request, class_view):
    response = class_view.get(data, request)
    return response.data


def multithread_get_random_hash(data, request, class_view):
    # Create a thread pool executor.
    executor = ThreadPoolExecutor(max_workers=4)

    futures = []
    for i in range(4):
        futures.append(executor.submit(call_api, data, request, class_view))

    # Get the results of the calls.
    responses = []
    for future in futures:
        responses.append(future.result())

    # Print the responses.
    for hash in responses:
        last_char = hash[-1]
        if last_char.isdigit() and int(last_char) % 2 == 1:
            return hash

    return None