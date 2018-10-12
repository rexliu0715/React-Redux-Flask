import pytest
from basedir import basedir
import os
import shutil
import sys


def main():
    argv = []

    argv.extend(sys.argv[1:])

    pytest.main(argv)

    try:
        os.remove(os.path.join(basedir, '.coverage'))

    except OSError:
        pass

    try:
        shutil.rmtree(os.path.join(basedir, '.cache'))

    except OSError:
        pass

    try:
        shutil.rmtree(os.path.join(basedir, 'tests/.cache'))
    except OSError:
        pass



if __name__ == '__main__':
    main()

#export DATABASE_URL="postgres://jkgqrwuhomkipe:4f6b74f4cf68fff945c1a4f9a067733f16d8a5dcba353b0458c63d0a43fd5d61@ec2-174-129-192-200.compute-1.amazonaws.com:5432/dbohohpujil9qf"