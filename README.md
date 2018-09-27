# pytest-headlock
Some pytest plugins and helper modules to simplify using headlock
with pytest.


### Error Reporting Plugin

pytest_headlock will install a plugin called "headlock-report-error".
This plugin ensures that when a C-module fails due to a compile-error
(i.e. invalid syntax) you will not get a python exception of
type ```CompileError``` with the corresponing stack trace (which refers
into modules of headlock). Instead you get well formatted C error
messages like:

```
==== ERROR IN C SOURCE CODE ===================
C:\Users\user1\Development\project1\tests\file1.c:100: Error 1
C:\Users\user1\Development\project1\tests\file1.c:102: Error 2
C:\Users\user1\Development\project1\tests\file1.c:210: Error 3
===============================================
```


### Debugging Support Plugin

pytest_headlock will install a plugin called "headlock-debug-support".
It can be used when you need to debug into a failing C module
with the debugger of your IDE.

This plugin creates a file ```.pytest-headlock/CMakeLists.txt```,
in the [pytest root directory](https://docs.pytest.org/en/latest/customize.html#finding-the-rootdir).
This CMakeLists file can be incorporated (via
[add_subdirectory](https://cmake.org/cmake/help/v3.0/command/add_subdirectory.html))
into your main CMakeLists file.

It creates a shared library project starting with ```TS_*```.
you can debug this shared library from your IDE by running the
following executable from within any directory of your project
(it will search the root directory containing ```.pytest-headlock```
automaticially):

```
python -m pytest_headlock.debug_failed
```

This module will rerun the *first failed test* of the last regular
pytest run (or the *last test at all* if no one failed). Furthermore it
will ensure that the C code is not build automaticially, as it was
already build by your IDE.


### Helper Methods

 - ```testsetup_fixture``` decorator

   Simplifies creation of testsetups as reuable fixtures:

   ```python
   from headlock import TestSetup, CModule
   from pytest_headlock import testsetup fixture

   @testsetup_fixture
   @CModule('test.c')
   class ts(TestSetup):
       def __startup__(ts):
          pass  # will be run BEFORE running test function
       def __shutdown__(ts):
          pass  # will be run AFTER running test function

   def test_foo(ts):
       ts.c_func()
   ```

 - ```val_ptr()``` / ```mem_ptr()```

   Convenience method to compare pointers. As in C parameters are
   passed by-reference (=pointers) instead of by-value. But in headlock
   comparing pointers means you compare the address they are pointing
   to. Thus when using a mock framework like
   ```unittest.mock.assert_called_*_with()``` it is hard to check
   if the passed value is correct.

   To compare the value referred by a pointer it has to be resolved:
   ```ts.pointer.ref.val == 123```. This can be replaced by val_ptr:
   ```val_ptr(ts.pointer) == 123``` (```mem_ptr``` will resolve to
   ```ts.pointer.ref.mem```).

   Assume we have a C function signature ```void c_func(char * buf, int buf_len);```
   When mocking this function it is pretty easy now to check if
   a specific value was passed to *buf*:

   ```python
   def test_foo(ts):
       ts.c_func = unittest.mock.Mock()
       ### run some C code that calls c_func
       ts.c_func.assert_called_with(mem_ptr(b'test'), 4)
   ```