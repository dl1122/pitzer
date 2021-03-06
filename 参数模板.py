
jt={
    'na':1,
    'k':1,
    'cl':1,
    'so4':2,
    'co3':2,
    'br':1,
    'ca':2,
    'mg':2,
    'b4o7':2,
    'sr':2,
    'cs':1,
    'rb':1,
    'al':3,
    'nh4':1,
    'li':1,
    'b5o6(oh)4':1,
    'b5o8':1,
    'b(oh)4':1,
    'b4o5(oh)4':2,
    }
cation=['','li', 'nh4','na','mg','al','k','ca','rb','sr','cs','ba']
anion=['','b4o7', 'b5o6(oh)4','b5o8','b(oh)4','b4o5(oh)4','co3','so4','cl','br','no3','so3']
Ay_25=0.3915
pitzer11_25 = {#分别为：B0,B1,C,B2
        'nacl':[0.0765,0.2664,0.00127],
        'kcl':[0.04835,0.2122,-0.00084],
        'naco3':[0.0399,1.389,0.0044],
        'naso4':[0.01958,1.113,0.00497],
        'liso4':[0.14396,1.17736,-0.00571],
        'kco3':[0.1488,1.43,-0.0015],
        'kso4':[0.07548,0.44371,0],
        'mgcl':[0.3511,1.6512,0.0065],
        'mgso4':[0.221,3.343,0.025,-37.23],
        
            }
OZYL_25={#电解质pitzer参数O,顺序交换输入两次#CC',
    'nak':[-0.012],'kna':[-0.012],
    'clco3':[-0.02],'co3cl':[-0.02],
    'clso4':[0.03],'so4cl':[0.03],
    'nasr':[-0.2276],'srna':[-0.2276],
    'ksr':[0.0149],'srk':[0.0149],
    'co3so4':[0.02],'so4co3':[0.02],
    'namg':[0.07],'mgna':[0.07],
    'mgsr':[-0.1965],'srmg':[-0.1965],
    
         }
OZYLCYy_25={#电解质pitzer参数U,顺序交换输入六次,
        'nakcl':-0.0018, 'knacl':-0.0018,'naclk':-0.0018, 'kclna':-0.0018, 'clnak':-0.0018, 'clkna':-0.0018,
        'nakso4':-0.01,'knaso4':-0.01,'naso4k':-0.01,'kso4na':-0.01,'so4nak':-0.01,'so4kna':-0.01,
        'nakco3':0.003,'knaco3':0.003,'naco3k':0.003,'kco3na':0.003,'co3nak':0.003,'co3kna':0.003,
        'clso4na':0.0014,'clnaso4':0.0014,'so4nacl':0.0014,'so4clna':0.0014,'naclso4':0.0014,'naso4cl':0.0014,
        'clso4k':-0.005,'clkso4':-0.005,'so4kcl':-0.005,'so4clk':-0.005,'kclso4':-0.005,'kso4cl':-0.005,
        'clco3na':0.0085,'clnaco3':0.0085,'co3nacl':0.0085,'co3clna':0.0085,'naclco3':0.0085,'naco3cl':0.0085,
        'clco3k':0.004,'clkco3':0.004,'co3kcl':0.004,'co3clk':0.004,'kclco3':0.004,'kco3cl':0.004,
        'co3so4na':-0.005,'co3naso4':-0.005,'so4naco3':-0.005,'so4co3na':-0.005,'naco3so4':-0.005,'naso4co3':-0.005,
        'co3so4k':-0.009,'co3kso4':-0.009,'so4kco3':-0.009,'so4co3k':-0.009,'kco3so4':-0.009,'kso4co3':-0.009,
        'namgcl':-0.012, 'naclmg':-0.012, 'mgclna':-0.012, 'mgnacl':-0.012, 'clnamg':-0.012, 'clmgna':-0.012,
        'namgso4':-0.015,'naso4mg':-0.015,'mgso4na':-0.015,'mgnaso4':-0.015,'so4namg':-0.015,'so4mgna':-0.015,
        
           }
phcs_25={#平衡常数，数字格式，水为：_n
    'nacl':39.7417,
    'kcl':7.94,
    'naso4':0.5158,
    'kso4':0.0166799,
    'srcl_6':75.944286569,
    'srcl_2':4722.057997,
    'nh4cl':17.46,
    'cacl_6':17171.39,
    'naso4mgso4_4':0.0044985507,
    'csso4mgso4_6':0.000062271971,
    'csso4':7.0851426,
    'liso4_1':2.787653,
    'liso4naso4_12':0.00036919,
    
      }


