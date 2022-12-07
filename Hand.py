import Servo as servo
import math
class Hand():
  def __init__(self,placa,polegar,indicador,medio,anelar, minino):
    self.polegar = polegar
    self.indicador = indicador
    self.medio= medio
    self.anelar = anelar
    self.minimo = minino
    self.placa = placa
    
    self.motorPolegar = servo.servo(polegar,placa)
    self.motorIndicador = servo.servo(indicador,placa)
    self.motorMedio = servo.servo(medio,placa)
    self.motorAnelar = servo.servo(anelar,placa)
    self.motorMinimo = servo.servo(minino,placa)
    
    self.motorPolegar.move(0)
    self.motorIndicador.move(0)
    self.motorMedio.move(0)
    self.motorAnelar.move(0)
    self.motorMinimo.move(0)
    
  def moveHand(self,pos1, pos2 , pos3, pos4, pos5):
    self.motorPolegar.move(pos1)
    self.motorIndicador.move(pos2)
    self.motorMedio.move(pos3)
    self.motorAnelar.move(pos4)
    self.motorMinimo.move(pos5)
    
  def move(self,lmList):
    pos1 = self.calcularDistancia(lmList,0,4)
    pos2 = self.calcularDistancia(lmList,0,8)
    pos3 = self.calcularDistancia(lmList,0,12)
    pos4 = self.calcularDistancia(lmList,0,16)
    pos5 = self.calcularDistancia(lmList,0,20)
    self.moveHand(pos1,pos2,pos3,pos4,pos5)
    
  def calcularDistancia(self,lmList,pontoA,pontoB):
        x1, y1 = lmList[pontoA][1], lmList[pontoA][2]
        x2, y2 = lmList[pontoB][1], lmList[pontoB][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        #colocando na tela 
        
      #  cv2.circle(img, (x1, y1),5, (255, 0, 255), cv2.FILLED)
       # cv2.circle(img, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
       # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
      #  cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)
 
        
        return(int((length/180)*100))
  