# Train-RealTime-info

## 蓄積データ

- JR
  - 中央線
  - 中央特快


## テーブル定義(MySQL)
### Train_Logーブル
| 物理名 | 論理名 | 型 | null | key | default |
| -- | -- | -- | -- | -- | -- |
| id | id | UNSIGN INT(11) | no | prime |  |
| train_id | データID | VARCHAR(255) |  |  |  |
| odpt_type | ODPTタイプ | VARCHAR(255) |  |  |  |
| dc_date | 生成時刻 | VARCHAR(255) |  |  |  |
| dct_valid | 有効期限 | VARCHAR(255) |  |  |  |
| odpt_delay | 遅延情報 | INT(10) |  |  |  |
| odpt_railway | 路線名 | VARCHAR(255) |  |  |  |
| odpt_operator | 運営会社 | VARCHAR(255) |  |  |  |
| odpt_train_number | 列車番号 | VARCHAR(255) |  |  |  |
| odpt_train_type | 種別 | VARCHAR(255) |  |  |  |
| odpt_toStation | 次駅 | VARCHAR(255) |  |  |  |
| odpt_from_station | 出発駅 | VARCHAR(255) |  |  |  |
| odpt_rail_direction | 進行方向 | VARCHAR(255) |  |  |  |
| odpt_car_composition | 編成数 | INT(10) |  |  |  |
| odpt_destination_station | 行先 | VARCHAR(255) |  |  |  |
| created_at | 作成日 | TATETIME | no | | CURRENT_TIMESTAMP |
| updated_at | 更新日 | TATETIME | no | | CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP |
