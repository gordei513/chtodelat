#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# загрузка библиотек
import math
import numpy
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже
# проверка для гита

if __name__=='__main__':
# начальная точка, интервал
    arguments = numpy.r_[0:200:0.1]
    mpp.plot(
        arguments,
# один sin задает амлитуду, а второй уже сами ,,волны,, (периуд совподает), получается такой рисунок
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
    mpp.show()
