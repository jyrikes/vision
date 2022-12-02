import Servo as servo
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
    
  