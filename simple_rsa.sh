#!/bin/bash


openssl genrsa 128 > my.key

openssl rsa -inform PEM -text -noout < my.key

openssl rsa -pubout -in my.key > my.pub

openssl rsa -inform PEM -text -noout -pubin < my.pub

cat my.pub
