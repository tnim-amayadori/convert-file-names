import glob
from os import path
import sys

# Import project folder.
_tmp_path = path.dirname(__file__)
sys.path.append(_tmp_path)
from util import log_util

# Debug用の設定.
_root_path = r"C:\Users\yukoa\PycharmProjects\convert-file-names\Output"
_project_name = "convert-file-names"

_folder_path = r""
_target_name = "test*"
_new_name = ""
_is_partial = True
_extend = "txt"


def main(folder_path: str, target_name: str, new_name: str, is_partial: bool, extend: str):
    # Set name to search.
    target_name = glob.escape(target_name)
    if extend is not None and extend != "":
        if is_partial:
            target_name = "*" + target_name + "*." + extend
        else:
            target_name = target_name + "." + extend
    else:
        if is_partial:
            target_name = "*" + target_name + "*"

    log_util.logger.debug("target_name=[{0}]".format(target_name))



    # TODO

if __name__ == '__main__':
    log_util.init_logger(_root_path, _project_name, is_debug=True)
    main(_folder_path, _target_name, _new_name, _is_partial, _extend)
