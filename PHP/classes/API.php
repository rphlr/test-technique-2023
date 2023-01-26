<?php

class API {
	public function getData() {
		// Initialisation de cURL
		$curl = curl_init();
		// Configuration des options cURL
		curl_setopt_array($curl, array(
		CURLOPT_URL => "http://localhost:8081/installations",
		CURLOPT_RETURNTRANSFER => true,
		CURLOPT_TIMEOUT => 30,
		CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
		CURLOPT_CUSTOMREQUEST => "GET",
		));
		// Envoi de la requête cURL
		$response = curl_exec($curl);
		// Fermeture de cURL
		curl_close($curl);
		// Renvoi de la réponse
		return $response;
	}
}


?>
