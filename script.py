#importo librerias necesiarias para la automatizacion de la calculadora de windows
#instalo  Appium, urllib y selenium para la automatizacion de la calculadora de windows
from appium import webdriver
import time

#configuro las capacidades para la automatizacion de la calculadora de windows
caps = {
    "platformName": "Windows",
    "deviceName": "Maick.D",
    "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
}

#inicializo el driver para la automatizacion de la calculadora de windows
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

#muestro un mensaje indicando que la calculadora se ha abierto correctamente
print("Calculadora abierta correctamente")

#doy tiempo para que la calculadora se abra correctamente
time.sleep(2)

#########2. Verificar que la calculadora inicia en modo "Estándar".
#busco por nombre de la calculadora 

try:
    calculadoraEs = driver.find_element_by_accessibility_id("CalculatorResults")
    print("La calculadora inicia en modo 'Estándar'")
except:
    print("Error: No se pudo encontrar el elemento de resultados")

#--------------------------------------------------------------------------
########3. Realizar la operación 9 + 3 y verificar que el resultado es 12.
driver.find_element_by_accessibility_id("num9Button").click()
driver.find_element_by_accessibility_id("plusButton").click()
driver.find_element_by_accessibility_id("num3Button").click()
driver.find_element_by_accessibility_id("equalButton").click()

#valida el resultado de la operacion 9 + 3
resultado = driver.find_element_by_accessibility_id("CalculatorResults").text

assert "12" in resultado, f"Resultado incorrecto: {resultado}"
    
time.sleep(2)


####5. limpio operacion realizada
driver.find_element_by_accessibility_id("clearButton").click()

#---------------------------------------------------------------------
##### 6. Provocar un error: Realizar 5 / 0 =
driver.find_element_by_accessibility_id("num5Button").click()
driver.find_element_by_accessibility_id("divideButton").click()
driver.find_element_by_accessibility_id("num0Button").click()
driver.find_element_by_accessibility_id("equalButton").click()

#---------------------------------------------------------------------
#### 7. Validar que el display muestra el mensaje de error (ej. "Cannot divide by zero").
error = driver.find_element_by_accessibility_id("CalculatorResults").text
error_text = error.lower()

assert (
    "cannot divide by zero" in error_text or 
    "dividir entre cero" in error_text
), f"Error inesperado: {error}"
driver.find_element_by_accessibility_id("clearButton").click()
time.sleep(2)
#---------------------------------------------------------------------
### 8. Provocar nuevo error: Realizar 6 / 0 =
driver.find_element_by_accessibility_id("num6Button").click()
driver.find_element_by_accessibility_id("divideButton").click()
driver.find_element_by_accessibility_id("num0Button").click()
driver.find_element_by_accessibility_id("equalButton").click()

resultado2 = driver.find_element_by_accessibility_id("CalculatorResults").text
print("Resultado 2:", resultado2)
driver.find_element_by_accessibility_id("clearButton").click()
time.sleep(2)
#guardo captura de pantalla de la prueba realizada
driver.save_screenshot("evidencia.png")

if "0" in resultado2:
    print("Test pasa (según requerimiento dados)")
else:
    print("BUG DETECTADO")
    
    # Guardar evidencia
    driver.save_screenshot("bug.png")


#---------------------------------------------------------------------
### 9. Validar que el display muestre como resultado 0. Si no pasa la prueba, usar una de las siguientes tareas, en todos los casos incluir pasos a reproducir y captura de pantalla:
#Reportar un bug en JIRA
#Reportar un bug en Azure DevOps - Boards
#Reportar el bug por email.
#Crear un pdf con los detalles de bug.

#cierro la calculadora de windows
driver.quit()