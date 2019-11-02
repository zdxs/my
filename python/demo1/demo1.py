#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('hello,world');
print('多个字符','逗号','隔开');
print(1+1);
print('11+0=',1+1);
print('=====================================>用户输入start');
name = input();
print('输入的内容：',name);

name2 = input('提示输入:');
print('输入的内容2：',name2);
print('=====================================>用户输入end');


print('==========》数据类型和变量start');
print('斜杠\转义字符:','I\'m ok ');
print(" '''...''' 多行" );
print('''line1
... line2
... line3''')

print(r'''hello,\n
world''')

print('布尔值');
age = int(input('请输入年龄[强制转换]：'));
if age >= 10:
	print('你输入',age,'大于等于10');
else:
	print('你输入',age);
print('----------------------------------------');
print('ord()函数获取字符的整数表示，chr()');
print(ord('A'));
print(ord('中'));
print(chr(66));
print(chr(20013));
print('----------------------------------------');


print('占位符');
print('%2d-%02d' % (3, 1))
print('%d hello world' %(123));
print('%.2f' % 3.1415926)


print('==========》数据类型和变量end');