create database mmt_backend_test;

CREATE TABLE `mmt_backend_test`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(32) NOT NULL,
  `gender` ENUM('MALE', 'FEMALE', 'OTHER') NOT NULL,
  PRIMARY KEY (`id`));