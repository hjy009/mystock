DROP TABLE IF EXISTS `stock_base`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stock_base` (
  `ts_code` varchar(45) NOT NULL,
  `symbol` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `area` varchar(45) DEFAULT NULL,
  `industry` varchar(45) DEFAULT NULL,
  `curr_type` varchar(45) DEFAULT NULL,
  `list_status` varchar(45) DEFAULT NULL,
  `list_date` varchar(45) DEFAULT NULL,
  `delist_date` varchar(45) DEFAULT NULL,
  `is_hs` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ts_code`,`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


