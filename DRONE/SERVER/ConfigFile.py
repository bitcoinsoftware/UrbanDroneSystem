__author__ = 'noname'
#TODO : Osobny videoport dla kazdej z kamer. Dzieki temu jedna osoba moze byc kierowca a druga np. celowniczym
config = {'serverType':'tank', 'videoAvailable':True, 'port':12341, 'audioAvailable':True,
          'microphoneAvailable':True, 'speakerAvailable':True,
'cameraParams':
[
    {'cameraIndex':0, 'videoPort':22345, 'taken':False, 'xAxisAvailable':True, 'yAxisAvailable':True, 'zAxisAvailable':False},
    {'cameraIndex':1, 'videoPort':32345, 'taken':False, 'xAxisAvailable':False,'yAxisAvailable':False,'zAxisAvailable':False}
],
'leftRoboticArmAvailable':False, 'leftRoboticFingersAvailable':False, 'rightRoboticArmAvailable':True,
'rightRoboticFingersAvailable':True, 'sensorList':{'temperature':30, 'methan':0.1}}