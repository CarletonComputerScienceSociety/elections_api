<?php
$key = $argv[1];
$iv = $argv[2];
$enc = $argv[3];

$plaintext=openssl_decrypt($enc, "aes-256-cbc", $key, $options=0, $iv);
echo $plaintext
?> 