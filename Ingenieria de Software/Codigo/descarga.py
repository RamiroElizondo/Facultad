import requests
import zipfile
import os
import subprocess

def download_chromedriver_136():
    """Descarga ChromeDriver específico para Chrome 136"""
    
    print("Descargando ChromeDriver para Chrome 136.0.7103.125...")
    
    # URL específica para Chrome 136 en Windows
    download_url = "https://storage.googleapis.com/chrome-for-testing-public/136.0.6776.0/win64/chromedriver-win64.zip"
    
    try:
        # Descargar el archivo
        print(f"Descargando desde: {download_url}")
        response = requests.get(download_url, timeout=60)
        
        if response.status_code != 200:
            # Intentar con otra versión compatible
            alternative_urls = [
                "https://storage.googleapis.com/chrome-for-testing-public/136.0.6776.12/win64/chromedriver-win64.zip",
                "https://storage.googleapis.com/chrome-for-testing-public/135.0.6751.0/win64/chromedriver-win64.zip"
            ]
            
            for url in alternative_urls:
                print(f"Intentando URL alternativa: {url}")
                response = requests.get(url, timeout=60)
                if response.status_code == 200:
                    download_url = url
                    break
            else:
                raise Exception("No se pudo descargar ninguna versión compatible")
        
        # Guardar el archivo ZIP
        zip_filename = "chromedriver-win64.zip"
        with open(zip_filename, "wb") as f:
            f.write(response.content)
        
        print("✅ Archivo descargado exitosamente")
        
        # Extraer el ChromeDriver
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            # Buscar chromedriver.exe en cualquier carpeta
            extracted = False
            for file_info in zip_ref.filelist:
                if file_info.filename.endswith('chromedriver.exe'):
                    # Extraer directamente al directorio actual
                    source = zip_ref.open(file_info)
                    with open('chromedriver.exe', 'wb') as target:
                        target.write(source.read())
                    extracted = True
                    print(f"✅ Extraído: {file_info.filename} -> chromedriver.exe")
                    break
            
            if not extracted:
                # Si no se encuentra, extraer todo y buscar
                zip_ref.extractall("temp_chromedriver")
                for root, dirs, files in os.walk("temp_chromedriver"):
                    for file in files:
                        if file == "chromedriver.exe":
                            source_path = os.path.join(root, file)
                            target_path = "chromedriver.exe"
                            os.rename(source_path, target_path)
                            extracted = True
                            print(f"✅ ChromeDriver movido a: {target_path}")
                            break
                    if extracted:
                        break
                
                # Limpiar carpeta temporal
                import shutil
                shutil.rmtree("temp_chromedriver", ignore_errors=True)
        
        # Limpiar el ZIP
        os.remove(zip_filename)
        
        if extracted:
            chromedriver_path = os.path.abspath("chromedriver.exe")
            print(f"✅ ChromeDriver listo en: {chromedriver_path}")
            
            # Verificar que funcione
            try:
                result = subprocess.run([chromedriver_path, "--version"], 
                                      capture_output=True, text=True, timeout=10)
                print(f"✅ Verificación exitosa: {result.stdout.strip()}")
                return chromedriver_path
            except Exception as e:
                print(f"⚠️  Error en verificación: {e}")
                return chromedriver_path
        else:
            raise Exception("No se pudo extraer chromedriver.exe")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    path = download_chromedriver_136()
    if path:
        print(f"\n🎉 ¡ChromeDriver descargado exitosamente!")
        print(f"📁 Ubicación: {path}")
        print(f"🔧 Ahora puedes ejecutar tu script principal")
    else:
        print(f"\n❌ No se pudo descargar ChromeDriver")
        print(f"💡 Intenta descargar manualmente desde:")
        print(f"   https://googlechromelabs.github.io/chrome-for-testing/")