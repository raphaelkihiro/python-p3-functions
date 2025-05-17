#!/usr/bin/env python3

def greet_programmer():
    return "Hello, programmer!"

def greet(name):
    return f"Hello, {name}!"

def greet_with_default(name="programmer"):
    return f"Hello, {name}!"

def add(num1=8, num2=4):
    return num1 + num2

def halve(number=16):
    return number / 2
