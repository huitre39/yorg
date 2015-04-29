from ya2.build.build import extensions, get_files, image_extensions, \
    set_path, p3d_path_str, win_path_str, osx_path_str, linux_path_str, \
    src_path_str, devinfo_path_str, docs_path_str, build_p3d, build_windows, \
    build_osx, build_linux, build_src, build_devinfo, build_docs, \
    build_strings, build_string_template, build_images, win_path_noint_str,\
    osx_path_noint_str, linux_path_noint_str

argument_info = [
    ('path', 'built'), ('lang', 0), ('p3d', 0), ('source', 0), ('devinfo', 0),
    ('windows', 0), ('osx', 0), ('linux_32', 0), ('linux_64', 0), ('docs', 0),
    ('images', 0), ('nointernet', 0)]
arguments = dict((arg, ARGUMENTS.get(arg, default))
                  for arg, default in argument_info)
if any(arguments[arg] for arg in ['windows', 'osx', 'linux_32', 'linux_64']):
    arguments['p3d'] = 1
if arguments['p3d']:
    arguments['images'] = 1
path = set_path(arguments['path'])
app_name = 'yorg'
lang_path = 'assets/locale/'

p3d_path = p3d_path_str.format(path=path, name=app_name)
win_path = win_path_str.format(path=path, name=app_name)
osx_path = osx_path_str.format(path=path, name=app_name)
linux_path_32 = linux_path_str.format(path=path, name=app_name,
                                      platform='i386')
linux_path_64 = linux_path_str.format(path=path, name=app_name,
                                      platform='amd64')
win_path_noint = win_path_noint_str.format(path=path, name=app_name)
osx_path_noint = osx_path_noint_str.format(path=path, name=app_name)
linux_path_32_noint = linux_path_noint_str.format(path=path, name=app_name,
                                                  platform='i386')
linux_path_64_noint = linux_path_noint_str.format(path=path, name=app_name,
                                                  platform='amd64')
src_path = src_path_str.format(path=path, name=app_name)
devinfo_path = devinfo_path_str.format(path=path, name=app_name)
docs_path = docs_path_str.format(path=path, name=app_name)

bld_p3d = Builder(action=build_p3d)
bld_windows = Builder(action=build_windows)
bld_osx = Builder(action=build_osx)
bld_linux = Builder(action=build_linux)
bld_src = Builder(action=build_src)
bld_devinfo = Builder(action=build_devinfo)
bld_docs = Builder(action=build_docs)
bld_images = Builder(action=build_images)
bld_str = Builder(action=build_strings, suffix='.mo', src_suffix='.po')
bld_str_tmpl = Builder(action=build_string_template, suffix='.pot',
                       src_suffix='.py')

env = Environment(BUILDERS={'p3d': bld_p3d, 'windows': bld_windows,
                            'osx': bld_osx, 'linux': bld_linux,
                            'source': bld_src, 'devinfo': bld_devinfo,
                            'docs': bld_docs, 'images': bld_images,
                            'str': bld_str, 'str_tmpl': bld_str_tmpl})
env['P3D_PATH'] = p3d_path
env['NAME'] = app_name
env['LANG'] = lang_path
env['NOINTERNET'] = arguments['nointernet']

VariantDir(path, '.')

img_files = image_extensions(get_files(['psd']))
if arguments['images']:
    env.images(img_files, get_files(['psd']))
if arguments['p3d']:
    src_p3d = get_files(extensions) + img_files + \
        [lang_path+'it_IT/LC_MESSAGES/%s.mo' % app_name]
    env.p3d([p3d_path], src_p3d)
if arguments['source']:
    env.source([src_path], get_files(extensions))
if arguments['devinfo']:
    env.devinfo([devinfo_path], get_files(['py']))
if arguments['windows']:
    out_path = win_path_noint if arguments['nointernet'] else win_path
    env.windows([out_path], [p3d_path])
if arguments['osx']:
    out_path = osx_path_noint if arguments['nointernet'] else osx_path
    env.osx([out_path], [p3d_path])
if arguments['linux_32']:
    out_path = linux_path_32_noint if arguments['nointernet'] \
        else linux_path_32
    env.linux([out_path], [p3d_path], PLATFORM='i386')
if arguments['linux_64']:
    out_path = linux_path_64_noint if arguments['nointernet'] \
        else linux_path_64
    env.linux([out_path], [p3d_path], PLATFORM='amd64')
if arguments['docs']:
    env.docs([docs_path], get_files(['py']))
if arguments['lang']:
    for lang_code in ['it_IT']:
        tmpl = env.str_tmpl(
            lang_path+lang_code+'/LC_MESSAGES/%s.po' % app_name,
            get_files(['py']))
        env.Precious(tmpl)
        env.str(lang_path+lang_code+'/LC_MESSAGES/%s.mo' % app_name,
                lang_path+lang_code+'/LC_MESSAGES/%s.po' % app_name)