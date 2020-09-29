# @class_declaration interna_secuenciasejercicios #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_secuenciasejercicios(modelos.mtd_secuenciasejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_secuenciasejercicios #
class guanabana_sync_m2_secuenciasejercicios(interna_secuenciasejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration secuenciasejercicios #
class secuenciasejercicios(guanabana_sync_m2_secuenciasejercicios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.secuenciasejercicios_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
