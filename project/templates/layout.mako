<!DOCTYPE html>
<html lang="{{ '${request.locale_name}' }}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('project:static/pyramid-16x16.png')}">

    <title>Hvad er der i kaninen? | Netcompany Aalborg</title>

    <!-- Bootstrap core CSS -->
    <link href="${request.static_url('project:static/css/bootstrap.min.css')}" rel="stylesheet">

    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('project:static/css/style.css')}" rel="stylesheet">
</head>
<body>

    ${self.body()}


<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="//oss.maxcdn.com/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/js/bootstrap.min.js"></script>
</body>
</html>
