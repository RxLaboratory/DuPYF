def get_baseName( filename ):
    """Gets the name part of a filename without the extension"""
    fileBaseName = filename
    fileBaseNameList = filename.split('.')
    if len(fileBaseNameList) > 1:
        fileBaseName = '.'.join(fileBaseNameList[0:-1])
    return fileBaseName