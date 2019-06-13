from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

from echo.consumers import EchoChamberConsumer


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "websocket": URLRouter([
        url(r"^echo/$", EchoChamberConsumer),
    ]),
})
