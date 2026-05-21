@echo off
REM Create backend directory structure for FoodLion

cd /d e:\FoodLion

echo Creating backend directory structure...
echo.

mkdir backend 2>nul
mkdir backend\foodlion 2>nul
mkdir backend\authentication 2>nul
mkdir backend\restaurants 2>nul
mkdir backend\menu_items 2>nul
mkdir backend\orders 2>nul
mkdir backend\adminpanel 2>nul

echo.
echo Backend directory structure created successfully!
echo.
echo Verifying directory structure...
echo.

dir backend /B

echo.
echo All directories verified!
echo.
pause
