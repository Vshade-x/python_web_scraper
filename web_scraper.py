import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. CONFIGURACIÓN
URL_BASE = "http://books.toscrape.com/"
lista_libros = [] 

# 2. FUNCIÓN DE RASPADO (SCRAPING)
def raspar_datos():
    print(f"Iniciando raspado de datos de: {URL_BASE}")
    
    respuesta = requests.get(URL_BASE)
    
    if respuesta.status_code == 200:
        print("Conexión exitosa. Analizando HTML...")
        sopa = BeautifulSoup(respuesta.content, 'html.parser')
        productos = sopa.find_all('article', class_='product_pod')
        
        for producto in productos:
            try:
                titulo = producto.h3.a['title']
            except AttributeError:
                titulo = "N/A"
            
            precio_raw = producto.find('p', class_='price_color').text.strip()
            precio_limpio = float(precio_raw.replace('£', ''))
            
            lista_libros.append({
                'Titulo del Libro': titulo,       # Nombre de columna más descriptivo y con espacios
                'Precio (GBP)': precio_limpio     # Nombre de columna claro para el valor numérico con moneda
            })
            
        print(f"✅ Extracción completada. Se encontraron {len(lista_libros)} libros.")
        exportar_a_csv(lista_libros)
        
    else:
        print(f"❌ Error al conectar. Código de estado: {respuesta.status_code}")

# 3. FUNCIÓN DE EXPORTACIÓN (¡Ajuste Final Aquí!)
def exportar_a_csv(datos):
    df = pd.DataFrame(datos)
    
    # Aseguramos el orden de las columnas para la salida
    columnas_finales = ['Titulo del Libro', 'Precio (GBP)'] 
    df_final = df[columnas_finales]
    
    archivo_salida = 'reporte_libros_scraping.csv'
    
    # Reemplaza la línea de df_final.to_csv(...) con esta versión
    df_final.to_csv(archivo_salida, index=False, encoding='utf-8', sep=';', decimal='.')
    
    print(f"✅ Reporte de Web Scraping guardado como: {archivo_salida}")

# Ejecutar la función principal
if __name__ == "__main__":
    raspar_datos()