// Récupération des données depuis l'API
$.getJSON("classes/API.php", function (data) {
	// Transformation des données en format compatible avec echarts.min.js
	var labels = [];
	var capacites = [];
	for (var i = 0; i < data.length; i++) {
		labels.push(data[i].nom);
		capacites.push(data[i].capacite);
	}

	// Initialisation des graphes
	var barChart = echarts.init(document.getElementById('bar-chart'));
	var pieChart = echarts.init(document.getElementById('pie-chart'));

	// Configuration des options pour le graphe en barres
	var barOptions = {
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
	};

	// Configuration des options pour le graphe en camembert
	var pieOptions = {
		series: [{
			data: capacites,
			type: 'pie'
		}]
	};

	// Appliquer les options aux graphes et les afficher
	barChart.setOption(barOptions);
	pieChart.setOption(pieOptions);
});
