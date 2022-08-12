#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are a student and you are trying to organize your subjects and grades using Python.
# Use what you've learned about lists to organize your subjects and scores.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = [["physics"],
["calculus"],
["poetry"],
["history"]]
grades = [98,97,85,88]
gradebook=[["physics",98],['calculus',97],['poetry',85],['history',88]]
print(gradebook)
gradebook.append(['computer_science',100])
gradebook.append(['visual_arts',93])
gradebook[-1][-1] = 93+5
gradebook[-1].remove(98)
gradebook[-1].append('Pass')
print(gradebook)
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
