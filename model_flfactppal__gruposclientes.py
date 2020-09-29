# @class_declaration interna_gruposclientes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_gruposclientes(modelos.mtd_gruposclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_gruposclientes #
class guanabana_sync_m2_gruposclientes(interna_gruposclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration gruposclientes #
class gruposclientes(guanabana_sync_m2_gruposclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.gruposclientes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
