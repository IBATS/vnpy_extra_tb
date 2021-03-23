"""
@author  : MG
@Time    : 2021/3/11 6:57
@File    : utils.py
@contact : mmmaaaggg@163.com
@desc    : 用于
"""
from vnpy.trader.constant import Interval
from vnpy_extra.utils.enhancement import CtaSignal, ArrayManager
import talib


class TBArrayManager(ArrayManager):
    def ma(self, *args, matype=0, array: bool = False):
        """
        ta.MA(close,timeperiod=30,matype=0)
        移动平均线系列指标包括：SMA简单移动平均线、EMA指数移动平均线、WMA加权移动平均线、DEMA双移动平均线、TEMA三重指数移动平均线、TRIMA三角移动平均线、KAMA考夫曼自适应移动平均线、MAMA为MESA自适应移动平均线、T3三重指数移动平均线。
        其中，close为收盘价，时间序列，timeperiod为时间短，默认30天，
        :param args:
        :param matype: matype 分别对应：0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, 5=TRIMA, 6=KAMA, 7=MAMA, 8=T3 (Default=SMA)
        :param array: 是否返回数组
        :return:
        """
        rets = [talib.MA(self.close, win, matype) for win in args]

        if array:
            return tuple(rets)
        return tuple([_[-1] for _ in rets])


class TBCtaSignal(CtaSignal):
    def __init__(self, array_size: int, **kwargs):
        super().__init__(array_size=array_size, **kwargs)
        self.am = TBArrayManager(size=array_size)
        # 对应 TB 中用于记录上一次进场到现在的数量
        self.bars_since_entry = 0
        # 对应 TB 中用于记录上一次出场到现在的数量
        self.bars_since_exit = 0

    def set_signal_pos(self, pos):
        if self.signal_pos != 0 and pos == 0:
            self.bars_since_exit = self.win_bar_count
        elif self.signal_pos == 0 and pos != 0:
            self.bars_since_entry = self.win_bar_count
        super().set_signal_pos(pos)


if __name__ == "__main__":
    pass
