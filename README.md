## 测试如下

- 使用curl

```
curl -X POST "http://127.0.0.1:5000/api/group" \
-H "Content-Type: application/json" \
-d '{
  "main_zd": "Z51.103",
  "other_zd": "",
  "main_ss": "99.2503",
  "other_ss": "",
  "gender": "2",
  "dept": "0302",
  "inHospitalTime": 14,
  "leavingType": "1",
  "age": 10,
  "age_days": 21,
  "weight": 3200
}'
```

- 对应关系为
```
  "main_zd": "Z51.103", #主要诊断
  "other_zd": "", #其他诊断
  "main_ss": "99.2503", #主要手术
  "other_ss": "", #其他手术
  "gender": "2", #性别1为男，2为女
  "dept": "0302", #部门（无关）
  "inHospitalTime": 14, #住院天数
  "leavingType": "1", #离开院方式
  "age": 10, #年龄
  "age_days": 21, #新生儿出生天数
  "weight": 3200 #体重
```

## 增加docker运行

```
docker compose up -d
```
