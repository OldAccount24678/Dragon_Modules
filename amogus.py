# module by t.me/KeyZenD
# Adaptation for Dragon-Userbot by AmokDev
# AmokDev's' GitHub - https://github.com/AmokDev 
#¯\_(ツ)_/¯

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix

from requests import get
from io import BytesIO
from random import randint, choice
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap

@Client.on_message(filters.command("mother", prefix) & filters.me)
async def kekkkk(client: Client, message: Message):
	await message.edit("<code>This is an example module</code>")


@Client.on_message(filters.command("amogus", prefix) & filters.me)
async def amogus(client: Client, message: Message):
	clrs = {'red': 1, 'lime': 2, 'green': 3, 'blue': 4, 'cyan': 5, 'brown': 6, 'purple': 7, 'pink': 8, 'orange': 9, 'yellow': 10, 'white': 11, 'black': 12}
	clr = randint(1,12)
	text = " ".join(message.command[1:])

	url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
	font = ImageFont.truetype(BytesIO(get(url+"bold.ttf").content), 60)
	imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
	text_ = "\n".join(["\n".join(wrap(part, 30)) for part in text.split("\n")])
	w, h = ImageDraw.Draw(Image.new("RGB", (1,1))).multiline_textsize(text_, font, stroke_width=2)
	text = Image.new("RGBA", (w+30, h+30))
	ImageDraw.Draw(text).multiline_text((15,15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000")
	w = imposter.width + text.width + 10
	h = max(imposter.height, text.height)
	image = Image.new("RGBA", (w, h))
	image.paste(imposter, (0, h-imposter.height), imposter)
	image.paste(text, (w-text.width, 0), text)
	image.thumbnail((512, 512))
	output = BytesIO()
	output.name = "imposter.webp"
	image.save(output)
	output.seek(0)
	await message.delete()
	await client.send_sticker(message.chat.id, output)

modules_help["Amogus"] = {
	"amogus [text]": "amgus, tun tun tun tun tun tun tun tudududn tun tun"
}