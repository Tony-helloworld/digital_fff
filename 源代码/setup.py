from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    executables=[Executable("launcher.py")],
    # Include other files
    options={
        "build_exe": {
            "includes": ["algorithms"],  # Include additional modules or packages
            "include_files": ["qmain.ui"],  # Include additional files
        }
    }
)
