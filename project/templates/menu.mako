<%inherit file="layout.mako"/>
<div class="panel-group container">
    % for index, week in enumerate(menu):
        <div class="card">
            <div class="card-header">
                <h4 class="panel-title text-center">
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#${week}"
                            aria-expanded="true" aria-controls="${week}">
                        ${week}
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
                        <th>Varm mad</th>
                        </thead>
                        % for day in menu[week]:
                            <tr>
                                <td>${day}</td>
                                % for item in menu[week][day]:
                                    <td>${menu[week][day][item]}</td>
                                % endfor
                            </tr>
                        % endfor
                    </table>
                </div>

            </div>
        </div>
    % endfor
</div>