@echo off
setlocal enabledelayedexpansion

REM Fonction pour la conversion d'un nombre en binaire
:codeB
set "n=%1"
if !n! EQU 0 (
    echo 0
) else (
    set "binary="
    :loop
    set /a "bit=!n! %% 2"
    set "binary=!bit!!binary!"
    set /a "n=!n! / 2"
    if !n! GTR 0 goto loop
    echo !binary!
)
exit /b

REM Fonction pour générer une liste de nombres binaires jusqu'à n
:ordre
set "nbr=%1"
set "result="
for /l %%i in (0,1,!nbr!) do (
    call :codeB %%i
)
exit /b

REM Saisie du nombre
set /p "nbr=Veuillez donner un nombre : "
call :ordre %nbr%
