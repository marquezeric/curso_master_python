-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: crm1
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `accounts_customer`
--

DROP TABLE IF EXISTS `accounts_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `phone` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `email` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customer`
--

LOCK TABLES `accounts_customer` WRITE;
/*!40000 ALTER TABLE `accounts_customer` DISABLE KEYS */;
INSERT INTO `accounts_customer` VALUES (1,'Juan Rivera Saucedo','5551234567','jrivera@gmail.com','2022-01-26 23:03:44.384943'),(2,'Ricardo Torres Torres','5551234568','rtorres@gmail.com','2022-02-16 23:05:13.347838'),(3,'Ricardo Buendía Palmerín','5551234569','rbuendia@gmail.com','2022-02-17 18:30:11.538200'),(4,'Elmer Meza Peña','5551234561','emeza@gmail.com','2022-02-17 18:30:50.050919');
/*!40000 ALTER TABLE `accounts_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_order`
--

DROP TABLE IF EXISTS `accounts_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_created` datetime(6) DEFAULT NULL,
  `status` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_order_customer_id_23c59287_fk_accounts_customer_id` (`customer_id`),
  KEY `accounts_order_product_id_83d789e2_fk_accounts_product_id` (`product_id`),
  CONSTRAINT `accounts_order_customer_id_23c59287_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `accounts_order_product_id_83d789e2_fk_accounts_product_id` FOREIGN KEY (`product_id`) REFERENCES `accounts_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_order`
--

LOCK TABLES `accounts_order` WRITE;
/*!40000 ALTER TABLE `accounts_order` DISABLE KEYS */;
INSERT INTO `accounts_order` VALUES (1,'2022-02-16 23:50:10.281871','Pending',1,3),(2,'2022-02-16 23:51:13.110247','Pending',1,1),(3,'2022-02-16 23:51:30.531006','Pending',2,2),(9,'2022-03-04 00:26:00.581470','Out for delivery',3,2),(10,'2022-03-04 00:26:09.058271','Pending',3,2),(11,'2022-03-04 00:26:33.175341','Out for delivery',4,3);
/*!40000 ALTER TABLE `accounts_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_product`
--

DROP TABLE IF EXISTS `accounts_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `price` double DEFAULT NULL,
  `category` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `desciption` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `name` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_product`
--

LOCK TABLES `accounts_product` WRITE;
/*!40000 ALTER TABLE `accounts_product` DISABLE KEYS */;
INSERT INTO `accounts_product` VALUES (1,200,'Out Door',NULL,'2022-02-16 23:40:07.492752','BBQ Grill'),(2,50,'Indoor',NULL,'2022-02-16 23:40:50.525171','Dishes'),(3,3,'Out Door',NULL,'2022-02-16 23:49:30.584460','Ball');
/*!40000 ALTER TABLE `accounts_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_product_tags`
--

DROP TABLE IF EXISTS `accounts_product_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_product_tags` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_product_tags_product_id_tag_id_f558f1ef_uniq` (`product_id`,`tag_id`),
  KEY `accounts_product_tags_tag_id_f4ba4ec3_fk_accounts_tag_id` (`tag_id`),
  CONSTRAINT `accounts_product_tags_product_id_2d1c4b64_fk_accounts_product_id` FOREIGN KEY (`product_id`) REFERENCES `accounts_product` (`id`),
  CONSTRAINT `accounts_product_tags_tag_id_f4ba4ec3_fk_accounts_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `accounts_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_product_tags`
--

LOCK TABLES `accounts_product_tags` WRITE;
/*!40000 ALTER TABLE `accounts_product_tags` DISABLE KEYS */;
INSERT INTO `accounts_product_tags` VALUES (1,1,2),(2,1,3),(3,2,3),(4,3,1),(5,3,2);
/*!40000 ALTER TABLE `accounts_product_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_tag`
--

DROP TABLE IF EXISTS `accounts_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_tag`
--

LOCK TABLES `accounts_tag` WRITE;
/*!40000 ALTER TABLE `accounts_tag` DISABLE KEYS */;
INSERT INTO `accounts_tag` VALUES (1,'Sports'),(2,'Summer'),(3,'Kitchen');
/*!40000 ALTER TABLE `accounts_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add customer',7,'add_customer'),(26,'Can change customer',7,'change_customer'),(27,'Can delete customer',7,'delete_customer'),(28,'Can view customer',7,'view_customer'),(29,'Can add order',8,'add_order'),(30,'Can change order',8,'change_order'),(31,'Can delete order',8,'delete_order'),(32,'Can view order',8,'view_order'),(33,'Can add product',9,'add_product'),(34,'Can change product',9,'change_product'),(35,'Can delete product',9,'delete_product'),(36,'Can view product',9,'view_product'),(37,'Can add tag',10,'add_tag'),(38,'Can change tag',10,'change_tag'),(39,'Can delete tag',10,'delete_tag'),(40,'Can view tag',10,'view_tag');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$CaYcOrDb4XLp$z8rDQAJCm1Lug86RHs3IWxUtu5lfB/XTRHr6BDIfr20=','2022-03-03 19:14:57.310521',1,'emarquez','Eric','Marquez','idsemarquez@gmail.com',1,1,'2022-01-26 22:09:45.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_spanish_ci,
  `object_repr` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-01-26 22:11:29.007862','1','emarquez',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),(2,'2022-01-26 23:03:44.390600','1','Customer object (1)',1,'[{\"added\": {}}]',7,1),(3,'2022-02-16 23:04:32.048085','1','Juan Rivera Saucedo',2,'[{\"changed\": {\"fields\": [\"Name\", \"Phone\", \"Email\"]}}]',7,1),(4,'2022-02-16 23:05:13.403159','2','Ricardo Torres Torres',1,'[{\"added\": {}}]',7,1),(5,'2022-02-16 23:06:02.940178','1','Sports',1,'[{\"added\": {}}]',10,1),(6,'2022-02-16 23:06:12.391204','2','Summer',1,'[{\"added\": {}}]',10,1),(7,'2022-02-16 23:06:39.040110','3','Kitchen',1,'[{\"added\": {}}]',10,1),(8,'2022-02-16 23:40:07.509819','1','BBQ Grill',1,'[{\"added\": {}}]',9,1),(9,'2022-02-16 23:40:50.540113','2','Dishes',1,'[{\"added\": {}}]',9,1),(10,'2022-02-16 23:49:30.598867','3','Ball',1,'[{\"added\": {}}]',9,1),(11,'2022-02-16 23:50:10.289030','1','Order object (1)',1,'[{\"added\": {}}]',8,1),(12,'2022-02-16 23:51:13.166644','2','Order object (2)',1,'[{\"added\": {}}]',8,1),(13,'2022-02-16 23:51:30.535334','3','Order object (3)',1,'[{\"added\": {}}]',8,1),(14,'2022-02-17 18:30:11.545254','3','Ricardo Buendía Palmerín',1,'[{\"added\": {}}]',7,1),(15,'2022-02-17 18:30:50.054915','4','Elmer Meza Peña',1,'[{\"added\": {}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'accounts','customer'),(8,'accounts','order'),(9,'accounts','product'),(10,'accounts','tag'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-01-26 16:22:18.586831'),(2,'auth','0001_initial','2022-01-26 16:22:19.016818'),(3,'admin','0001_initial','2022-01-26 16:22:20.172389'),(4,'admin','0002_logentry_remove_auto_add','2022-01-26 16:22:20.448887'),(5,'admin','0003_logentry_add_action_flag_choices','2022-01-26 16:22:20.476072'),(6,'contenttypes','0002_remove_content_type_name','2022-01-26 16:22:20.749821'),(7,'auth','0002_alter_permission_name_max_length','2022-01-26 16:22:20.921805'),(8,'auth','0003_alter_user_email_max_length','2022-01-26 16:22:21.145961'),(9,'auth','0004_alter_user_username_opts','2022-01-26 16:22:21.170586'),(10,'auth','0005_alter_user_last_login_null','2022-01-26 16:22:21.297784'),(11,'auth','0006_require_contenttypes_0002','2022-01-26 16:22:21.306774'),(12,'auth','0007_alter_validators_add_error_messages','2022-01-26 16:22:21.331168'),(13,'auth','0008_alter_user_username_max_length','2022-01-26 16:22:21.483575'),(14,'auth','0009_alter_user_last_name_max_length','2022-01-26 16:22:21.673232'),(15,'auth','0010_alter_group_name_max_length','2022-01-26 16:22:21.831287'),(16,'auth','0011_update_proxy_permissions','2022-01-26 16:22:21.855459'),(17,'auth','0012_alter_user_first_name_max_length','2022-01-26 16:22:22.048099'),(18,'sessions','0001_initial','2022-01-26 16:22:22.077103'),(19,'accounts','0001_initial','2022-01-26 22:16:10.577031'),(20,'accounts','0002_order_product','2022-01-26 23:26:55.475755'),(21,'accounts','0003_auto_20220214_0909','2022-02-14 15:09:15.798079'),(22,'accounts','0004_auto_20220216_1651','2022-02-16 22:51:37.263376'),(23,'accounts','0005_auto_20220216_1701','2022-02-16 23:02:29.813622'),(24,'accounts','0006_auto_20220216_1738','2022-02-16 23:38:29.327652');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('eamriw5xczgl9cv9jz0qlr6w0ib5uafa','.eJxVjDsOwyAQBe9CHSGzrPikTJ8zoAWW4CTCkrErK3ePLblI2pl5bxOB1qWGtfMcxiyuQonLL4uUXtwOkZ_UHpNMU1vmMcojkaft8j5lft_O9u-gUq_7etCMmAjJgVPRO0AyHsCq5MEYHUHvmKIHBNaDZ4eWU_HF5mg0FRafL7uBN3k:1nKTCC:yScnZ2QWdjeHWrd18GNXfqgVa6zYaHwELEWjbZF-9Vw','2022-03-02 22:54:48.042841'),('fdsqwzwi3qj732cs9ec9w36qz2wbusea','.eJxVjDsOwyAQBe9CHSGzrPikTJ8zoAWW4CTCkrErK3ePLblI2pl5bxOB1qWGtfMcxiyuQonLL4uUXtwOkZ_UHpNMU1vmMcojkaft8j5lft_O9u-gUq_7etCMmAjJgVPRO0AyHsCq5MEYHUHvmKIHBNaDZ4eWU_HF5mg0FRafL7uBN3k:1nPquf:_HTqfimIevtjtcwBN-e-BRP_9W7urHUHmRwNXbqWlGg','2022-03-17 19:14:57.320099'),('ksfxq0mbbgr83m978zpjiv4mjcc7nqdu','.eJxVjDsOwyAQBe9CHSGzrPikTJ8zoAWW4CTCkrErK3ePLblI2pl5bxOB1qWGtfMcxiyuQonLL4uUXtwOkZ_UHpNMU1vmMcojkaft8j5lft_O9u-gUq_7etCMmAjJgVPRO0AyHsCq5MEYHUHvmKIHBNaDZ4eWU_HF5mg0FRafL7uBN3k:1nCrIW:VdD8fRpkBjqwWHoJbhPNI5gyqttDOKKjoEtCNtu9RFU','2022-02-09 23:01:52.369032'),('yabxmmeqlxv1dix124ofobkdizw3j2uq','.eJxVjDsOwyAQBe9CHSGzrPikTJ8zoAWW4CTCkrErK3ePLblI2pl5bxOB1qWGtfMcxiyuQonLL4uUXtwOkZ_UHpNMU1vmMcojkaft8j5lft_O9u-gUq_7etCMmAjJgVPRO0AyHsCq5MEYHUHvmKIHBNaDZ4eWU_HF5mg0FRafL7uBN3k:1nO9ot:8LA5kHA5vcySln34tI2OtlsCOPt0VUNLvXsXyrgaQQE','2022-03-13 03:01:59.904852'),('zpqtt57odlahvxp7ru9gnstm8m5mqosx','.eJxVjDsOwyAQBe9CHSGzrPikTJ8zoAWW4CTCkrErK3ePLblI2pl5bxOB1qWGtfMcxiyuQonLL4uUXtwOkZ_UHpNMU1vmMcojkaft8j5lft_O9u-gUq_7etCMmAjJgVPRO0AyHsCq5MEYHUHvmKIHBNaDZ4eWU_HF5mg0FRafL7uBN3k:1nKlWy:4BowsQadm5h9BS0CG0WK_P3ZiZk2SexaZCYafJ20zJ8','2022-03-03 18:29:28.890845');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-07 23:49:45
