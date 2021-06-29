import  pandas  as pd
import os

file = 'quanjingtu.xlsx'
fllePath = '/Users/wubin/workspace/python/tongshang/esb/excel'


class item:
    bigCategory=''
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

    def __init__(self,bigCategory,subCategory,svcCode,svcName,sceneCode,sceneName,
    tradeCode,tradeName,consumer,provider,status):
        self.bigCategory = bigCategory#大类
        self.subCategory = subCategory#子类
        self.svcCode = svcCode #服务码
        self.svcName = svcName #服务名称
        self.sceneCode = sceneCode #场景码
        self.sceneName = sceneName #场景名称
        self.tradeCode = tradeCode #交易码
        self.tradeName = tradeName  #交易名称
        self.consumer = consumer    #消费方
        self.provider = provider    #服务提供方
        self.status = status    #状态
    def __str__(self):  # 定义打印对象时打印的字符串
        return str(self.__dict__)
        # return " ".join(str(strObj) for strObj in (
        #    self.bigCategory,
        # self.subCategory,
        # self.svcCode ,
        # self.svcName ,
        # self.sceneCode,
        # self.sceneName,
        # self.tradeCode ,
        # self.tradeName ,
        # self.consumer,
        # self.provider,
        # self.status))
        

def read_excel(excelDir,fileName):
    
    print("===============================")
    sheet = ['流程服务','内部渠道服务','合作方服务']
    print(f'start to check file {excelDir} / {fileName}')
    df = pd.read_excel(excelDir+'/'+fileName,sheet_name='客户信息管理',dtype=str)
    df = df.fillna(method='ffill')

    # for rowIndex,row in df.iterrows():
    #     print(row)
    items = []
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
        

    for i in items:
        print(i)   
   


def listFiles(filePath):
    count=0
    for i in os.listdir(fllePath):
        count+=read_excel(fllePath,i)
    #print(count)
    

if __name__ == '__main__':
	read_excel(fllePath,file)
    #print(os.getcwd())
    # listFiles(fllePath)
    #print("全景图")
   
            
    #print (list(set(listB).difference(set(listA)))) # listB中有而listA中没有的