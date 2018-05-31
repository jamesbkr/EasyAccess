
variable "access_key" {
}

variable "secret_key" {
}

variable "region" {
  default  = "ap-south-1"
}

variable "vpc_name"{
  default = "vpcName"
}

variable "cidrblock"{
  default = "10.71.0.0/16"
}

variable "name" {
  default = "nameTheVPC"
}

variable "purpose" {
  default = "whyAreYouBuilding"
}

variable "owner" {
  default = "emailAddress"
}
