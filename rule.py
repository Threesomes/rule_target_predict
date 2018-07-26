import linecache
import re
import win_unicode_console
win_unicode_console.enable()

# 积分
def jifen(text):
    target = None
    if '积分' in text:
        pattern = '查查|有多少|剩余|查一下|多少|查询|有没有|有积分|查|有多些'
        if re.search(pattern, text):
            target = '积分'
        if '话费' in text:
                target = None
    else:
        target = None
    return target
# 短信
def duanxin(text):
    target = None
    if '短信' in text:
        pattern_1 = '查询|查一下|有多少|有多些|短信优惠|免费短信|短信接收|还剩多少|剩余|剩下|免费|有没有|剩多少'
        if len(text) < 5:
            target = '短信'
        if re.search(pattern_1, text):
            target = '短信'
        pattern_2 = '服务密码|账单|话费'
        if re.search(pattern_2, text):  
            target = None
    elif '信息' in text or '彩信' in text:
        pattern_3 = '有多少条|剩余|接收信息|免费|剩多少'
        if re.search(pattern_3, text):
            target = '短信'
    else:
        target = None
    if target == '短信':
        if '流量' in text or '谢谢' in text:
            target = None
        elif '话费' in text:
            target = None
        else:
            target = '短信'
    return target
# 流量
def liuliang(text):
    target = None
    pattern_1 = '查查|多少|有多少|剩余|查一下|查询|查|有多些'
    pattern_2 = '办理|办|买|购买|订购|开通|开|开一个|取消|退订|订|介绍'
    pattern_3 = '流量业务|上网套餐|流量套餐|流量'
    pattern_4 = '[一二两三四五六七八九十]+(元|块钱)|[一二两三四五六七八九百]+(元|块钱)'
    pattern_5 = '优惠流量|国内流量|流量套餐|叠加包|流量包|加油包|加油套餐|基础包|基础流量|小时流量|小时包|周末包|日流量|日套餐|夜间包|夜间流量|闲时流量|[一二两三四五六七八九十]+[百]*(元|块钱)[包]*[一二两三四五六七八九十]+[百]*[个]*(g|兆)'
    pattern_6 = '[一二两三四五六七八九十]+[百]*(g|兆)'
    if '流量' in text and re.search(pattern_1, text) and (not '话费' in text): # 查询流量
        target = '流量'
    elif (re.search(pattern_2, text) or re.search(pattern_4,text)) and re.search(pattern_3,text): # 开通和取消流量
        target = '流量' 
    elif re.search(pattern_5,text):
        target = '流量'
    elif ('流量' in text or re.search(pattern_6,text)) and (len(text)<7 or (re.search(pattern_2, text) and re.search(pattern_4,text))):
        target = '流量'
    return target
# 余额
def yue(text):
    target = None
    if '余额' in text:
        pattern_1 = '查查|多少|有多少|剩余|查一下|查询|查|有多些'
        if '流量余额' in text:
            target = None
        elif re.search(pattern_1, text):
            target = '余额'
    elif '话费' in text or '欠费' in text or '还有多少钱' in text :
        pattern_2 = '查查|有多少|剩余|剩多少|查一下|查询|查|有多些|是多少|余额'
        pattern_3 = '话费清单|话费详单|消费|交话费|充话费|话费单|充值情况|使用情况|扣[话]*[费]*|到没到|进没进来|到了没有'
        if re.search(pattern_2, text) and (not re.search(pattern_3, text)) and zhangdan(text) == None:
            target = '余额'
    else:
        target = None
    if '流量' in text:
        target = None
    return target
# 宽带
def kuandai(text):
    target = None
    if '宽带' in text:
        target = '宽带'
        pattern = '故障|修理|报修|断|无法|出问题|坏|不能使用|不能用|不能上网|没有网|没有信号|连不上|不好使|连接不上|上不了|不能看|看不了|网速'
        if re.search(pattern,text):
            target = '集外业务咨询'
    return target
