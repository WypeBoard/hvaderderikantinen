<%inherit file="layout.mako"/>
<div class="panel-group container">
    % for index, week in enumerate(menu):
        <div class="card">
            <div class="card-header">
                <h4 class="panel-title text-center">
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#${week}"
                            aria-expanded="true" aria-controls="${week}">
                        Uge ${week[4:]} ${week[:4]}
                    </button>
                </h4>
            </div>
            <div id="${week}" class="${'in' if index == 0 else 'collapse' }">
                <div class="card-body">
                    <table class="table table-light">
                        <thead>
                        <th></th>
                        <th>Salat</th>
                        <th>Salat</th>
                        <th>Pålæg</th>
                        <th>Pålæg</th>
                        <th>Fisk</th>
                        <th>Varm mad</th>
                        </thead>
                        % for day in menu[week]:
                            <tr class="${'table-primary' if menu[week][day]['dato'] == today else ''}">
                                <td>${day}<br />${menu[week][day]['dato'][6:]}/${menu[week][day]['dato'][4:6]}</td>
                                % for item in menu[week][day]['retter']:
                                    <td>${menu[week][day]['retter'][item]}</td>
                                % endfor
                            </tr>
                        % endfor
                    </table>
                </div>
            </div>
        </div>
    % endfor
</div>