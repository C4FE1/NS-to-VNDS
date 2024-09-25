# NS-to-VNDS

## A Guide of how "Convert" a NScripter game to VNDS
The NScripter engine has already 26 years and a bunch of plataforms dont support anymore
for that a guide of how "Convert" a NScripter game exists.

## About the code
The code here has a example of how "convert" the game Tsukihime.

## Steps
  0. Setup
  1. Extracting game assets
  2. (Optional) Extracting game script
  3. Writing code to write the scripts 
### 0. Install wget and wine (LINUX/POSIX only)
The easiest way to use the tools for extract games achive is use the Windows binaries
### 1. Extract the game assets

1.1 Download NSAOUT from insani
  On Linux/POSIX
  ```bash
  wget http://nscripter.insani.org/downloads/nsaout.zip
  ```
1.2 Download SARDEC from insani
  On Linux/POSIX
  ```bash
  wget http://nscripter.insani.org/downloads/sardec.zip
  ```
1.3 Download NSDEC from insani
  On Linux/POSIX
  ```bash
  wget http://nscripter.insani.org/downloads/nsdec.zip
  ```
2.0 With that done extract all binaries and move toyour games folder
2.1 Extract and move NSAOUT
  On Linux/POSIX
  ```bash
  unzip nsaout.zip
  mv nsaout.exe [Your Game Folder]
  ```
2.2 Extract and move SARDEC
  On Linux/POSIX
  ```bash
  unzip sardec.zip
  mv sardec.exe [Your Game Folder]
  ```
2.3 Extract and move NSDEC
  On Linux/POSIX
  ```bash
  unzip nsdec.zip
  mv NSDEC.exe [Your Game Folder]
  ```
3.0 Some explanation of what all that programs does

NSAOUT
  Extracts .nsa files which contains game assest
SARDEC
  Extracts .sar files which also contains game assests
  usually has less files than .nsa
NSDEC
  Extract nscript.dat which is the game script/code
4.0 Extracting game assets/script
4.1 Extract game script
  ```bash
  wine NSDEC.exe nscript.dat
  ```
4.2 Extract game assets (from .nsa files)
  ```bash
  wine nsaout.exe *.nsa
  ```
4.3 Extract game assets (from .sar files)
  ```bash
  wine sardec.exe *.sar
  ```
5.to be continued

