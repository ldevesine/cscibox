# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_baconc', [dirname(__file__)])
        except ImportError:
            import _baconc
            return _baconc
        if fp is not None:
            try:
                _mod = imp.load_module('_baconc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _baconc = swig_import_helper()
    del swig_import_helper
else:
    import _baconc
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class PreCalDet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PreCalDet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PreCalDet, name)
    __repr__ = _swig_repr

    def __init__(self, enm, ey, estd, edpth, ea, eb, years, probs):
        this = _baconc.new_PreCalDet(enm, ey, estd, edpth, ea, eb, years, probs)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def ShortOut(self):
        return _baconc.PreCalDet_ShortOut(self)

    def U(self, theta):
        return _baconc.PreCalDet_U(self, theta)

    def Ut(self, theta):
        return _baconc.PreCalDet_Ut(self, theta)
    __swig_destroy__ = _baconc.delete_PreCalDet
    __del__ = lambda self: None
PreCalDet_swigregister = _baconc.PreCalDet_swigregister
PreCalDet_swigregister(PreCalDet)


def runSimulation(numdets, dets, numhiatus, hdata, sections, a, b, minyr, maxyr, th0, thp0, c0, cm, outfile, numsamples):
    return _baconc.runSimulation(numdets, dets, numhiatus, hdata, sections, a, b, minyr, maxyr, th0, thp0, c0, cm, outfile, numsamples)
runSimulation = _baconc.runSimulation

def run_simulation(numdets, dets, hdim, sections, memorya, memoryb, minyr, maxyr, firstguess, secondguess, mindepth, maxdepth, outfile, numsamples):
    return _baconc.run_simulation(numdets, dets, hdim, sections, memorya, memoryb, minyr, maxyr, firstguess, secondguess, mindepth, maxdepth, outfile, numsamples)
run_simulation = _baconc.run_simulation
# This file is compatible with both classic and new-style classes.


