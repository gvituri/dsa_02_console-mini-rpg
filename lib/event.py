from collections import defaultdict

subscribers = defaultdict(list)

def subscribe_to(event_type, func):
    subscribers[event_type].append(func)

def notfy_listeners(event_type):
    if event_type in subscribers:
        for func in subscribers[event_type]:
            func()