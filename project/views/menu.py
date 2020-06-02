from datetime import datetime

from pyramid.view import view_config, view_defaults

from .. import models

uge_lookup_tabel = {'Monday': 'Mandag', 'Tuesday': 'Tirsdag', 'Wednesday': 'Onsdag', 'Thursday': 'Torsdag',
                    'Friday': 'Fredag'}
strftime_iso = '%Y%m%d'


def initialize_dictionary(uge_dag: str):
    res = dict(retter=dict.fromkeys(list(range(1, 7)), ''))
    return dict({uge_dag: res})


def mapMenuTilRetter(daglig_menu: models.Menu):
    uge_dag = uge_lookup_tabel[daglig_menu.dato.strftime('%A')]
    data = initialize_dictionary(uge_dag)
    data[uge_dag]['dato'] = daglig_menu.dato.strftime(strftime_iso)
    for ret in sorted(daglig_menu.fk_ret, key=lambda sort_key: sort_key.sortering):
        data[uge_dag]['retter'][ret.sortering] = ret.item
    return data


@view_defaults(route_name='home', renderer='../templates/menu.mako')
class MenuViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):
        dbsession = self.request.dbsession
        menu = dbsession.query(models.Menu).order_by(models.Menu.dato)
        uge_menu = {}
        for daglig_menu in menu:
            ugenr = daglig_menu.dato.strftime('%Y%W')  # <Årstal><ugenr>
            if ugenr not in uge_menu:
                uge_menu[ugenr] = {}
            uge_menu[ugenr].update(mapMenuTilRetter(daglig_menu))
        return dict(menu=dict(sorted(uge_menu.items(), reverse=True)), today=datetime.today().strftime(strftime_iso))
