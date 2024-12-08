# Forzar la salida en UTF-8 para mostrar correctamente los caracteres especiales
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Obtiene la ruta completa donde está ubicado el script (sin cambiar el directorio de trabajo actual)
$scriptDir = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition

# Muestra la ruta del directorio del script
Write-Output "`nDirectorio del script actual: $scriptDir`n"

# Ruta al entorno virtual dentro del directorio del script
$envPath = Join-Path -Path $scriptDir -ChildPath ".env"

# Verifica si el entorno virtual ya existe, si no, lo crea
if (!(Test-Path -Path $envPath)) {
    Write-Output "`nCreando el entorno virtual en '$envPath'...`n"
    python -m venv $envPath
} else {
    Write-Output "`nEl entorno virtual ya existe en '$envPath'.`n"
}

# Ruta al script de activación del entorno virtual
$activatePath = Join-Path -Path $envPath -ChildPath "Scripts\Activate.ps1"

# Activa el entorno virtual creado, si existe
if (Test-Path -Path $activatePath) {
    Write-Output "`nActivando el entorno virtual desde: $activatePath`n"
    & $activatePath
} else {
    Write-Output "`nNo se encontró el script de activación en: $activatePath`n"
    exit
}

# Actualiza 'pip' a la última versión dentro del entorno virtual
Write-Output "`nActualizando 'pip' a la última versión...`n"
python -m pip install --upgrade pip

# Ruta al archivo requirements.txt
$requirementsPath = Join-Path -Path $scriptDir -ChildPath "requirements.txt"

# Instala las dependencias listadas en requirements.txt si el archivo existe
if (Test-Path -Path $requirementsPath) {
    Write-Output "`nInstalando dependencias desde: $requirementsPath`n"
    pip install -r $requirementsPath
} else {
    Write-Output "`nNo se encontró el archivo requirements.txt en: $requirementsPath`n"
}

# Verifica si Docker Desktop está en ejecución; si no, lo inicia
if (-not (Get-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue)) {
    Write-Output "`nIniciando Docker Desktop...`n"
    Start-Process -NoNewWindow "C:\Program Files\Docker\Docker\Docker Desktop.exe" -ArgumentList "--background"
    Start-Sleep -Seconds 10
} else {
    Write-Output "`nDocker Desktop ya está en ejecución.`n"
}

# Verifica si el puerto 54320 está en uso antes de iniciar Docker Compose
$puerto = 54320
if (Get-NetTCPConnection -LocalPort $puerto -ErrorAction SilentlyContinue) {
    Write-Output "`nEl puerto $puerto ya está en uso. Se recomienda cambiar el puerto en docker-compose.yml a uno disponible, como 54321.`n"
    exit
}

# Ruta al archivo docker-compose.yml
$composeFilePath = Join-Path -Path $scriptDir -ChildPath "docker-compose.yml"

# Verifica que el archivo docker-compose.yml existe antes de ejecutarlo
if (Test-Path -Path $composeFilePath) {
    Write-Output "`nEjecutando Docker Compose desde: $composeFilePath`n"
    docker-compose -f $composeFilePath up -d
} else {
    Write-Output "`nEl archivo docker-compose.yml no se encontró en: $composeFilePath`n"
}

# Mensaje opcional para apagar y eliminar los contenedores
# Write-Output "`nPara detener y eliminar los contenedores, usa: docker-compose -f $composeFilePath down`n"

# Desactivación opcional del entorno virtual (requiere cerrar la sesión o terminal)
# No es necesario incluir `deactivate` explícitamente, ya que PowerShell no tiene un comando directo para ello en virtualenv.
