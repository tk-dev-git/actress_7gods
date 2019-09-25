import os
import glob
import pandas as pd

BASE_DIR = '/Users/taishi/Documents/Develop/pre_process/img_download/generate'
BUCKET_URI = 'gs://cloud-api-183809-vcm/actress_7gods'


if __name__ == '__main__':
    # ターゲットディレクトリを取得
    dirs = []
    for d in os.listdir(BASE_DIR):
        d_path = os.path.join(BASE_DIR, d)
        if os.path.isdir(d_path):
            dirs.append(d)
    # ※特定ディレクトリのみに絞り込む場合はコチラ
    # dirs = [
    # ]

    # ターゲット画像ファイルを取得
    files = []
    csv_list = []
    for _dir in dirs:
        search = os.path.join(BASE_DIR, _dir, '*.jpg')
        files = glob.glob(search)
        print('==========================================')
        print('dir: [{}]({}) -> '.format(_dir, len(files)))
        for _index in range(1, len(files)):
            _uri = os.path.join(BUCKET_URI, _dir, '{0}-{1:03d}.jpg'.format(_dir, _index))
            _label = _dir
            print('{},{}'.format(_uri, _label))
            csv_data = []
            csv_data.append(_uri)
            csv_data.append(_label)
            csv_list.append(csv_data)
    
    # pandas DataFrame を作成して CSV を作成
    df = pd.DataFrame(data=csv_list)
    df.to_csv(
        path_or_buf='./active_dataset.csv',
        header=False,
        index=False,
        encoding='utf-8'
    )
