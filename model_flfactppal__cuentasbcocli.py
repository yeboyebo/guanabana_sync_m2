# @class_declaration interna_cuentasbcocli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_cuentasbcocli(modelos.mtd_cuentasbcocli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_cuentasbcocli #
class guanabana_sync_m2_cuentasbcocli(interna_cuentasbcocli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration cuentasbcocli #
class cuentasbcocli(guanabana_sync_m2_cuentasbcocli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.cuentasbcocli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
