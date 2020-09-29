# @class_declaration interna_secuencias #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_secuencias(modelos.mtd_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_secuencias #
class guanabana_sync_m2_secuencias(interna_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration secuencias #
class secuencias(guanabana_sync_m2_secuencias, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.secuencias_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
