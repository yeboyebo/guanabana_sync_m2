# @class_declaration interna_textosinformes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_textosinformes(modelos.mtd_textosinformes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_textosinformes #
class guanabana_sync_m2_textosinformes(interna_textosinformes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration textosinformes #
class textosinformes(guanabana_sync_m2_textosinformes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.textosinformes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
