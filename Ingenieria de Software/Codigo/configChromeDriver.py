import os
import subprocess
import requests
import zipfile
import shutil
from pathlib import Path

def find_chromedriver():
    """Busca ChromeDriver en ubicaciones comunes"""
    common_paths = [
        os.path.join(os.path.dirname(__file__), "chromedriver.exe"),
        "chromedriver.exe",
        "./chromedriver.exe",
        ".\chromedriver.exe",
        "C:/chromedriver/chromedriver.exe",
        "C:/WebDriver/bin/chromedriver.exe",
        os.path.expanduser("~/AppData/Local/Google/Chrome/Application/chromedriver.exe"),
        "C:/Program Files/Google/Chrome/Application/chromedriver.exe",
        "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
        "Codigo\chromedriver.exe"
    ]
    
    print("🔍 Buscando ChromeDriver existente...")
    for path in common_paths:
        print(path)
        if os.path.exists(path):
            abs_path = os.path.abspath(path)
            print(f"✅ ChromeDriver encontrado: {abs_path}")
            return abs_path
    
    print("❌ No se encontró ChromeDriver existente")
    return None

def download_compatible_chromedriver():
    """Descarga ChromeDriver compatible con Chrome 136"""
    print("📥 Descargando ChromeDriver compatible...")
    
    # URLs para diferentes versiones compatibles con Chrome 136
    urls_to_try = [
        "https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.68/win64/chromedriver-win64.zip",
    ]
    
    for url in urls_to_try:
        try:
            print(f"🌐 Intentando descargar desde: {url}")
            response = requests.get(url, timeout=30)
            
            if response.status_code == 200:
                # Guardar y extraer
                zip_path = "chromedriver_temp.zip"
                with open(zip_path, "wb") as f:
                    f.write(response.content)
                
                # Extraer ChromeDriver
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    # Buscar chromedriver.exe en el ZIP
                    for file_info in zip_ref.filelist:
                        if file_info.filename.endswith('chromedriver.exe'):
                            # Extraer directamente
                            source = zip_ref.open(file_info)
                            with open('chromedriver.exe', 'wb') as target:
                                target.write(source.read())
                            
                            os.remove(zip_path)
                            abs_path = os.path.abspath("chromedriver.exe")
                            print(f"✅ ChromeDriver descargado: {abs_path}")
                            
                            # Verificar que funciona
                            try:
                                result = subprocess.run([abs_path, "--version"], 
                                                      capture_output=True, text=True, timeout=5)
                                print(f"✅ Versión: {result.stdout.strip()}")
                                return abs_path
                            except:
                                print("⚠️  Error verificando ChromeDriver")
                                return abs_path
                
                os.remove(zip_path)
                
        except Exception as e:
            print(f"❌ Error con {url}: {e}")
            continue
    
    return None

def setup_chromedriver():
    """Configura ChromeDriver para Appium"""
    print("🔧 Configurando ChromeDriver para Appium...\n")
    
    # Buscar ChromeDriver existente
    chromedriver_path = find_chromedriver()
    
    # Si no existe, descargar
    if not chromedriver_path:
        chromedriver_path = download_compatible_chromedriver()
    
    if chromedriver_path:
        print(f"\n🎉 ChromeDriver listo:")
        print(f"📁 Ruta: {chromedriver_path}")
        print(f"✅ Existe: {os.path.exists(chromedriver_path)}")
        
        # Verificar permisos
        if os.access(chromedriver_path, os.X_OK):
            print("✅ Permisos de ejecución: OK")
        else:
            print("⚠️  Sin permisos de ejecución")
        
        return chromedriver_path
    else:
        print("\n❌ No se pudo configurar ChromeDriver")
        print("💡 Intenta descargar manualmente desde:")
        print("   https://googlechromelabs.github.io/chrome-for-testing/")
        return None

if __name__ == "__main__":
    path = setup_chromedriver()
    
    if path:
        print(f"\n🚀 Para usar en tu script:")
        print(f'options.set_capability("chromedriverExecutable", r"{path}")')
        
        # Crear un archivo de configuración
        config_content = f'''# Configuración ChromeDriver generada automáticamente
CHROMEDRIVER_PATH = r"{path}"

# Usar en tu script:
# options.set_capability("chromedriverExecutable", CHROMEDRIVER_PATH)
'''
        
        with open("chromedriver_config.py", "w") as f:
            f.write(config_content)
        
        print(f"✅ Configuración guardada en: chromedriver_config.py")
    else:
        print(f"\n❌ Configuración fallida")