# 账单
def zhangdan(text):
    target = None
    pattern = '账单查询|查下账|本月消费|花了[多少]*[啥]*钱|怎么消费|交易明细|花哪了'
    pattern_1 = '账单|话费清单|话费单|话费使用情况|什么费用|扣费|手机费用|消费情况'
    pattern_2 = '查询|查一下|查查|看看|查|查一查|看一下'
    pattern_3 = '这个月|这月|本月|每月|月份|每个月|上个月|上月'
    pattern_4 = '话费|费用|消费|扣[了]*[什么]*[啥]*费[用]*'
    pattern_5 = '扣'
    pattern_6 = '什么费[用]*|钱是什么|啥钱|多少钱'
    if re.search(pattern, text):
        target = '账单'
    elif re.search(pattern_1,text) and re.search(pattern_2, text):
        target = '账单'
    # elif re.search(pattern_3,text) and re.search(pattern_4,text):
    #     if yue(text) == None:
    #         target = '账单'
    elif re.search(pattern_5, text) and re.search(pattern_6, text):
        target = '账单'
    elif '账单' in text and len(text)<10:
        target = '账单'
    else:
        target = None
    if yuechukoufei(text) != None:
        target = None
    return target
# 月初扣费
def yuechukoufei(text):
    target = None
    pattern = '月租是多少|月租费是多少|月租多少|最低消费是多少|月租到底是多少|座机费'
    pattern_1 = '月初|这个月刚刚开始'
    pattern_2 = '扣款|扣费|扣钱|扣了|扣的|少了这么多钱'
    if(re.search(pattern_1, text) and re.search(pattern_2,text)): # re.search(pattern, text) or 
        target = '月初扣费'
    elif re.search(pattern, text) or ('月租' in text and len(text)<10):
        target = '月初扣费'
    elif '查询' in text and ('月租' in text or '用了多少钱' in text):
        target = '月初扣费'
    else:
        target = None
    return target
# 本机业务
def benjiyewu(text):
    target = None
    pattern_1 = '什么业务|哪些业务|已定业务|开[啥|什么|通的]*业务|开通什么'
    pattern_2 = '我[的|这张]*卡|这卡|本机|我手机|这个手机|我现在'
    pattern_3 = '业务|开通|有(啥|什么)(业务|功能|套餐)|开(啥|什么)了'

    if re.search(pattern_1,text) or (re.search(pattern_2,text) and re.search(pattern_3,text)):
        target = '本机业务'
        if '增值业务' in text:
            target = '增值业务费'
        if '上网' in text:
            target = 'GPRS'
        if liuliang(text) != None:
            target = liuliang(text)
    return target


def main(text):
    '''
    输入为text，string
    输出为target，string
    '''
    fun_list = [jifen,duanxin,liuliang,yue,zhangdan,yuechukoufei,kuandai,benjiyewu]
    for function in fun_list:
        target = function(text)
        if target != None:
            return target
    return target



def txt_test():
    path = 'result_2/data/积分.txt'
    # test
    all_num = 0 #txt中所有句子总数
    corr_num = 0 #分类正确的句子数
    for i in range(1, 404):
        if i%2 == 1:
            # print(linecache.getline(path, i))
            text = linecache.getline(path, i).split(',')[1].strip()
            all_num += 1
            # print(text)
            target = jifen(text)
            if target == '积分':
                corr_num += 1
                print(text)
    print('all_num:'+str(all_num))
    print('corr_num:'+str(corr_num))
    print('accuracy:'+str('%.2f' % (corr_num/all_num)))

