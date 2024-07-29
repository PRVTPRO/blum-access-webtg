import asyncio
from mitmproxy import http
from mitmproxy.tools.dump import DumpMaster
from mitmproxy import options

class HeaderModifier:
    def response(self, flow: http.HTTPFlow) -> None:
        # Удаляем заголовки
        headers_to_remove = [
            "Content-Security-Policy",
            "X-Content-Security-Policy",
            "X-Frame-Options"
        ]
        for header in headers_to_remove:
            if header in flow.response.headers:
                del flow.response.headers[header]
        
        # Добавляем заголовок Access-Control-Allow-Origin
        flow.response.headers["Access-Control-Allow-Origin"] = "*"

addons = [
    HeaderModifier()
]

async def start_proxy():
    opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
    m = DumpMaster(opts)
    m.addons.add(*addons)
    try:
        await m.run()
    except KeyboardInterrupt:
        m.shutdown()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_proxy())
