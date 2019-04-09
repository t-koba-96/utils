import numpy as np
import pandas as pd
import os

def make_csv(PATH):
    df=pd.read_csv((os.path.join(PATH+"pose.csv")),header=None)
    r_x_r=[]
    r_y_r=[]
    l_x_r=[]
    l_y_r=[]
    r_x_e=[]
    r_y_e=[]
    l_x_e=[]
    l_y_e=[]

    for i,(a,b,c,d) in enumerate(zip(df.iloc[:,8],df.iloc[:,9],df.iloc[:,14],df.iloc[:,15])):
      if i<=(len(df)-2401):
        if a==0:
          r_x_r.append(e)
        else:
          r_x_r.append(a)
          e=a
        if b==0:
          r_y_r.append(f)    
        else:
          r_y_r.append(b)
          f=b
        if c==0:
          l_x_r.append(g)    
        else:
          l_x_r.append(c)
          g=c
        if d==0:
          l_y_r.append(h)   
        else:
          l_y_r.append(d)
          h=d

      else:
        if a==0:
          r_x_e.append(e)
        else:
          r_x_e.append(a)
          e=a
        if b==0:
          r_y_e.append(f)    
        else:
          r_y_e.append(b)
          f=b
        if c==0:
          l_x_e.append(g)    
        else:
          l_x_e.append(c)
          g=c
        if d==0:
          l_y_e.append(h)   
        else:
          l_y_e.append(d)
          h=d

    save_df = pd.DataFrame({
                    'r_x_r' : r_x_r,
                    'r_y_r' : r_y_r,
                    'l_x_r' : l_x_r,
                    'l_y_r' : l_y_r
                    
          })
    save_df.to_csv(os.path.join(PATH+"train.csv"),index=None)

    save_df = pd.DataFrame({
                    'r_x_e' : r_x_e,
                    'r_y_e' : r_y_e,
                    'l_x_e' : l_x_e,
                    'l_y_e' : l_y_e
                    
          })
    save_df.to_csv(os.path.join(PATH+"test.csv"),index=None)



PATH="../local/dataset/work_detect/mogi_data/worker_a/pose_a/"
make_csv(PATH)