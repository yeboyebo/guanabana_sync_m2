# @class_declaration interna_agruparalbaranesprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_agruparalbaranesprov(modelos.mtd_agruparalbaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_agruparalbaranesprov #
class guanabana_sync_m2_agruparalbaranesprov(interna_agruparalbaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration agruparalbaranesprov #
class agruparalbaranesprov(guanabana_sync_m2_agruparalbaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.agruparalbaranesprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
