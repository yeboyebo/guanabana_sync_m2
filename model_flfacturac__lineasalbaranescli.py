# @class_declaration interna_lineasalbaranescli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineasalbaranescli(modelos.mtd_lineasalbaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_lineasalbaranescli #
class guanabana_sync_m2_lineasalbaranescli(interna_lineasalbaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineasalbaranescli #
class lineasalbaranescli(guanabana_sync_m2_lineasalbaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineasalbaranescli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
