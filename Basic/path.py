"""
获取路径的方法
"""
import os, sys

print("__file__=%s" % __file__)
print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))
print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))
print("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])
print("os.path.abspath(__file__)=%s" % os.path.abspath(__file__))
print("os.getcwd()=%s" % os.getcwd())
print("sys.path[0]=%s" % sys.path[0])
print("sys.argv[0]=%s" % sys.argv[0])

