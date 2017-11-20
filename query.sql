-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema SistemaEstacionamento
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SistemaEstacionamento
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SistemaEstacionamento` DEFAULT CHARACTER SET utf8 ;
USE `SistemaEstacionamento` ;

-- -----------------------------------------------------
-- Table `SistemaEstacionamento`.`Vaga`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SistemaEstacionamento`.`Vaga` (
  `idVaga` INT NOT NULL AUTO_INCREMENT,
  `nomeVaga` VARCHAR(45) NOT NULL,
  `valorPorVaga` FLOAT NOT NULL,
  `ocupada` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idVaga`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SistemaEstacionamento`.`UsoVaga`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SistemaEstacionamento`.`UsoVaga` (
  `idUsoVaga` INT NOT NULL,
  `horarioEntrada` DATETIME NOT NULL,
  `horarioSaida` DATETIME NOT NULL,
  `Vaga_idVaga` INT NOT NULL,
  PRIMARY KEY (`idUsoVaga`),
  INDEX `fk_UsoVaga_Vaga_idx` (`Vaga_idVaga` ASC),
  CONSTRAINT `fk_UsoVaga_Vaga`
    FOREIGN KEY (`Vaga_idVaga`)
    REFERENCES `SistemaEstacionamento`.`Vaga` (`idVaga`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
