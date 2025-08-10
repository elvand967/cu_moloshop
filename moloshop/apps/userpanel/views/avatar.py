
# moloshop/apps/userpanel/views/avatar.py

from django.http import HttpResponse
from django.contrib.auth import get_user_model
from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO


def generate_avatar_view(request, user_id):
    """
    Генерация PNG-заглушки аватарки с первой буквой email.
    """
    User = get_user_model()
    user = User.objects.filter(pk=user_id).first()

    if not user:
        return HttpResponse(status=404)

    letter = (user.email[0].upper() if user.email else "?")
    size = 128

    bg_colors = ['#FF6B6B', '#6BCB77', '#4D96FF', '#FFD93D', '#9D4EDD']
    text_color = '#FFFFFF'

    img = Image.new("RGB", (size, size), random.choice(bg_colors))
    draw = ImageDraw.Draw(img)

    font_size = int(size * 0.6)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(letter, font=font)
    position = ((size - text_width) / 2, (size - text_height) / 2)
    draw.text(position, letter, fill=text_color, font=font)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")
