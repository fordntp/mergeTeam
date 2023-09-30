# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass  # Handle WebSocket disconnect here, if needed

    async def receive(self, text_data):
        # Handle WebSocket messages received from the client, if needed
        pass

    async def update_data(self, event):
        # This method handles real-time updates
        data = event['data']
        await self.send(text_data=json.dumps({'data': data}))
