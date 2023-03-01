import os
from TBM_RezManager import utils

class Build(utils.Build):
    def post_build(self):
        # Package info file
        self.create_package_info(
            os.path.join(self.build_path, "TBM_hook", '__version__.py'))

if __name__ == "__main__":
    Build(
        exclude_patterns=["*.pyc", "__pycache__"], 
        keep_roots=[
            "resources",
            "TBM_hook",
            "LICENCE",
            "TBM_hook"
        ], 
        compile=True
    )




