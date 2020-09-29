# @class_declaration interna_datosadicionales #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_datosadicionales(modelos.mtd_datosadicionales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_datosadicionales #
class guanabana_sync_m2_datosadicionales(interna_datosadicionales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration datosadicionales #
class datosadicionales(guanabana_sync_m2_datosadicionales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.datosadicionales_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
