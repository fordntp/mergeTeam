from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from mergeTeamApp import consumers  # Import your WebSocket consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/some_path/", consumers.YourConsumer.as_asgi()),  # Define your WebSocket path and consumer
    ]),
})
