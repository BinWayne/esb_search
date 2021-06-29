import  pandas  as pd
import os

file = 'quanjingtu.xlsx'
fllePath = '/Users/wubin/workspace/python/tongshang/esb/excel'

listA=[]
listB=[]
count=0
def read_excel(excelDir,fileName):
    
    print("===============================")
    print(f'start to check file {excelDir} / {fileName}')
    df = pd.read_excel(excelDir+'/'+fileName,sheet_name='客户信息管理')
    name=''
    for row in df.itertuples():
       name = getattr(row, '交易码')
       if(fileName=='quanjingtu.xlsx'):
           listA.append(name)
       else:
           listB.append(name)
       
       #print(name) # 输出每一行
    #print(listA)
    #print(listB)
       
    #for index, row in df.iteritems():
    #    print(row[2]) # 输出列名
  
    return df.shape[0]
        #print(i)


def listFiles(filePath):
    count=0
    for i in os.listdir(fllePath):
        count+=read_excel(fllePath,i)
    #print(count)
    

if __name__ == '__main__':
	#read_excel(fllePath,file)
    #print(os.getcwd())
    listFiles(fllePath)
    print("全景图")
   # print(listA)#全景
    print(len(listA))
    print("================")
   # print("治理平台")
   # print(listB)
    print(len(listB))

    # 导出  服务治理平台的服务 不存在 全景图里的
    for item in listB:
        if item not in listA:
            print(item)
    print("================")
    for item in listA:
        if item not in listB:
            print(item)
    
            
    #print (list(set(listB).difference(set(listA)))) # listB中有而listA中没有的