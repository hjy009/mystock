import pytest
import base


class test_base():
    i = None
    def setup_method(self, method):
        self.i = base.base()
        return
    def teardown_method(self, method):
        return

    def test_lxcgdd(self):
        self.i.menu('流程管理','交易类型管理')
        self.i.mtree('采购管理','采购订单')
        self.i.driver.close()
        return

    def test_xzcgdd(self):
        self.i.menu('采购管理', '采购订单新增')
        self.i.minput('采购组织', '宁波新华昌运输设备有限公司')
        # self.i.minputpop('采购组织','新华昌集团有限公司')
        # self.i.minputpopi('采购组织',3)
        self.i.minput('订单类型', '钢材采购')
        self.i.minputdt('订单日期', '2022-01-04')
        self.i.minputpop('供应商', '宏晟物流装备有限公司')
        self.i.minput('采购部门', '采购部')
        # self.i.dinput(1,'物料编码','0501010001')
        self.i.dinputpop(1, '物料编码', '0501010001')
        self.i.dinput(1, '数量', 100)
        self.i.dinput(1, '含税单价', 1000)
        self.i.dinputpop(2, '物料编码', '0501010002')
        self.i.dinput(2, '数量', 101)
        self.i.dinput(2, '含税单价', 1001)

        return