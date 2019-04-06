from kivy.deps import sdl2, glew


# -*- mode: python -*-


block_cipher = None

kivydata = [('Users\Pudim\Desktop\Estudo em Python\Kivy\Telas+Desenho\main2.kv', 'main2')]

a = Analysis(['Principal.py'],
             pathex=['C:\\Users\\Pudim\\Desktop\\Estudo em Python\\Kivy\\Telas+Desenho'],
             binaries=[],
             datas=[('Users\Pudim\Desktop\Estudo em Python\Kivy\Telas+Desenho\main2.kv', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Desenho',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Desenho')
