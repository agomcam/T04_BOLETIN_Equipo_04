# Forzar la salida en UTF-8 para mostrar correctamente los caracteres especiales
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Obtiene la ruta completa donde está ubicado el script y la muestra en consola
$scriptDir = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
Write-Output "`nDirectorio del script actual: $scriptDir`n"

# Construye la ruta al script de activación del entorno virtual y la muestra en consola
$activatePath = Join-Path -Path $scriptDir -ChildPath ".env\Scripts\Activate.ps1"
Write-Output "`nRuta esperada del archivo de activación: $activatePath`n"

# Verifica si el archivo de activación existe y lo ejecuta, mostrando mensajes según el resultado
if (Test-Path -Path $activatePath) {
    Write-Output "`nActivando el entorno virtual desde: $activatePath`n"
    & $activatePath
} else {
    Write-Output "`nEl entorno virtual no se encontró en la ruta esperada: $activatePath`n"
}
