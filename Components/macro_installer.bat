echo
echo Install some packages for you ...
echo Packages 1 / 7 installing : Chocolatey


@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

echo Packages 2 / 7 installing : Python
choco install python -y

echo Packages 3 / 7 installing : Swig

choco install swig -y

echo installing packages 4 / 7 : C++

choco install microsoft-visual-cpp-build-tools

echo upgrading pip : 

pip install --upgrade pip

echo Packages 5 / 7 installing : Python Keyboard 

pip install keyboard

echo Packages 6 / 7 installing : Pyhook3

pip install Pyhook3

echo packages installing 7 / 7 : pywin32

pip install pywin32

echo Starting App  

python macro.py

python app.py