def recall_test(test_target='积分', test_fun=jifen, mode=1):
    if mode == 1:
        path = 'train_result/train.txt'
        txt_len = 16016
        # path = 'c:/Users/Alice/Desktop/中移动/result_analysis/result_2/data/账单.txt'
        # txt_len = 69
    elif mode == 2:
        path = 'result_2/test1.txt'
        txt_len = 4005
    else:
        print('======模式选择错误======')
    all_num = 0 # 所有句子中被分类为test_target的句子数
    corr_num = 0 # 被分类为test_target的句子中的分类正确的个数
    for i in range(1, txt_len):  # 4005 16016
        target_true = linecache.getline(path, i).split(',')[0].strip()
        text = linecache.getline(path, i).split(',')[1].strip()
        target = test_fun(text)
        if target_true == test_target:
            all_num += 1
            if target == test_target:
                corr_num += 1
            # else:
            #     print(linecache.getline(path, i).strip())
    if all_num != 0 :
        print('all_num:'+str(all_num))
        print('corr_num:'+str(corr_num))
        print('recall:'+str('%.2f' % (corr_num/all_num)))
    else:
        print('分类总数为0')


def accuracy_test(test_target='积分', test_fun=jifen, mode = 1):
    if mode == 1:
        path = 'train_result/train.txt'
        txt_len = 16016
        # path = 'c:/Users/Alice/Desktop/中移动/result_analysis/result_2/data/账单.txt'
        # txt_len = 69
    elif mode == 2:
        path = 'result_2/test1.txt'
        txt_len = 4005
    else:
        print('======模式选择错误======')
    all_num = 0 # 所有句子中被分类为test_target的句子数
    corr_num = 0 # 被分类为test_target的句子中的分类正确的个数
    for i in range(1, txt_len):  # 4005 16016
        target_true = linecache.getline(path, i).split(',')[0].strip()
        text = linecache.getline(path, i).split(',')[1].strip()
        target = test_fun(text)
        if target == test_target:
            all_num += 1
            if target_true == test_target:
                corr_num += 1
            # else:
            #     print(linecache.getline(path, i).strip())
    if all_num != 0 :
        print('all_num:'+str(all_num))
        print('corr_num:'+str(corr_num))
        print('accuracy:'+str('%.2f' % (corr_num/all_num)))
    else:
        print('分类总数为0')

def accuracy(mode = 1):
    if mode == 1:
        path = 'train_result/train.txt'
        txt_len = 16016
        # path = 'c:/Users/Alice/Desktop/中移动/result_analysis/result_2/data/账单.txt'
        # txt_len = 69
    elif mode == 2:
        path = 'result_2/test1.txt'
        txt_len = 4005
    else:
        print('======模式选择错误======')
    all_num = 0 # 所有句子数
    corr_num = 0 # 分类正确的个数
    corr_dict = {}
    all_dict = {}
    for i in range(1, txt_len):  # 4005 16016
        target_true = linecache.getline(path, i).split(',')[0].strip()
        text = linecache.getline(path, i).split(',')[1].strip()
        target = main(text)
        all_num += 1
        if target_true in all_dict.keys():
            all_dict[target_true] += 1
        else:
            all_dict[target_true] = 0
        if target_true == target:
            corr_num += 1
            if target in corr_dict.keys():
                corr_dict[target] += 1
            else:
                corr_dict[target] = 0
        else:
            print(linecache.getline(path, i).strip())
    if all_num != 0 :
        print('all_num:'+str(all_num))
        print('corr_num:'+str(corr_num)) 
        print('accuracy:'+str('%.2f' % (corr_num/all_num)))
    else:
        print('分类总数为0')
    for i in corr_dict.keys():
        print(i+'\t'+str(corr_dict[i])+'\t'+str(all_dict[i])+'\t'+('%.2f' % (corr_dict[i]/all_dict[i])))

# accuracy()


# txt_test()
# accuracy_test(test_target='本机业务', test_fun=benjiyewu, mode=1)
# recall_test(test_target='本机业务', test_fun=benjiyewu, mode=1)
# text= '三百元包五百兆'
# pattern = '夜间流量|[一二三四五六七八九十]+[百]*元[包]*[一二三四五六七八九十]+[百]*[个]*(g|兆)'
# if re.search(pattern, text):
#     print('ok')

