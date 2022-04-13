import gc
from ncc import base
from datasets import cachedy,ccdy
from datasets import index_basic,cacheidx
import time
import numpy as np
import pandas as pd

i=base.base()
#i.menu('流程管理','交易类型管理')
#i.mtree('采购管理','采购订单')
#i.driver.close()
i.menu('采购管理','采购订单新增')
i.minput('采购组织', '宁波新华昌运输设备有限公司')
#i.minputpop('采购组织','新华昌集团有限公司')
#i.minputpopi('采购组织',3)
i.minput('订单类型', '钢材采购')
i.minputdt('订单日期', '2022-01-04')
i.minputpop('供应商', '宏晟物流装备有限公司')
i.minput('采购部门', '采购部')
#i.dinput(1,'物料编码','0501010001')
i.dinputpop(1,'物料编码','0501010001')
i.dinput(1,'数量',100)
i.dinput(1,'含税单价',1000)
i.dinputpop(2,'物料编码','0501010002')
i.dinput(2,'数量',101)
i.dinput(2,'含税单价',1001)


