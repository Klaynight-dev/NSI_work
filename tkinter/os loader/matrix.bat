
@echo off
mode con cols=64 lines=35 &color 0a
title Animation Matrix V2 ^|  by Batchapp
:m
cls
set /a empty = empty + 1
set BAR=%BAR%Û
echo.
echo.
echo              Chargement ...........
echo.
echo              %BAR%                             
echo.
if %empty%==37 goto endbar
@ping localhost -n 1 >nul
echo          %random% %random% %random% %random% %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo  %random%   %random%%random% %random%    %random%   %random% %random% %random%   %random%
echo    %random%  %random%   %random% %random%        %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%  %random% %random% %random%   %random%
echo %random%   %random%   %random% %random%    %random%     %random%     %random% %random%
echo  %random%   %random%   %random% %random%    %random%   %random% %random% %random%   %random%
echo          %random% %random% %random% %random% %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo  %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo    %random%  %random%   %random% %random%        %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%  %random% %random% %random%   %random%
echo %random%   %random%   %random%%random%    %random%     %random%     %random% %random%
echo  %random%   %random%   %random% %random%    %random%   %random% %random% %random%   %random%
echo          %random% %random% %random% %random% %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo  %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo    %random%  %random%   %random% %random%         %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%  %random% %random% %random%   %random%
echo %random%   %random%   %random% %random%    %random%     %random%     %random% %random%
echo  %random%   %random%   %random% %random%    %random%   %random% %random% %random%   %random%
goto m
:endbar
echo suite du code !
pause>nul
