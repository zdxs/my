#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates);
print(classmates[1]);
print('长度len():',len(classmates));
print('append追加---------------------->')
append = input('请输入追加元素:');
classmates.append(append);
print(classmates);
print('insert插入到指定位置---------------------->')
_insertXu = int(input('请输入追加元位置:'));
_insertVal = input('请输入插入内容:');
classmates.insert(_insertXu,_insertVal);
print(classmates);