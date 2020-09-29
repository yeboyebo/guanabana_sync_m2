# @class_declaration interna_descuentosclientes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_descuentosclientes(modelos.mtd_descuentosclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_descuentosclientes #
class guanabana_sync_m2_descuentosclientes(interna_descuentosclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration descuentosclientes #
class descuentosclientes(guanabana_sync_m2_descuentosclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.descuentosclientes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
