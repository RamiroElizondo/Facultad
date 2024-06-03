-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `cuil` int DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `puntos` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,204484232,'Pepito','0'),(2,204498574,'Eduardo','200'),(3,204393242,'Ana ','100'),(4,203293282,'Ramon','0');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `cuil` int NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cuil`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES (204785967,'Facuendo','Mut'),(204875968,'Daniel','Ruiz'),(207654321,'Pedro','Garcia');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturacion`
--

DROP TABLE IF EXISTS `facturacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturacion` (
  `fecha` date DEFAULT NULL,
  `importe` double DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `facturas_numero` int NOT NULL,
  `productos_id` int NOT NULL,
  `empleados_cuil` int NOT NULL,
  `cliente_idCliente` int NOT NULL,
  PRIMARY KEY (`facturas_numero`,`productos_id`,`empleados_cuil`,`cliente_idCliente`),
  KEY `fk_facturacion_facturas1_idx` (`facturas_numero`),
  KEY `fk_facturacion_productos1_idx` (`productos_id`),
  KEY `fk_facturacion_empleados1_idx` (`empleados_cuil`),
  KEY `fk_facturacion_cliente1_idx` (`cliente_idCliente`),
  CONSTRAINT `fk_facturacion_cliente1` FOREIGN KEY (`cliente_idCliente`) REFERENCES `cliente` (`idCliente`),
  CONSTRAINT `fk_facturacion_empleados1` FOREIGN KEY (`empleados_cuil`) REFERENCES `empleados` (`cuil`),
  CONSTRAINT `fk_facturacion_facturas1` FOREIGN KEY (`facturas_numero`) REFERENCES `facturas` (`numero`),
  CONSTRAINT `fk_facturacion_productos1` FOREIGN KEY (`productos_id`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturacion`
--

LOCK TABLES `facturacion` WRITE;
/*!40000 ALTER TABLE `facturacion` DISABLE KEYS */;
INSERT INTO `facturacion` VALUES ('2023-06-22',1920,2,1,1,204785967,2),('2023-06-24',19200,20,1,1,204875968,2),('2023-06-22',3840,4,2,1,204785967,2),('2023-06-22',2400,2,3,2,204785967,2),('2023-06-22',24000,4,4,3,207654321,2),('2023-06-24',19200,20,16,1,204875968,2),('2023-06-24',9600,10,17,1,204875968,3);
/*!40000 ALTER TABLE `facturacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas`
--

DROP TABLE IF EXISTS `facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturas` (
  `numero` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`numero`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas`
--

LOCK TABLES `facturas` WRITE;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
INSERT INTO `facturas` VALUES (1,'A'),(2,'A'),(3,'A'),(4,'A'),(5,'A'),(6,'A'),(7,'A'),(8,'A'),(9,'A'),(13,'A'),(16,'A'),(17,'A');
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `cantidad` varchar(45) DEFAULT NULL,
  `marca` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Leche',960,'50','Sancor'),(2,'Cerveza',1200,'200','Schneider'),(3,'Pañales',7000,'110','Pampers'),(4,'Chocolates',360,'50','Block'),(5,'Yogur',480,'100','SERENISIMA'),(14,'Electronica',200000,'10','Samsung'),(15,'Electronica',320000,'5','Motorola');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provee`
--

DROP TABLE IF EXISTS `provee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provee` (
  `numT` int NOT NULL,
  `proveedores_cuil` int NOT NULL,
  `productos_id` int NOT NULL,
  `cantidadP` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `precioP` int DEFAULT NULL,
  PRIMARY KEY (`numT`,`proveedores_cuil`,`productos_id`),
  KEY `fk_proveedores_has_productos_productos1_idx` (`productos_id`),
  KEY `fk_proveedores_has_productos_proveedores1_idx` (`proveedores_cuil`),
  CONSTRAINT `fk_proveedores_has_productos_productos1` FOREIGN KEY (`productos_id`) REFERENCES `productos` (`id`),
  CONSTRAINT `fk_proveedores_has_productos_proveedores1` FOREIGN KEY (`proveedores_cuil`) REFERENCES `proveedores` (`cuil`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provee`
--

LOCK TABLES `provee` WRITE;
/*!40000 ALTER TABLE `provee` DISABLE KEYS */;
INSERT INTO `provee` VALUES (1,208765432,14,10,'2023-06-24',166667),(2,206543210,4,50,'2023-06-22',300),(3,201234567,1,100,'2023-06-22',800),(4,201234567,5,100,'2023-06-22',400),(5,209876543,3,100,'2023-06-22',5000),(6,202345678,2,200,'2023-06-22',1000),(7,205678943,3,10,'2023-06-24',5833);
/*!40000 ALTER TABLE `provee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `cuil` int NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `empresa` varchar(45) DEFAULT NULL,
  `provee` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cuil`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (201234567,'Daniel','Sanchez','Cabral','Lacteos'),(202345678,'Fabricio','Rubio','Quilmes','BebidaConA'),(203456789,'Luis','Rodriguez','Motorola','Electronica'),(205678943,'Antonella','Garcia','Pampers','ArtBebe'),(206543210,'Juan','Perez','Arcor','Chocolates'),(208765432,'Octavio','Garello','Samsung','Electronica'),(209876543,'Federico','Garello','Coca Cola','BebidadSinA');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-25 22:39:42
