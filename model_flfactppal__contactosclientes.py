# @class_declaration interna_contactosclientes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_contactosclientes(modelos.mtd_contactosclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_contactosclientes #
class guanabana_sync_m2_contactosclientes(interna_contactosclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration contactosclientes #
class contactosclientes(guanabana_sync_m2_contactosclientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.contactosclientes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
