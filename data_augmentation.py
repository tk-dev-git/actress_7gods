import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image

BASE_DIR = '/Users/taishi/Documents/Develop/pre_process/img_download/origin'
GENERATE_DIR = '/Users/taishi/Documents/Develop/pre_process/img_download/generate'
PARAMS = {
    'rotation_range': 30,
    'width_shift_range': 0.1,
    'height_shift_range': 0.1,
    'horizontal_flip': True,
    'brightness_range': [0.6, 0.8],
    'zoom_range': 0.2
}


def conv_4darray(img_path):
    img = image.load_img(img_path)
    arry = image.img_to_array(img)
    return arry.reshape((1,) + arry.shape)


def generate_image(x=None, row=3, col=3, prefix=None):
    max_img_num = row * col
    generate_dir = os.path.join(GENERATE_DIR, prefix)
    if not os.path.exists(generate_dir):
        os.makedirs(generate_dir)
    datagen = image.ImageDataGenerator(**PARAMS)
    imgs = []
    for img in datagen.flow(x, batch_size=1, save_to_dir=generate_dir, save_prefix=prefix, save_format='jpg'):
        imgs.append(image.array_to_img(img[0], scale=True))
        if (len(imgs) % max_img_num) == 0:
            break
    return imgs


def show_image(imgs, row=3, col=3):
    for i, img in enumerate(imgs):
        plot_num = i + 1
        plt.subplot(row, col, plot_num)
        plt.tick_params(labelbottom="off")    # x軸の削除
        plt.tick_params(labelleft="off")      # y軸の削除
        plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    # ターゲットディレクトリを取得
    dirs = []
    for d in os.listdir(BASE_DIR):
        d_path = os.path.join(BASE_DIR, d)
        if os.path.isdir(d_path):
            dirs.append(d)

    # ターゲット画像ファイルを取得
    files = []
    for _dir in dirs:
        search = os.path.join(BASE_DIR, _dir, '*.jpg')
        files = glob.glob(search)
        print('==========================================')
        print('dir: [{}]({}) -> '.format(_dir, len(files)))
        for _file in files:
            print('{}, '.format(_file))
            x = conv_4darray(_file)
            # imgs = generate_image(x)
            imgs = generate_image(x=x, row=3, col=2, prefix=_dir)
            # show_image(imgs)
            # show_image(imgs=imgs, row=6, col=5)
    
