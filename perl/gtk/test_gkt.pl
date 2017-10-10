#!/usr/bin/perl

use strict;
use warnings;
use Glib;
use Gtk2 '-init';

my $window = Gtk2::Window->new();
my $button = Gtk2::Button->new('Hell World');

sub clean_and_exit {
    Gtk2->main_quit();
    exit(0);
}

$window->add($button);

$window->signal_connect(destroy => \&clean_and_exit);
$button->signal_connect(clicked => \&clean_and_exit);

$window->show_all();

Gtk2->main();
