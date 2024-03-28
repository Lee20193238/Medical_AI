
import pandas as pd
import os

data_folder = "C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/"


def get_df_stone(k_fold, data_folder):
    df_train = pd.read_csv(os.path.join( data_folder, 'train.csv'))

    # 고유 'title' 값에 대한 fold 번호 할당

    unique_titles = df_train['title'].unique()
    print(len(unique_titles))
    patients2fold = {title: i % k_fold for i, title in enumerate(unique_titles)}

    # 각 데이터 포인트에 fold 번호 매핑
    df_train['fold'] = df_train['title'].map(patients2fold)

    # 결과 확인
    print(df_train['fold'].value_counts())

get_df_stone(5, data_folder)