<?php

// echo"<pre>";
// var_dump($_POST);
// echo"</pre>";

// $kind = $_POST["kind"];
// $date = $_POST["date"];

$curl = curl_init();
$ACCESS_TOKEN = "x-access-token:ODZmYjJiYjNkYmE1YjEyMTE3MjU4YWJh";
$ACCOUNT_ID = "302010004343";

// CURLOPT_URL => `https://api.sunabar.gmo-aozora.com/personal/v1/accounts/{$kind}?dateFrom={$date}&accountId={$ACCOUNT_ID}`,
curl_setopt_array($curl, array(
    CURLOPT_URL => "https://api.sunabar.gmo-aozora.com/personal/v1/accounts/balances?accountId=302010004343",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "GET",
    CURLOPT_HTTPHEADER => array(
        "accept: application/json;charset=UTF-8",
        $ACCESS_TOKEN
    ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

$res =json_decode($response, true);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else { 
echo $response;

}