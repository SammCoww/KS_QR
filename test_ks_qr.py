import cv2
import numpy as np

from ks_qr import make_qr

for link in ["https://example.com", "https://kappasigma.org/chapters/some/long/path?with=query&and=more" * 3]:
    img = cv2.cvtColor(np.array(make_qr(link)), cv2.COLOR_RGB2BGR)
    decoded, _, _ = cv2.QRCodeDetector().detectAndDecode(img)
    assert decoded == link, (link, decoded)
print("ok")
