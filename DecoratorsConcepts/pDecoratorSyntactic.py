import functools
def dfHelloWord(df_helloworld):
    @functools.wraps(df_helloworld)
    def dfWrapper():
        df_helloworld()
        df_helloworld()
    return dfWrapper

@dfHelloWord
def say_helloworld():
    print ('Hello World of Decorators')

say_helloworld()