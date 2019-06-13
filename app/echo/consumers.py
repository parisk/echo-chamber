from channels.generic.websocket import AsyncJsonWebsocketConsumer

class EchoChamberConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
    async def receive_json(self, content):
        await self.send_json(content)
    async def disconnect(self, close_code):
        await self.close()
