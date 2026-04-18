[Setup]
AppName=MikuMikuWidget2026
AppVersion=2.5
AppPublisher=storchP
DefaultDirName={autopf}\MikuMikuWidget2026
DefaultGroupName=MikuMikuWidget2026
OutputDir=E:\MikuMikuWidget\MMW2\dist
OutputBaseFilename=MMW2026install
SetupIconFile=E:\MikuMikuWidget\MMW2\icon.ico
UninstallDisplayIcon={app}\MikuMikuWidget2026.exe
Compression=lzma2
SolidCompression=yes
LanguageDetectionMethod=locale

[Languages]
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Files]
Source: "E:\MikuMikuWidget\MMW2\dist\MikuMikuWidget2026.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\MikuMikuWidget\MMW2\icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MikuMikuWidget2026"; Filename: "{app}\MikuMikuWidget2026.exe"; IconFilename: "{app}\icon.ico"
Name: "{group}\MikuMikuWidget2026 をアンインストール"; Filename: "{uninstallexe}"
Name: "{autodesktop}\MikuMikuWidget2026"; Filename: "{app}\MikuMikuWidget2026.exe"; IconFilename: "{app}\icon.ico"

[Run]
Filename: "{app}\MikuMikuWidget2026.exe"; Description: "アプリケーションを実行する"; Flags: nowait postinstall skipifsilent
