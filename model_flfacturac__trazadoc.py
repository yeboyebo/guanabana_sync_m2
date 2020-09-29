# @class_declaration interna_trazadoc #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_trazadoc(modelos.mtd_trazadoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_trazadoc #
class guanabana_sync_m2_trazadoc(interna_trazadoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration trazadoc #
class trazadoc(guanabana_sync_m2_trazadoc, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.trazadoc_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
