<!doctype html>
<html lang="en">

<head>
	<title>Test Technique - {Nom du candidat}</title>
	<meta charset="utf-8">

	<link rel="stylesheet" href="css/custom.css">
	<script src="js/jquery.min.js"></script>
	<script src="js/echarts.min.js"></script>
	<script src="js/custom.js"></script>
</head>

<body>
	<span style="float: right;"><i>Version de l'API : v1.0.0</i></span>
	<h1>Installations photovoltaïques</h1>
	<div id="barChart" style="width: 49%; display: inline-block; text-align: center; vertical-align: top;">
		<h2>Installations par année</h2>
	</div>
	<div id="pieChart" style="width: 49%; display: inline-block; text-align: center; vertical-align: top;">
		<h2>Répartition des capacités par propriétaire</h2>
	</div>
	<div style="width: 100%; display: inline-block; text-align: center; vertical-align: top;">
		<h2>Liste des installations</h2>
		<table id="table" style="width: 50%; margin: auto;">
			<thead>
				<tr>
					<td>Install 1</td>
					<td>Commune</td>
					<td>Capacité</td>
					<td>Propriétaire</td>
				</tr>
			</thead>
			<thead>
				<tr>
					<td>Install 2</td>
					<td>Commune</td>
					<td>Capacité</td>
					<td>Propriétaire</td>
				</tr>
			</thead>
		</table>
	</div>
	<script>
		var api = new API();
		var data = JSON.parse(api.getData());

		// Utiliser les données pour afficher les graphes et les entrées dans le tableau
		// Pour le graphique en barres
		var labels = [];
		var capacites = [];
		for (var i = 0; i < data.length; i++) {
			labels.push(data[i].nom);
			capacites.push(data[i].capacite);
		}

		var barChart = echarts.init(document.getElementById("barChart"));
		barChart.setOption({
			xAxis: {
				type: 'category',
				data: labels
			},
			yAxis: {
				type: 'value'
			},
			series: [{
				data: capacites,
				type: 'bar'
			}]
		});

		// Pour le graphique en camembert
		var proprietaires = {};
		for (var i = 0; i < data.length; i++) {
			if (!proprietaires[data[i].proprietaire]) {
				proprietaires[data[i].proprietaire] = 0;
			}
			proprietaires[data[i].proprietaire] += data[i].capacite;
		}

		var pieChart = echarts.init(document.getElementById("pieChart"));
		pieChart.setOption({
			series: [
				{
					name: 'Capacité (en kW)',
					type: 'pie',
					data: Object.entries(proprietaires).map(function (item) {
						return { name: item[0], value: item[1] };
					})
				}
			]
		});

		// Pour le tableau
		var table = $("table");
		for (var i = 0; i < data.length; i++) {
			var row = "<tr><td>" + data[i].nom + "</td><td>" + data[i].commune + "</td><td>" + data[i].capacite + "</td><td>" + data[i].proprietaire + "</td></tr>";
			table.append(row);
		}
	</script>
</body>

</html>