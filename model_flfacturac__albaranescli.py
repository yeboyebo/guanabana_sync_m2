# @class_declaration interna_albaranescli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_albaranescli(modelos.mtd_albaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_albaranescli #
class guanabana_sync_m2_albaranescli(interna_albaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration albaranescli #
class albaranescli(guanabana_sync_m2_albaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.albaranescli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
