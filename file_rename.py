import os
import glob

BASE_DIR = '/Users/taishi/Documents/Develop/pre_process/img_download/generate'


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
        for _index, _file in enumerate(files):
            renamed = os.path.join(BASE_DIR, _dir, '{0}-{1:03d}.jpg'.format(_dir, (_index + 1)))
            print('rename: {0}'.format(renamed))
            os.rename(_file, renamed)
