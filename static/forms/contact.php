<?php 
/*
  /**
  * Requires the "PHP Email Form" library
  * The "PHP Email Form" library is available only in the pro version of the template
  * The library should be uploaded to: vendor/php-email-form/php-email-form.php
  * For more info and help: https://bootstrapmade.com/php-email-form/
  */

  // Replace contact@example.com with your real receiving email address
  /*
  $receiving_email_address = 'sheikhrizvan.test@gmail.com';

  if( file_exists($php_email_form = '../assets/vendor/php-email-form/php-email-form.php' )) {
    include( $php_email_form );
  } else {
    die( 'Unable to load the "PHP Email Form" Library!');
  }

  $contact = new PHP_Email_Form;
  $contact->ajax = true;
  
  $contact->to = $receiving_email_address;
  $contact->from_name = $_POST['name'];
  $contact->from_email = $_POST['email'];
  $contact->subject = $_POST['subject'];

  // Uncomment below code if you want to use SMTP to send emails. You need to enter your correct SMTP credentials
  
  $contact->smtp = array(
    'host' => 'gmail.com',
    'username' => 'sheikhrizvan.test',
    'password' => 'Passw0rd@123',
    'port' => '587'
  );
  

  $contact->add_message( $_POST['name'], 'From');
  $contact->add_message( $_POST['email'], 'Email');
  $contact->add_message( $_POST['message'], 'Message', 10);

  echo $contact->send();
  */


$error = "";
$success = "";
if (isset($_POST)) {
  $emailTo = "sheikhrizvan@gmail.com";
  $subject = $_POST["subject"];
  $body = $_POST["message"];
  $header = "From: ".$_POST["email"];

  if(mail($emailTo,$subject,$body,$header)){
    $success = "<p>The email sent successfully</p>";
  }else{
    $error = "<p>Unable to send email..</p>";
  }
}


?>
