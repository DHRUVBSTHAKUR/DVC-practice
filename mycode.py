import pandas as pd 
import os 

data = {'Name':['Dhruv','Thakur'],
        'Area':['SHIMLA','CHENNAI']}

df = pd.DataFrame(data)
data_dir='data'
os.makedirs(data_dir,exist_ok=True)
file_path = os.path.join(data_dir,'this.csv')
df.to_csv(file_path,index=False)
print(f"csv file saved to{file_path}")
