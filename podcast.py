import requests
from selectolax.parser import HTMLParser
import chompjs
import json
import rich
import pyglet

podcast = "https://www.podbean.com/media/share/dir-hrpga-19b6ed45?utm_campaign=w_share_ep&utm_medium=dlink&utm_source=w_share"

res = requests.get(podcast)

html = HTMLParser(res.text)


data = html.css('script[type="application/ld+json"]')


for script in data:
    new = chompjs.parse_js_object(script.text())
    parse = new
    url = parse["associatedMedia"]["contentUrl"]

    rich.print(url)
    mp3 = url

    source = pyglet.media.load(mp3)
    player = pyglet.media.Player()
    player.queue(source)
    player.play()


pyglet.app.run()
