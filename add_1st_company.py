use strict;
use warnings;
use Time::HiRes qw(sleep);
use Test::WWW::Selenium;
use Test::More "no_plan";
use Test::Exception;

my $sel = Test::WWW::Selenium->new( host => "localhost", 
                                    port => 4444, 
                                    browser => "*chrome", 
                                    browser_url => "http://change-this-to-the-site-you-are-testing/" );

$sel->open_ok("/main_app");
$sel->click_ok("link=Add Companies");
$sel->wait_for_page_to_load_ok("30000");
$sel->type_ok("id_name", "Company Inc");
$sel->type_ok("id_street", "123 Main Street");
$sel->type_ok("id_city", "Boston");
$sel->type_ok("id_state", "MA");
$sel->type_ok("id_zip_code", "02147");
$sel->type_ok("id_country", "USA");
$sel->type_ok("id_phone", "617-000-0000");
$sel->type_ok("id_fax", "617-000-0000");
$sel->type_ok("id_industry", "0");
$sel->type_ok("id_description", "Decription of Company Inc.");
$sel->click_ok("//input[\@value='submit']");
$sel->wait_for_page_to_load_ok("30000");
