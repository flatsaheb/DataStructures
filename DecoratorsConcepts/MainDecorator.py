'''
Creating decorator function to re-use it in other programs
'''
import functools

def dfHelloWorld(df_sayhello):
    @functools.wraps(df_sayhello)
    def wInnerFunction():
        df_sayhello()
    return wInnerFunction