# -*- coding: utf-8 -*-
import sys
sys.path.append('./')
from classes import SampleSub01, SampleSub02


if __name__ == '__main__':
  sub01 = SampleSub01("hoge")
  sub02 = SampleSub02("piyo")

  sub01.print_value()
  sub02.print_value()
