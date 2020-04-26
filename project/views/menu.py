from pyramid.view import view_config, view_defaults

@view_defaults(route_name='home', renderer='../templates/menu.mako')
class MenuViews(object):
    def __init__(self, request):
        self.request = request

    def mocked_data(selfs):
        data = {}
        for date in ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag']:
            data[date] = {}
            data[date]['salat1'] = 'The good'
            data[date]['salat2'] = 'The bad'
            data[date]['paalaeg1'] = 'The medioore'
            data[date]['paalaeg2'] = 'the pis'
            data[date]['varm'] = 'The best'
        return data


    @view_config(request_method='GET')
    def get(self):
        uge_menu = {}
        uge_menu['202020'] = self.mocked_data()
        uge_menu['192020'] = self.mocked_data()
        return dict(menu=uge_menu)

