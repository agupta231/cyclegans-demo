import numpy as np
import base64
import PIL.Image
import io


def requestb64_to_image(req: str):
  prefix, _, b64 = req.partition(',')
  buf = io.BytesIO(base64.b64decode(b64))
  return PIL.Image.open(buf)


def numpy_img2b64req(img: np.ndarray):
  amin = np.amin(img)
  amax = np.amax(img)
  norm = (255 * (img - amin) / (amax - amin)).astype(np.uint8)

  pil_img = PIL.Image.fromarray(norm)
  buffer = io.BytesIO()
  pil_img.save(buffer, format='PNG')
  return 'data:image/png;base64,' + \
         base64.b64encode(buffer.getvalue()).decode('utf-8')