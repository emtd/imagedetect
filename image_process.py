# coding=utf-8
import opencv_util as ou
import numpy as np
import time
from appium.webdriver.common.touch_action import TouchAction

rate = 0.5
def region(x, y, width, height):#像素点区域
    return ou.region(x, y, width, height)
    
def regionP(driver,x, y, width, height):#百分比区域
    sWidth=driver.get_window_size()['width'];
    sHeight=driver.get_window_size()['height'];
    return ou.region(x*sWidth, y*sHeight, width*sWidth, height*sHeight)

def tap_element_by_image(driver, img,reference ,region=None):
    tapPoint=_get_element_middle_point(driver, img, region)
    status = tapPoint[2]
    if(tapPoint[0] is not None and tapPoint[1] is not None):
        target = 1-float(abs(reference[0]-tapPoint[0]))/float(reference[0])
        base = 1-float(abs(reference[1]-tapPoint[1]))/float(reference[1])
        if(target >= rate and base >= rate):
            TouchAction(driver).press(x=int(tapPoint[0]),y=int(tapPoint[1])).release().perform()
            return True
        else:
            return False
        return True;
    else:
        return False;

def is_element_present_by_image(driver, img,reference ,region=None):
    tapPoint=_get_element_middle_point(driver, img, region)
    status = tapPoint[2]
#np.sum(status), len(status))
    if(tapPoint[0] is not None and tapPoint[1] is not None):
        target = 1-float(abs(reference[0]-np.sum(status)))/float(reference[0])
        base = 1-float(abs(reference[1]-len(status)))/float(reference[1])
        if(target >= rate and base >= rate):
            return True
        else:
            return False
#        return True
    else:
        return False

def get_feature_number_by_image(img1,img2, region=None):
    findElementObj=ou.FindObj(img1, img2, region)
    return (findElementObj.findFeatureNumByBrisk())

def _get_element_middle_point(driver, img, region):
    #screenShotFileName=str(time.time())+'.png'
    #screen picture of shot must be .png
    i=img.find('.')
    j=img.rfind('/')
    if(j>=0):#picture path is not null
        screenShotFileName=img[0:j+1]+str(time.time())+'-'+img[j+1:i]+'.png'
    else:#picture path is null
        screenShotFileName=str(time.time())+'-'+img[0:i]+'.png'
    driver.get_screenshot_as_file(screenShotFileName)
    findElementObj=ou.FindObj(img, screenShotFileName, region)
    tapPoint=findElementObj.findMiddlePointByBrisk()
    return tapPoint

