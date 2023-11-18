import qrcode
from PIL import Image

class QrCodeGenerator():
  def __init__(self):
    self.qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size = 16,
        border=0,
    )
  def generator_qr_code(self, qrcode_content: str):
    self.qr.add_data(qrcode_content)
    self.qr.make(fit=True)

    img = self.qr.make_image(fill_color="black", back_color="white")
    return img.get_image()

  def add_offset_background(self, img: Image, offset_min: int = 0):
    w, h = img.size
    w = (w + 255 + offset_min)
    h = (h + 255 + offset_min)

    if w > 1024:
      raise ValueError("Qr Code is too big, please re-generate a shorter URL")
    bg_img = Image.new('L', (w,h), 255)
    coords = ((w-img.size[0]) // 2 // 16*16,
              (h-img.size[1]) // 2// 16*16)
    bg_img.paste(img, coords)
    return bg_img

qrcode_gen = QrCodeGenerator()
qrcode_img = qrcode_gen.generator_qr_code('https://bit.ly/youtube_codexplore')
bg_qrcode_img = qrcode_gen.add_offset_background(qrcode_img)
bg_qrcode_img.size