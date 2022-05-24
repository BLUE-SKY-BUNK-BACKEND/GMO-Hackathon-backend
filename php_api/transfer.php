<?php

$curl = curl_init();
// 2&  &nextItemKey=1234567890&requestTransferStatus=20&requestTransferTerm=1
curl_setopt_array($curl, array(
    CURLOPT_URL => "https://api.sunabar.gmo-aozora.com/personal/v1/transfer/status?accountId=302010004343&queryKeyClass=2&dateFrom=2022-03-20&dateTo=2022-05-24",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "GET",
    CURLOPT_HTTPHEADER => array(
        "accept: application/json;charset=UTF-8",
        "x-access-token: ODZmYjJiYjNkYmE1YjEyMTE3MjU4YWJh"
    ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}