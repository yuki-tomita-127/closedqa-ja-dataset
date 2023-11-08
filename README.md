# closedqa-ja-dataset
## 概要
趣味でClosedQAの日本語データセットを作成しています。  
目標データ数は**2000個**です。  

基本的には[databricks/databricks-dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k)の`ClosedQA`形式にならい、WikipediaのURLやサブカテゴリのフィールドを追加しています。

万が一、内容に誤りがありましたらご指摘いただけますと助かります。

## 進捗
登録データ数: 1/2000
```
[--------------------------------------------------] 0.05%
```

## 作業記録
### 2023-11-08
- 作業時間: 1h
- 新規データ: 1個
- データ修正: 0個
- データ削除: 0個
- ひとこと: まずは最初の一歩。もうくじけそう。

```vega-lite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": "line",
  "encoding": {
    "x": {"field": "a", "type": "ordinal"},
    "y": {"field": "b", "type": "quantitative"}
  }
}
```
