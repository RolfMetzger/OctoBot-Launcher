# -*- mode: python -*-

block_cipher = None


a = Analysis(['../entrypoint.py'],
             pathex=['../'],
             binaries=[],
             datas=[('../launcher', 'launcher')],
             hiddenimports=["glob", "subprocess", "json", "requests", "os", "logging",
             "distutils", "distutils.version", "config", "flask"],
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
          name='launcher_app',
          debug=False,
          strip=False,
          icon="favicon.ico",
          upx=True,
          runtime_tmpdir=None,
          console=True )
