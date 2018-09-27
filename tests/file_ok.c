#if ! defined(FUNCNAME)
    #define FUNCNAME func
#endif
#if ! defined(RET_VAL)
    #define RET_VAL 123
#endif

int FUNCNAME(void)
{
    return RET_VAL;
}