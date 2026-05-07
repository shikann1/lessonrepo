KEYPOINTS_NAMES = [
    "nose",  # 0 鼻
    "eye(L)",  # 1 左目
    "eye(R)",  # 2 右目
    "ear(L)",  # 3 左耳
    "ear(R)",  # 4 右耳
    "shoulder(L)",  # 5 左肩
    "shoulder(R)",  # 6 右肩
    "elbow(L)",  # 7 左肘
    "elbow(R)",  # 8 右肘
    "wrist(L)",  # 9 左手首
    "wrist(R)",  # 10 右手首
    "hip(L)",  # 11 左腰
    "hip(R)",  # 12 右腰
    "knee(L)",  # 13 左膝
    "knee(R)",  # 14 右膝
    "ankle(L)",  # 15 左足首
    "ankle(R)",  # 16 右足首
]# 姿勢分析結果のキーポイントを取得する
#keypoints = results[0].keypoints.xy  # 座標
#confs = results[0].keypoints.conf  # 信頼度

#for keypoint in keypoints:
    #for idx, point in enumerate(keypoint):
        #x, y = int(point[0]), int(point[1])
        #score = confs[0][idx]

        # スコアが0.5以下なら描画しない
        #if score < 0.5:
            #continue

#上記のコードをコメントアウトし、以下のコードを追記してください

keypoints = results[0].keypoints.xy[0]  # 1人目のキーポイント
    confs = results[0].keypoints.conf[0]   # 1人目の信頼度

    for idx, (point, score) in enumerate(zip(keypoints, confs)):
        x, y = int(point[0]), int(point[1])
        if score < 0.5:
            continue