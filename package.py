name = "tik_manager"

version = "4.3.7"

requires = [
    "python",
    "requests"
]

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.prepend("{root}")

    # Adds Maya Integration
    env.MAYA_MODULE_PATH.prepend("{root}/tik_manager4/dcc/maya/setup")
