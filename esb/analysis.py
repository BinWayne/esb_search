import  pandas  as pd
import os
from mysql import TestDBHelper
from mysql import DBHelper

file = 'quanjingtu.xlsx'
fllePath = '/Users/wubin/workspace/python/tongshang/esb_search/esb/excel'
sheets=['流程服务','内部渠道服务','合作方服务','客户信息管理','客户服务','存款','贷款',
'银行卡','支付结算','投资理财','中间业务','金融市场','投行','客户资产管理','风险管理','银行业务支持','企业管理支持','技术支持']

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


def read_excel(excelDir,fileName,sheetName):
    
    print("===============================")
    print(f'start to check file {excelDir} / {fileName}')
   
    df = pd.read_excel(excelDir+'/'+fileName,sheet_name=sheetName,dtype=str)
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
    #for i in items:
    db = DBHelper()
    sql="INSERT INTO esb.overview \
(big_category, sub_category, svc_code, svc_name, scene_code, scene_name, trade_code, trade_name, consumer, provider, status) \
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
    for i in items:
        
        params=(i.bigCategory,i.subCategory,i.svcCode,i.svcName,i.sceneCode,i.sceneName,
                i.tradeCode,i.tradeName,i.consumer,i.provider,i.status)
        print(params) 
        #db.insert(sql,*params)

        
    print('==============================')    


def listFiles(filePath):
    count=0
    for i in os.listdir(fllePath):
        count+=read_excel(fllePath,i)
    #print(count)
    

if __name__ == '__main__':
    for sheetName in sheets:
	    read_excel(fllePath,file,sheetName)
        
    #print(os.getcwd())
    # listFiles(fllePath)
    #print("全景图")
   
            
    #print (list(set(listB).difference(set(listA)))) # listB中有而listA中没有的