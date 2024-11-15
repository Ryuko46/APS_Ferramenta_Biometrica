-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: banco
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `nivel_acesso` int DEFAULT NULL,
  `features` varchar(8000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (8,'oi','oi',1,'[3045153210000, 3045153209744, 3045153210192, 3045153209808, 3045153209936, 3045153210128, 3045153325520, 3045153325840, 3045153325264, 3045153210320, 3045153325328, 3045153325776, 3045153325456, 3045153326352, 3045153326032, 3045153326224, 3045153326608, 3045153326480, 3045153325968, 3045153325584, 3045153326864, 3045153326736, 3045153326800, 3045153327056, 3045153327376, 3045153327248, 3047147142928, 3047167672784, 3047166209872, 3047161942160, 3047161938192, 3047166327248, 3045153161424, 3045153051088, 3045153161488, 3047159253968, 3047166314256, 3045153206160, 3045153205712, 3045153205968, 3045153206544, 3045153206352, 3045153205584, 3045153207056, 3045153204048, 3045153206288, 3045153205904, 3045153200464, 3045153204496, 3045153207440, 3045153203920, 3045153204432, 3045153203728, 3045153204176, 3045153203664, 3045153203344, 3045153200784, 3045153207888, 3045153204240, 3045153207824, 3045153203536, 3045153201424, 3045153202128, 3045153202704, 3045153200400, 3045153204112, 3045153208464, 3045153208592, 3045153200336, 3045153201232, 3045153208400, 3045153208784, 3045153204880, 3045153204944, 3045153204368, 3045153204752, 3045153204816, 3045153205072, 3045153208272, 3045153209168, 3045153205456, 3045153205392, 3045153436112, 3045153205136, 3045153436176, 3045153436496, 3045153436048, 3045153436688, 3045153436560, 3045153435856, 3045153435984, 3045153437136, 3045153437328, 3045153436304, 3045153437392, 3045153437456, 3045153436944, 3045153437840, 3045153438224, 3045153437968, 3045153438288, 3045153438352, 3045153438672, 3045153438800, 3045153438864, 3045153439056, 3045153437520, 3045153437712, 3045153439120, 3045153439312, 3045153438544, 3045153439696, 3045153439248, 3045153439440, 3045153538512, 3045153538640, 3045153538192, 3045153539024, 3045153538576, 3045153538384, 3045153539344, 3045153539408, 3045153539216, 3045153538768, 3045153539856, 3045153539280, 3045153539920, 3045153539984, 3045153540496, 3045153540048, 3045153540240, 3045153540112, 3045153540688, 3045153540880, 3045153540944, 3045153541136, 3045153541328, 3045153540560]'),(9,'tchau','tchau',1,'[3047166211856, 3047166210640, 3047166211728, 3045153243344, 3045153243216, 3045153243408, 3045153244176, 3045153244112, 3045153243920, 3045153243600, 3045153243728, 3045153244496, 3045153243984, 3045153244688, 3045153244752, 3045153244880, 3045153244944, 3045153245456, 3045153244560, 3045153243536, 3045153245072, 3045153245264, 3045153245520, 3045153245136, 3045153246032, 3045153245648, 3045153434960, 3047158863312, 3047162627024, 3045153056720, 3047169021136, 3047162122128, 3047162122448, 3045153055504, 3047166080528, 3047169019600, 3047166079824, 3047166081040, 3047166079760, 3047166322704, 3047166314256, 3047166321168, 3047166327248, 3047166211664, 3047166209808, 3047166326928, 3047166322960, 3047166314384, 3047166318480, 3047166323984, 3047166319504, 3045153201232, 3045153200336, 3045153204304, 3045153209744, 3045153200976, 3045153208208, 3045153204560, 3045153201680, 3045153209808, 3045153210128, 3045153204624, 3045153202768, 3045153210320, 3045153204944, 3045153204688, 3045153205712, 3045153209936, 3045153208592, 3045153206480, 3045153206544, 3045153208784, 3045153208400, 3045153206352, 3045153210192, 3045153204752, 3045153204880, 3045153204368, 3045153209424, 3045153204816, 3045153206928, 3045153206736, 3045153209168, 3045153205072, 3045153207120, 3045153205136, 3045153199952, 3045153209552, 3045153207248, 3045153206288, 3045153205456, 3045153202832, 3045153203664, 3045153205392, 3045153207696, 3045153203344, 3045153204432, 3045153204240, 3045153201424, 3045153207824, 3045153203600, 3045153202128, 3045153208080, 3045153202256, 3045153208464, 3045153203216, 3045153203088, 3045153207312, 3045153546256, 3045153546384, 3045153546192, 3045153546896, 3045153546832, 3045153546640, 3045153547216, 3045153547344, 3045153546960, 3045153547728, 3045153547280, 3045153547088, 3045153548048, 3045153548112, 3045153547920, 3045153547472, 3045153548560, 3045153547984, 3045153548624, 3045153548688, 3045153549200, 3045153548752, 3045153548944, 3045153548816, 3045153549392, 3045153549584, 3045153549648, 3045153549840, 3045153550032, 3045153549264]');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-15 15:36:35
