#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
魔法门6自动化脚本。
"""

from macro.bot import bot

#--- 以下两个方法用户魔法门6角色修改器 ---
def learn_all_skill(level=60, master_level=0):
    """在技能编辑界面学会所有的技能。运行脚本前, 将鼠标放在第一个技能的技能等级
    的数字上, 并选中所有文本。然后运行此脚本, 并在1秒内切回到修改器界面。
    
    :param level: 技能等级
    :param master_level: 专精等级, 0是普通, 1是专家, 2是大师
    """
    level = str(level)
    bot.delay(1.0)
    for i in range(31): # 一共31个技能
        bot.type_string(level)
        bot.tab()
        bot.up(n=2)
        bot.down(n=master_level)
        bot.tab()

# learn_all_skill(level=1, master_level=0)

def learn_all_magic():
    """在魔法全书界面学会所有的技能。运行脚本前, 用鼠标选中第一个魔法, 设置为
    未习得。
    """
    bot.delay(1.0)
    for i in range(9 * 11): # 一共99个技能
        bot.space()
        bot.tab()
        
# learn_all_magic()