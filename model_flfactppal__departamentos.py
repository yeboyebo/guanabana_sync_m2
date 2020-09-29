# @class_declaration interna_departamentos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_departamentos(modelos.mtd_departamentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_departamentos #
class guanabana_sync_m2_departamentos(interna_departamentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration departamentos #
class departamentos(guanabana_sync_m2_departamentos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.departamentos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
