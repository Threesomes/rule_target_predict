### 功能
    短文本二级分类规则
### 使用
```
main()

Input: text (string) 
Output: target (string)
        target 为None时，说明未成功分类
```

#### 成功率及召回率
```
# 积分
all_num:179
corr_num:178
accuracy:0.99
all_num:208
corr_num:178
recall:0.86

# 短信
all_num:204
corr_num:196
accuracy:0.96
all_num:310
corr_num:196
recall:0.63

# 流量
all_num:4273
corr_num:4110
accuracy:0.96
all_num:4539
corr_num:4110
recall:0.91

# 余额
all_num:1050
corr_num:1008
accuracy:0.96
all_num:1474
corr_num:1008
recall:0.68

# 宽带
all_num:426
corr_num:400
accuracy:0.94
all_num:402
corr_num:400
recall:1.00

# 账单
all_num:130
corr_num:123
accuracy:0.95
all_num:314
corr_num:123
recall:0.39

# 月初扣费
all_num:40
corr_num:40
accuracy:1.00
all_num:47
corr_num:40
recall:0.85

# 本机业务
all_num:247
corr_num:224
accuracy:0.91
all_num:386
corr_num:224
recall:0.58
```
