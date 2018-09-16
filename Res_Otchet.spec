# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\Work\\python_projects\\RES_Otchet\\main.py'],
             pathex=['D:\\Work\\python_projects\\RES_Otchet'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Res_Otchet',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
