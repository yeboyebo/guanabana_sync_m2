# @class_declaration interna_lecturasinvetariocsv #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactalma import models as modelos


class interna_lecturasinvetariocsv(modelos.mtd_lecturasinvetariocsv, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration guanabana_sync_m2_lecturasinvetariocsv #
class guanabana_sync_m2_lecturasinvetariocsv(interna_lecturasinvetariocsv, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lecturasinvetariocsv #
class lecturasinvetariocsv(guanabana_sync_m2_lecturasinvetariocsv, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.lecturasinvetariocsv_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
