from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = f"Hello,{name}"
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/',handle),
        we.get('/{name}',handle)])

if__name__ == '__main__':
    web.run_app(app)