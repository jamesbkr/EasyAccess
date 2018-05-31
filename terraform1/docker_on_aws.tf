provider "aws"{
access_key = "${var.access_key}"
secret_key = "${var.secret_key}"
region = "${var.region}"

}

resource "aws_vpc" "vpc1" {

cidr_block = "${var.cidrblock}"
tags {
Name = "${var.name}"
Owner = "${var.owner}"
Purpose = "${var.purpose}"
}
}
