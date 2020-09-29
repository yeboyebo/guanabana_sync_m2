# @class_declaration interna_cuentasbanco #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_cuentasbanco(modelos.mtd_cuentasbanco, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_cuentasbanco #
class guanabana_sync_m2_cuentasbanco(interna_cuentasbanco, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration cuentasbanco #
class cuentasbanco(guanabana_sync_m2_cuentasbanco, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.cuentasbanco_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
