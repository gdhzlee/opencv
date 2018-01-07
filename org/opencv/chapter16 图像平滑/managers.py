import cv2
import numpy as np
import time

class CaptureManager(object):


    #_init_()方法是一种特殊的方法，及时构造函数。当时创建给类的时候就会调用该构造方法。
    def __init__(self, capture, previewWindowManager = None,
                 shouldMirrorPreview = False):
        # self 代表该类的实例，类似java中 this，而使用this来代替self完全没有问题
        # self.property_name 就可以为该类添加一个属性，用该类实例也可以同样的添加一个属性
        #且以 _ 符号开头的属性/方法为私有属性/方法
        """
            class Demo:
                def _init_(self,name):
                    #在初始化该类的时候，创建一个名为 _name的属性，并赋值。
                    self._name = name


            #实例化
            demo = Demo();
            #为该实例添加一个属性
            demo.age = 18;
            #删除该实例的属性
            del demo.age;
        """
        self.previewWindowManager = previewWindowManager;
        self.shouldMirrorPreview = shouldMirrorPreview;

        self._capture = capture;
        self._channel = 0;
        self._enteredFrame = False;

        self._frame = None;
        self._imageFilename = None;
        self._videoFilename = None;
        self._videoEncoding = None;
        self._videoWriter = None;

        self._startTime = None;
        #python3 整型是没有限制大小的，并且没有python2中的Long类型，因此整型可以当做Long类型来使用。
        self._framesElapsed = 0;
        self._fpsEstimate = None;

    # @property装饰器就是负责把一个方法变成属性调用，同时创建另外一个装饰器 @*.setter 负责把属性的setter方法变成属性赋值。
    @property
    def channel(self):
        return self._channel;

    @channel.setter
    def channel(self,value):
        if self._channel != value:
            self._channel = value;
            self._frame = None;

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve();
        return self._frame;

    @property
    def isWritingImage(self):
        return self._imageFIlename is not None;

    @property
    def isWritingVideo(self):
        return self._videoFilename is not None;


#