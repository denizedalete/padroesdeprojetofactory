#Usando padrão. Esse código simula um projeto de uma aplicação que rode em IOS e Android, por exemplo. Dessa maneira, a divisão de classes aplicando o método facilitaria mudanças posteriores que sejam específicas para um sistema ou outro.

##Definindo classe abstract factory

class ApplicationsFactory:
__metaclass__=ABC

def __init__(self):
super(ApplicationsFactory,self)

@abstractmethod
def getMusicPlayer(self):
pass

@abstractmethod
def getPhotoViewer(self):
pass

## Definindo classes concrete factory

class AppleApplicationsFactory(ApplicationsFactory):

def __init__(self):
super(AppleApplicationsFactory,self)

def getMusicPlayer(self):
return AppleMusicPlayer();

def getPhotoViewer(self):
return ApplePhotoViewer()

class AndroidApplicationsFactory(ApplicationsFactory):

def __init__(self):
super(AndroidApplicationsFactory,self)

def getMusicPlayer(self):
return AndroidMusicPlayer();

def getPhotoViewer(self):
return AndroidPhotoViewer()

def getPlatformFactory(plat):
## Definir qual plataforma será selecionada
factory_dict={
“Android”:AndroidApplicationsFactory(),
“Apple”:AppleApplicationsFactory()
}
return factory_dict[plat]

## Definindo a plataforma

platform=”Android”

app_factory=getPlatformFactory(platform)

music_player=app_factory.getMusicPlayer()

print(music_player.playMusic(“Cheap Thrills”))

#Qualquer mudança, por exemplo, em todas as aplicações apple, seriam efetuadas na classe “AppleApplicationsFactory”.
