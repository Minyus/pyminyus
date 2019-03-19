from PIL import Image, ImageDraw
from PIL.ImageChops import multiply
import numpy as np

try:
    import matplotlib.pyplot as plt
except:
    print('### matplotlib.pyplot could not be imported.')

def imshow(image):
    plt.imshow(image)
    plt.show()
    
def pilshow(pil_image):
    imshow(np.asarray(pil_image))
    

def mask_boxes(img, boxes=[[0,0,100,100]]):
    """
    Args:
        img: PIL image
        boxes: [[(left, upper, right, lower)]]
    Returns: PIL image    
    """
    w, h = img.size
    img_mask = Image.fromarray(np.full((h,w,3), fill_value=0, dtype=np.uint8))
    d = ImageDraw.Draw(img_mask)
    for box in boxes:
        d.rectangle(box, fill='white')
    img_out = multiply(img, img_mask)
    return img_out

if __name__=="__main__":
    boxes = [[300, 100, 400, 200],
             [140, 120, 265, 170]]
    image_path = '../val/instant_coffee/instant_coffee53.jpg'
    with Image.open(image_path) as img:
        image_pil = img.copy()
    pilshow(mask_boxes(image_pil, boxes))