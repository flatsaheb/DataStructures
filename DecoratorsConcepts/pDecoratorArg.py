'''
Function we are decorating is having parameters
'''
import functools
def dfHelloName(df_HelloName):
    @functools.wraps(df_HelloName)
    def wInner(*args, **kwargs):
        df_HelloName(*args, **kwargs)
    return wInner

def df_HelloName(name):
    print ("Hello {}".format(name))

df_HelloName('Fakhru')