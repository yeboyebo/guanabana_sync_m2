# @class_declaration interna_cuentasbco_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_cuentasbco_imp(modelos.mtd_cuentasbco_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_cuentasbco_imp #
class guanabana_sync_m2_cuentasbco_imp(interna_cuentasbco_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration cuentasbco_imp #
class cuentasbco_imp(guanabana_sync_m2_cuentasbco_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.cuentasbco_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
