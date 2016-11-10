#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Sat, 19 Sep 2015, 09:53:47
#========================================
import sys, re, os
import distutils.core, distutils.extension
import Cython.Build
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def py2pyd(path):
    '''
    '''
    os.chdir(path)

    file_list = os.listdir(path)
    for f in file_list:
        if os.path.isdir(f):
            continue

        if not re.search('.py$', f):
            continue

        if re.match('setup.py', f):
            continue

        if re.match('__init__.py', f):
            continue

        if re.search('_rc.py', f):
            continue

        extensions = [distutils.extension.Extension(os.path.splitext(f)[0], [f], include_dirs=[])]
        distutils.core.setup(name='pytopyd', ext_modules=Cython.Build.cythonize(extensions))

        cpp_file = '{0}.c'.format(os.path.splitext(f)[0])
        os.path.isfile(cpp_file) and os.remove(cpp_file)



if __name__ == '__main__':
    path = os.getcwd()
    py2pyd(path)
