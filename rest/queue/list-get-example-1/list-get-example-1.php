<?php
// Get the PHP helper library from twilio.com/docs/php/install
require_once('/path/to/twilio-php/Services/Twilio.php'); // Loads the library

// Your Account Sid and Auth Token from twilio.com/user/account
$sid = "AC5ef8732a3c49700934481addd5ce1659"; 
$token = "{{ auth_token }}"; 
$client = new Services_Twilio($sid, $token);

// Loop over the list of queues and echo a property for each one
foreach ($client->account->queues as $queue) {
    echo $queue->average_wait_time;
}