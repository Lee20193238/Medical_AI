#
# ## meta data
# # 타깃값과 상관성이 높은 변수만 선택해 학습
#
# import pandas as pd
# from sklearn.model_selection import train_test_split
#
# # print(bxpc3.columns)
# # print(capan2.columns)
# # print(h6c7.columns)
# # print(psn1.columns)
#
#
# # 'Surface area (um²)','Concentration (pg/um³)'
# # psn1 = psn1.drop(columns=['Unnamed: 0_x', 'Unnamed: 0.1_x'])
# # psn1 = psn1.rename(columns={'No._x': 'No.'})
#
#
# # psn1.to_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/PSN1.csv", index = False)
#
# # merged_df = pd.concat([bxpc3, capan2, h6c7, psn1]) # 74 + 55 + 105 + 145
# # print(merged_df.columns)
# # print(merged_df) # 379 x 16
#
#
# # merged_df.to_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/meta.csv", index = False)
#
# # 기존 train data에 해당 열만 추가해 새로운 train data생성? ㅌㅌ
#
#
# # meta = pd.read_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/meta.csv")
# # print(len(meta.columns))
# #
# # print(meta['Surface area (um²)'].head())
# # print(meta['Concentration (pg/um³)'].head())
# #
# # original = pd.read_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/train.csv")
# # print(len(original.columns)) # 4
# # print(len(original)) # 11100
# # ## NAN의 경우 어떻게 처리할지
# #
# #
# # merged_df = pd.read_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/merged.csv")
# # print(merged_df.columns)
# # print(merged_df)
# #
# # # merged_df.to_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/merged.csv")
# #
# # unique_titles_count = original['title'].nunique()
# # print(unique_titles_count) # 375
# #
# # unique_titles_count1 = meta['Title'].nunique()
# # print(unique_titles_count1) # 379
# #
# # unique_titles_count2 = merged_df['title'].nunique()
# # print(unique_titles_count2) # 375
# #
# #
# # # title_counts = merged_df['title'].value_counts()
# # #
# # # print(title_counts)
# #
# #
# # # 'title' 열에서 각 유니크한 값이 나타나는 횟수
# # title_counts = merged_df['title'].value_counts()
# #
# # title_counts_df = title_counts.reset_index()
# # title_counts_df.columns = ['title', 'count']
# #
# # print(title_counts_df)
# # ## 각 37장이어야 하는데 다 다름 > train, test 로 나누면서 발생
# # title_counts_df.to_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/title_counts.csv")
#
# ## merged_image : raw data 이미지 + 타이틀 + 타깃
# original = pd.read_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/merged_image.csv")
# print(original.columns)
# print(len(original)) #13875 = 37장 x 375
#
#
# # merged_image를 meta data와 병합: 동일한 열 기준 ['title']
#
#
# meta = pd.read_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/meta.csv")
# print(meta.columns)
# print(len(meta)) # 379: 하위 4행은 concentration, surface area 데이터가 없음
#
# # # 두 데이터프레임을 공통된 열 'title'을 기준으로 병합
# # merged_df = pd.merge(original,meta, on='title')
# # print(len(merged_df)) #13875
# # print(merged_df.columns)
#
#
# final = pd.read_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/final.csv")
# print(len(final)) #13875
# print(final.columns)
#
# # title 열 별 데이터 개수 확인: 37장씩인지
#
# # 'title' 열에 대한 데이터 개수를 계산
# title_counts = final['title'].value_counts()
# print(title_counts)
#
# # 모든 'title'의 데이터 개수가 동일한지 확인: value_counts()의 모든 값이 첫 번째 값과 같은지 확인
#
# all_equal = title_counts.nunique() == 1
#
# print("모든 'title'의 데이터 개수가 동일합니까?", all_equal)
#
# print(final['title'].nunique()) # 375
#
# ### train/test set 재생성
# train_df, test_df = train_test_split(final, test_size=0.2)
#
# # train_df.to_csv('C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/train.csv', index=False)
# # test_df.to_csv('C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/test.csv', index=False)
#
# train = pd.read_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/train.csv")
# test = pd.read_csv("C:/Users/mmc/Downloads/Stone_test-master_3/Stone_test-master/data/original_stone/test.csv")
# print(len(train))
# print(len(test))
#
#
# print(train.columns)
#
# # print(len(train1))
# # title_counts = train1['title'].value_counts()
# # print(title_counts)
#
#
#
# ## 다음에 할 것
#
#
# # meta 최종성능확인 [일] [O]
# # meta_result grouping [-] > auc성능 좀 더 높이기
# # predict.py 실행되게 수정
#
# # 경진대회..? // 1/31_수요일까지
#
#
# # image data: lr 변경 또는 다른 작업 수행 후 다시 eval.py 돌려 auc 98.5 달성시키기
#
# # result grouping // 2/5_일요일까지
#
#
# # 상관성 높은 변수 확인해 추가해서 학습시켜보기
#
#
#
#
# path = 'C:/Users/mmc/downloads/Stone_test-master_3/Stone_test-master/oofs/'
#
# # result grouping 결과 csv
# oof = pd.read_csv(path + '5fold_b3_256_30ep_best_grouped_oof.csv')
#
# # 'title' 열에서 유니크한 값들의 개수 계산
# unique_titles_count = oof['title'].nunique()
#
# print(f"유니크한 'title'의 개수: {unique_titles_count}") # 375



import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.device_count())
# print(torch.cuda.get_device_name(torch.cuda.current_device()))