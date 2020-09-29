# @class_declaration interna_lineasalbaranesprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineasalbaranesprov(modelos.mtd_lineasalbaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_lineasalbaranesprov #
class guanabana_sync_m2_lineasalbaranesprov(interna_lineasalbaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineasalbaranesprov #
class lineasalbaranesprov(guanabana_sync_m2_lineasalbaranesprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineasalbaranesprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
