# @class_declaration interna_empresa #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_empresa(modelos.mtd_empresa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_empresa #
class guanabana_sync_m2_empresa(interna_empresa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration empresa #
class empresa(guanabana_sync_m2_empresa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.empresa_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
