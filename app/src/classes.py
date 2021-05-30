# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class SampleSuper(metaclass=ABCMeta):
  def __init__(self, value):
    self.value = value

  def set_value(self, value):
    self.value = value
  
  def get_value(self):
    return self.value
  
  @abstractmethod
  def print_value(self):
    """ 何らかの文字列と一緒にvalueを出力する。 """
    pass

class SampleSub01(SampleSuper):
  def __init__(self, value):
    super().__init__(value)

  def print_value(self):
    print("Sub01.value: {}".format(self.get_value()))

class SampleSub02(SampleSuper):
  def __init__(self, value):
    super().__init__(value)

  def print_value(self):
    print("Sub02.value: {}".format(self.get_value()))
