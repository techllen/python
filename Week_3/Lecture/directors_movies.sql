-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema directors_movies_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema directors_movies_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `directors_movies_schema` DEFAULT CHARACTER SET utf8 ;
USE `directors_movies_schema` ;

-- -----------------------------------------------------
-- Table `directors_movies_schema`.`directors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `directors_movies_schema`.`directors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `birthdate` DATETIME NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `directors_movies_schema`.`movies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `directors_movies_schema`.`movies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `genre` VARCHAR(255) NULL,
  `title` VARCHAR(255) NULL,
  `release_date` DATE NULL,
  `box_office` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_atl` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `director_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_movies_directors_idx` (`director_id` ASC) VISIBLE,
  CONSTRAINT `fk_movies_directors`
    FOREIGN KEY (`director_id`)
    REFERENCES `directors_movies_schema`.`directors` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `directors_movies_schema`.`performers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `directors_movies_schema`.`performers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `birthdate` DATETIME NULL,
  `current_city` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `directors_movies_schema`.`movies_has_performers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `directors_movies_schema`.`movies_has_performers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `movie_id` INT NOT NULL,
  `performer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_movies_has_performers_movies1_idx` (`movie_id` ASC) VISIBLE,
  INDEX `fk_movies_has_performers_performers1_idx` (`performer_id` ASC) VISIBLE,
  CONSTRAINT `fk_movies_has_performers_movies1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `directors_movies_schema`.`movies` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movies_has_performers_performers1`
    FOREIGN KEY (`performer_id`)
    REFERENCES `directors_movies_schema`.`performers` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
