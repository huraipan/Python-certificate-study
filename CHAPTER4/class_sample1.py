# -*- coding: utf-8 -*-
"""class_sample1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13Z4gjYixKyftH1J2oJ50By-gMsSVmDvO
"""

class User:
    user_type = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def increment_age(self):
        """年齢を１つ増やす"""
        self.age += 1

    def start_name(self):
        """nameの1文字を取得する"""
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ""