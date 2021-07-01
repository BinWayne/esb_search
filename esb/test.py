import pandas  as pd


file = 'quanjingtu.xlsx'
filePath = '/Users/king/PycharmProjects/esb_search/esb/excel'


class item:
    bigCategory = ''
    subCategory = ''
    svcCode = ''
    svcName = ''
    sceneCode = ''
    sceneName = ''
    tradeCode = ''
    tradeName = ''
    consumer = ''
    provider = ''
    status = ''

    def __init__(self, bigCategory, subCategory, svcCode, svcName, sceneCode, sceneName,
                 tradeCode, tradeName, consumer, provider, status):
        self.bigCategory = bigCategory  # 大类
        self.subCategory = subCategory  # 子类
        self.svcCode = svcCode  # 服务码
        self.svcName = svcName  # 服务名称
        self.sceneCode = sceneCode  # 场景码
        self.sceneName = sceneName  # 场景名称
        self.tradeCode = tradeCode  # 交易码
        self.tradeName = tradeName  # 交易名称
        self.consumer = consumer  # 消费方
        self.provider = provider  # 服务提供方
        self.status = status  # 状态

    def __str__(self):  # 定义打印对象时打印的字符串
        return str(self.__dict__)

def read_excle(path):
    data_xls = pd.ExcelFile(path)
    data = data_xls.sheet_names  #获取全部sheet名
    del data[0:3]
    data.remove('投行') #先手动删除空sheet

    items = []
    for name in data:
        df = pd.read_excel(path,sheet_name=name,dtype=str)
        df = df.fillna(method='ffill')
        # for indexs in df.index:
        #     print(df.loc[indexs].values[0:-1])
        for i in range(0, len(df)):
            tt = item(
            df.iloc[i]['大类'],
            df.iloc[i]['子类'],
            df.iloc[i]['服务码'],
            df.iloc[i]['服务名称'],
            df.iloc[i]['场景码'],
            df.iloc[i]['场景名称'],
            df.iloc[i]['交易码'],
            df.iloc[i]['交易名称'],
            df.iloc[i]['服务调用方'],
            df.iloc[i]['服务提供方'],
            df.iloc[i]['服务状态'])
            items.append(tt)
    return items

if __name__ == '__main__':
    # print(read_excle(filePath+'/'+file))
    tup = read_excle(filePath+'/'+file)
    for i in tup:
        print(i)