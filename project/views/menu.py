from pyramid.view import view_config, view_defaults

@view_defaults(route_name='home', renderer='../templates/mytemplate.mako')
class MenuViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):

        return {'one': "Test", 'project': 'Project'}

