-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: nekko
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add single msg board',1,'add_singlemsgboard'),(2,'Can change single msg board',1,'change_singlemsgboard'),(3,'Can delete single msg board',1,'delete_singlemsgboard'),(4,'Can add userinfo',2,'add_userinfo'),(5,'Can change userinfo',2,'change_userinfo'),(6,'Can delete userinfo',2,'delete_userinfo'),(7,'Can add choice',3,'add_choice'),(8,'Can change choice',3,'change_choice'),(9,'Can delete choice',3,'delete_choice'),(10,'Can add article',4,'add_article'),(11,'Can change article',4,'change_article'),(12,'Can delete article',4,'delete_article'),(13,'Can add question',5,'add_question'),(14,'Can change question',5,'change_question'),(15,'Can delete question',5,'delete_question'),(16,'Can add log entry',6,'add_logentry'),(17,'Can change log entry',6,'change_logentry'),(18,'Can delete log entry',6,'delete_logentry'),(19,'Can add group',7,'add_group'),(20,'Can change group',7,'change_group'),(21,'Can delete group',7,'delete_group'),(22,'Can add permission',8,'add_permission'),(23,'Can change permission',8,'change_permission'),(24,'Can delete permission',8,'delete_permission'),(25,'Can add user',9,'add_user'),(26,'Can change user',9,'change_user'),(27,'Can delete user',9,'delete_user'),(28,'Can add content type',10,'add_contenttype'),(29,'Can change content type',10,'change_contenttype'),(30,'Can delete content type',10,'delete_contenttype'),(31,'Can add session',11,'add_session'),(32,'Can change session',11,'change_session'),(33,'Can delete session',11,'delete_session'),(34,'Can add like me data',12,'add_likemedata'),(35,'Can change like me data',12,'change_likemedata'),(36,'Can delete like me data',12,'delete_likemedata');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'admin','logentry'),(7,'auth','group'),(8,'auth','permission'),(9,'auth','user'),(10,'contenttypes','contenttype'),(4,'polls','article'),(3,'polls','choice'),(12,'polls','likemedata'),(5,'polls','question'),(1,'polls','singlemsgboard'),(2,'polls','userinfo'),(11,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-02-07 03:05:23.333087'),(2,'auth','0001_initial','2018-02-07 03:05:25.739129'),(3,'admin','0001_initial','2018-02-07 03:05:26.238395'),(4,'admin','0002_logentry_remove_auto_add','2018-02-07 03:05:26.295067'),(5,'contenttypes','0002_remove_content_type_name','2018-02-07 03:05:26.584799'),(6,'auth','0002_alter_permission_name_max_length','2018-02-07 03:05:26.792205'),(7,'auth','0003_alter_user_email_max_length','2018-02-07 03:05:27.006977'),(8,'auth','0004_alter_user_username_opts','2018-02-07 03:05:27.031395'),(9,'auth','0005_alter_user_last_login_null','2018-02-07 03:05:27.186427'),(10,'auth','0006_require_contenttypes_0002','2018-02-07 03:05:27.197905'),(11,'auth','0007_alter_validators_add_error_messages','2018-02-07 03:05:27.223363'),(12,'auth','0008_alter_user_username_max_length','2018-02-07 03:05:27.445337'),(13,'polls','0001_initial','2018-02-07 03:05:28.243272'),(14,'sessions','0001_initial','2018-02-07 03:05:28.394500'),(15,'auth','0009_alter_user_last_name_max_length','2018-03-25 21:40:04.255878'),(16,'polls','0002_auto_20180303_2003','2018-03-25 21:40:04.539724'),(17,'polls','0003_likemedata','2018-03-25 21:40:04.653670'),(18,'polls','0004_article_is_exist','2018-03-25 21:40:04.845582');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0ltd52xo1maiqncztje2te2lrxxeahua','MTkxYjU3OTcwYThmOTU0ZjZiNTIzMGE1YWQwZGU4YmFlOGNlNjI1MTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzEucG5nIn0=','2018-02-21 16:13:25.083208'),('10gv3ylz3rqh2zuy54o3u6ycefhpe6rw','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-12-23 20:22:03.032945'),('18j3213q8ubs1xh1wrrmx4kdfulfm2pn','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2019-07-14 10:41:45.102369'),('2b9y95f2iosnqjyqlc4a0ygrubbbnhlg','MWQxYmM2MTFiYWU0YzUyYTg2NTkyOWRhMWNkNjFjYTIwOGYxY2NhOTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci8xMy5wbmciLCJ1c2VySWQiOjEzfQ==','2018-06-17 19:06:19.435506'),('40vufdvh2nx53rw7hdnkdn81ci3ugugz','OTExZDE5YThhOTg5ZjFkM2Q0OTRiNjRjNTJmN2I4N2FmYWNkZWJjOTp7InVzZXJJZCI6MywiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzMucG5nIn0=','2018-02-21 21:14:24.030859'),('4rmis1rtwe6oikp4ssf0hq6acgk9kvnk','NzZmYWE4ZjYxYzQ1MzEzNTllNDdkNWNkYmVkODExZDE3NWZmYTMwNDp7InVzZXJJZCI6MTUsImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci9naXRodWIyNi5wbmcifQ==','2019-01-08 23:18:50.601179'),('5z23irksqkcnhd7e5ddlb9j6bdhnm304','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-12-08 19:57:53.591909'),('5z3o8eea7hm0m3rnrf1mg4lt3ouzgdwn','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2019-04-14 05:54:58.666378'),('6gw8feejnzbctpe3sp3la7emy445ontw','MWMxMTY1ZDgzMzMxM2E2NjNhODkzOWNmOGQ3Mjg5YzRjODVkZGE1Mjp7InVzZXJJZCI6MTcsImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci9naXRodWIyMi5wbmcifQ==','2019-06-05 13:24:46.843313'),('6rx3i431090j0wmmp0ualoipd8wp7mw3','ZmZjMWJiNDc2YWQyNWNkZTE5ZjE4YzUyNDQ2YTMzNzdjNzRhYjcyZTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci92eF9hdmF0YXIuanBnIiwidXNlcklkIjoxfQ==','2019-03-03 15:08:00.803362'),('6yc83s9k7k4msxhpi8f68md0qxgwfo5n','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-10-30 19:00:19.720910'),('702kwxcq7qqon8jhk4iazbcgw8wjlpqq','Nzk1MzM4ZDBhNjQwMTUxY2FkODJkODI0NjEzNDY2MDdiN2Q1MTI5ZTp7InVzZXJJZCI6MiwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzIucG5nIn0=','2018-02-23 23:27:19.991237'),('7ex2qvwannr1y9tnrou0cqs2212qdjt4','NzQyMjQ4MTYyOGQxODI2ZjUwZWM3YmM0Yzc2Mjg0NjY2NjA2NzI3Mjp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci8xNC5wbmciLCJ1c2VySWQiOjE0fQ==','2018-08-14 13:46:15.342744'),('7ohjqqen663zzjf5ptuskxenv05b88p6','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2019-06-30 13:58:26.277497'),('8ncs4z6z9047w4ftqckg50mbxvxtzvds','NzQyMjQ4MTYyOGQxODI2ZjUwZWM3YmM0Yzc2Mjg0NjY2NjA2NzI3Mjp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci8xNC5wbmciLCJ1c2VySWQiOjE0fQ==','2018-09-26 00:28:53.940274'),('axgjcvnxrkufaikqq0s1ncpr0ievrxxy','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-11-25 01:53:13.889461'),('ba0jh7ygde5gmgu7s0d75rd9dyxq9tou','MTQ1NTc0YTdlNjI2MzEzZDU5YzAwMTk2ZjA5NzcxZGJjOTkwNDJkZjp7InVzZXJJZCI6NiwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzYucG5nIn0=','2018-04-11 11:14:48.157917'),('dad8ruwi4d849558yq0i7n8vpha3jafq','NGVhYTA2NjA0MDkxOTJhNGRkM2ZjOWViZjI5MDBmYjc1NmU0NmJjNDp7fQ==','2019-01-08 23:27:07.809100'),('e9m1ihhfwd6mku1n6n8g47iqxsdyqc1i','ZjQzYzgwODI2ODBkNTM5ZTJiYTRlMDk4ZTEyYmQzY2RkMDEwODY1Mjp7InVzZXJJZCI6MTMsImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci8xMy5wbmcifQ==','2018-06-17 15:09:39.005258'),('eo02qmy90cbtz787q8lewzlwnnx9r9y0','ZmZjMWJiNDc2YWQyNWNkZTE5ZjE4YzUyNDQ2YTMzNzdjNzRhYjcyZTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci92eF9hdmF0YXIuanBnIiwidXNlcklkIjoxfQ==','2018-08-05 17:23:54.282276'),('eyz3ty4e8lhh5esuxejtttxmlgh6kylu','ZmZjMWJiNDc2YWQyNWNkZTE5ZjE4YzUyNDQ2YTMzNzdjNzRhYjcyZTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci92eF9hdmF0YXIuanBnIiwidXNlcklkIjoxfQ==','2018-12-10 23:56:08.859856'),('jalkmdupkx31bwslp0a6orgjjiz2k14d','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-08-02 12:15:49.289284'),('jxq9lkmzzr7uyi4bngifugvgih1g2m4r','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2019-07-14 10:33:07.195449'),('lblvc3c8ib3h3bw2v3904faba7n7si6p','MTQ1NTc0YTdlNjI2MzEzZDU5YzAwMTk2ZjA5NzcxZGJjOTkwNDJkZjp7InVzZXJJZCI6NiwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzYucG5nIn0=','2018-04-08 22:02:07.547464'),('m7dn4n244quvmy2udh742d30puvdgwj9','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-07-21 14:32:07.751058'),('mtwg1ir1fi001z0r2kzp1benx8ov0sk4','NzQyMjQ4MTYyOGQxODI2ZjUwZWM3YmM0Yzc2Mjg0NjY2NjA2NzI3Mjp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci8xNC5wbmciLCJ1c2VySWQiOjE0fQ==','2018-08-14 11:12:29.688780'),('nqzd81yezks1r83zz6n4th6h4ti3q28f','YmQ4ODEyNGVjN2Q4ZDAyMzRiNGRmZmYyMzQyOWQwOTYxNDVkZTkzZjp7InVzZXJJZCI6MTgsImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci9naXRodWI4LnBuZyJ9','2019-06-05 13:53:51.808879'),('ogjbhibfzfo0zljtbjmx2707p2ddnst8','ZmZjMWJiNDc2YWQyNWNkZTE5ZjE4YzUyNDQ2YTMzNzdjNzRhYjcyZTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci92eF9hdmF0YXIuanBnIiwidXNlcklkIjoxfQ==','2018-09-06 22:23:05.040458'),('qdblmcx6n4utnhmphhrgdzg5he81qb47','ZmZjMWJiNDc2YWQyNWNkZTE5ZjE4YzUyNDQ2YTMzNzdjNzRhYjcyZTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci92eF9hdmF0YXIuanBnIiwidXNlcklkIjoxfQ==','2019-02-26 20:13:05.326217'),('rfiwp43jm8m3rh9p4rodzn8qpi738aoj','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2019-04-07 10:36:35.764776'),('s1f3ogmbipszlooxgavekx6psxarswdg','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-06-17 14:38:59.480912'),('tahzyni1yexiqlyaeggmnq8b7elm6fta','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2019-06-08 08:22:52.106722'),('tfbkpitfmm59h58r9i8bvj464s58fwvs','NzQyMjQ4MTYyOGQxODI2ZjUwZWM3YmM0Yzc2Mjg0NjY2NjA2NzI3Mjp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci8xNC5wbmciLCJ1c2VySWQiOjE0fQ==','2018-09-03 13:07:36.180975'),('tixwztp1c10ed5vb9xfdx8ekp9puih9a','Y2MzODAzYmIzYTM4NzUxMTVjNTA0ODgwMjE5YjYxZjQzZWVmOGE4Mzp7InVzZXJJZCI6NywiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzcucG5nIn0=','2018-04-10 00:42:45.968863'),('tj5t7fc6wqhx3walr2zomtoioq6yk6n3','ZjZmMDU2NDNmNzBhMWY4YWRjODBjNmY2NGVhMGM3OWY5MGVkNjk5Mjp7InVzZXJJZCI6NCwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzQucG5nIn0=','2018-02-21 23:27:18.478149'),('ueuhvju1627q65s8h5xw4b7qa1hf5ctv','ZmZjMWJiNDc2YWQyNWNkZTE5ZjE4YzUyNDQ2YTMzNzdjNzRhYjcyZTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci92eF9hdmF0YXIuanBnIiwidXNlcklkIjoxfQ==','2018-09-03 14:13:10.264340'),('vgke0hd6f1k3z6b67fhb9uki13mbvehn','ZmZjMWJiNDc2YWQyNWNkZTE5ZjE4YzUyNDQ2YTMzNzdjNzRhYjcyZTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci92eF9hdmF0YXIuanBnIiwidXNlcklkIjoxfQ==','2018-08-27 18:19:33.064425'),('vubogo1xitl7d0zxkmmxld4ax3eiesj7','MmZiNjU5MmY1NzVkYzIzYjdmMTgyZGU0YWZmMzIwMjUwY2I5YzhhYTp7InVzZXJJZCI6MTYsImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci9naXRodWIxNC5wbmcifQ==','2019-04-03 15:28:39.000857'),('w46v1ozd9yy7bqkv3kq18uvaws0089ll','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-12-08 19:57:52.258678'),('wdqyov6m598hex0ji92qg76oso2io3v5','NWI1ZDQyZDJkY2Q2NDAyNWJjMmQ3ZWUxYjc3OTYwMTQyNDc2ZmJlNjp7InVzZXJJZCI6OCwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzgucG5nIn0=','2018-05-13 18:18:23.394794'),('wejbs1oe9wl3fl9oeo4cuv25eyn8elj1','ZmZjMWJiNDc2YWQyNWNkZTE5ZjE4YzUyNDQ2YTMzNzdjNzRhYjcyZTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci92eF9hdmF0YXIuanBnIiwidXNlcklkIjoxfQ==','2018-12-09 20:20:59.250988'),('ya6j4hg60rrehxapjolnlx6q8dl4oypu','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-08-02 12:15:30.953905'),('yi3b9e0dyts0uwvhi5mbbsugln55lzyj','NGVhYTA2NjA0MDkxOTJhNGRkM2ZjOWViZjI5MDBmYjc1NmU0NmJjNDp7fQ==','2018-10-23 21:09:38.860191'),('ynshk7a2l77l0uwo4ngfmpc1sc8vspe0','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2019-03-22 00:40:14.121953'),('zd5xfsuq6uez7wwlig4szs3ugu2fifn8','MTk5ODFlNmJhMTZjM2RmOWVkZDlkMGNmNGFhN2UzYjU4NmY0ODhmMTp7ImF2YXRhciI6Ii9zdGF0aWMvcG9sbHMvdXNlckF2YXRhci9naXRodWIxNS5wbmciLCJ1c2VySWQiOjl9','2018-06-09 14:47:04.720328'),('zd94ae7sn8vmpygwt6dyesrsuf4xbjeb','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2018-07-02 23:46:31.813731'),('zirxugumya51j98bjnklz00tuloitpqo','ZmYyMDdiYWMwYzg1OTE4YjM1ZDcwYjM5YmYxNjE4NDQ0ZDYxYWQyNTp7InVzZXJJZCI6MSwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyL3Z4X2F2YXRhci5qcGcifQ==','2019-07-14 10:38:07.017820'),('zp92ue5v30kxe6katm2d1q725z6frl70','Nzk1MzM4ZDBhNjQwMTUxY2FkODJkODI0NjEzNDY2MDdiN2Q1MTI5ZTp7InVzZXJJZCI6MiwiYXZhdGFyIjoiL3N0YXRpYy9wb2xscy91c2VyQXZhdGFyLzIucG5nIn0=','2018-04-02 13:10:42.237234');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_article`
--

DROP TABLE IF EXISTS `polls_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL,
  `title` varchar(50) NOT NULL,
  `title_zh` varchar(50) NOT NULL,
  `author` varchar(30) NOT NULL,
  `content_md` longtext NOT NULL,
  `content_html` longtext NOT NULL,
  `tags` varchar(30) NOT NULL,
  `views` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `is_exist` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_article`
--

LOCK TABLES `polls_article` WRITE;
/*!40000 ALTER TABLE `polls_article` DISABLE KEYS */;
INSERT INTO `polls_article` VALUES (2,'','Hello World','','karis','','Hello World!!!\r\n#####\r\nlt_cush1gt_cuslt_cusspan class=\"as-clr-purple\"gt_cusHlt_cus/spangt_cuslt_cusspan class=\"as-clr-red\"gt_cuselt_cus/spangt_cuslt_cusspan class=\"as-clr-yellow\"gt_cusLlt_cus/spangt_cuslt_cusspan class=\"as-clr-light-purple\"gt_cusLlt_cus/spangt_cuslt_cusspan class=\"as-clr-green\"gt_cus0lt_cus/spangt_cus lt_cusspan class=\"as-clr-red\"gt_cuswlt_cus/spangt_cuslt_cusspan class=\"as-clr-orange\"gt_cus0lt_cus/spangt_cuslt_cusspan class=\"as-clr-light-blue\"gt_cusRlt_cus/spangt_cuslt_cusspan class=\"as-clr-light-green\"gt_cusLlt_cus/spangt_cuslt_cusspan class=\"as-clr-zihong\"gt_cusdlt_cus/spangt_cuslt_cusspan class=\"as-clr-yellow\"gt_cus!lt_cus/spangt_cuslt_cus/h1gt_cus\r\n搞了好几个月，终于把这个博客搭好了，不容易啊。。。\r\nlt_cusbrgt_cus其实刚刚开始开发的时候，一直在犹豫要用现有的博客系统还是自己搞，用php还是python，然后最终选了Django。。果然还是太会折腾了。。\r\nlt_cusbrgt_cus\r\nlt_cusbrgt_cus风格偏向二次元。。一股浓浓的ACG味道。。。。请慢用(#^.^#)~\r\nlt_cusbrgt_cus','日常',437,'2018-05-30 00:57:50.870583','2018-05-30 22:18:36.213622',1),(3,'','画稿','','karis','','..\r\nlt_cusimg src=\"/static/polls/ArticleImages/hoshinosumika.jpg\" class=\"as-img-normal\" /gt_cus\r\n#####\r\n嗯\r\nlt_cusimg src=\"/static/polls/ArticleImages/hoshinosumika.jpg\" class=\"as-img-normal\" /gt_cus\r\nlt_cusbrgt_cus\r\nlt_cusbrgt_cus','画稿',395,'2018-05-30 22:43:24.151121','2018-12-01 18:23:29.976039',1),(4,'','LeetCode Stack','','karis','','Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.lt_cusbrgt_cus\r\n\r\nFor example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].lt_cusbrgt_cus\r\n\r\nNote: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].\r\nlt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\nlt_cusdiv class=\"code-wrapper normal-font\"gt_cus\r\nlt_cuspregt_cus\r\nlt_cuscode class=\"language-cpp\"gt_cus\r\nclass Solution {\r\npublic:\r\n    vector<int> dailyTemperatures(vector<int>& temperatures) {\r\n        int n = temperatures.size();\r\n        std::vector<int> vRet(n, 0);\r\n        std::stack<int> sIdx;\r\n        for (int i = 0; i < n; i++)\r\n        {\r\n            while (!sIdx.empty() && temperatures[i] > temperatures[sIdx.top()])\r\n            {\r\n                int idx = sIdx.top();\r\n                sIdx.pop();\r\n                vRet[idx] = i - idx;\r\n            }\r\n            sIdx.push(i);\r\n        }\r\n        return vRet;\r\n    }\r\n};\r\nlt_cus/codegt_cus\r\nlt_cus/pregt_cus\r\nlt_cus/divgt_cus\r\n偶尔也写写代码\r\nlt_cusbrgt_cus','code',682,'2018-07-08 17:42:19.200839','2018-12-01 18:25:59.465963',1),(5,'','懒','','karis','','.\r\n#####\r\n.','code',552,'2018-08-19 15:20:48.084890','2018-11-27 00:03:44.283721',1),(6,'','科学上网','','karis','','从虎牙离职以后，公司的vpn就用不了了，所以干脆自己搞个vps服务器，搭个科学上网环境好了，但是流量也比较多所以就分给几个人用吧。。（反正应该也没多少人）lt_cusbrgt_cus\r\nip: 45.32.23.169lt_cusbrgt_cus\r\n端口: 1024lt_cusbrgt_cus\r\n加密: AES-256-CFBlt_cusbrgt_cus\r\nemm...还有密码lt_cusbrgt_cus\r\n密码在下面lt_cusbrgt_cus\r\nlt_cusdiv style=\"display:none;\"gt_cus(密码: nasac0.club)lt_cus/divgt_cus\r\n密码在上面lt_cusbrgt_cus\r\n你能找得到吗哈哈哈lt_cusbrgt_cus\r\n#####\r\n从虎牙离职以后，公司的vpn就用不了了，所以干脆自己搞个vps服务器，搭个科学上网环境好了，但是流量也比较多所以就分给几个人用吧。。（反正应该也没多少人）lt_cusbrgt_cus\r\nip: 45.32.23.169lt_cusbrgt_cus\r\n端口: 1024lt_cusbrgt_cus\r\n加密: AES-256-CFBlt_cusbrgt_cus\r\nemm...还有密码lt_cusbrgt_cus\r\n密码在下面lt_cusbrgt_cus\r\nlt_cusdiv style=\"display:none;\"gt_cus(密码: nasac0.club)lt_cus/divgt_cus\r\n密码在上面lt_cusbrgt_cus\r\n你能找得到吗哈哈哈lt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n\r\nlt_cusspan class=\"clr-BlueViolet\"gt_cus---------------------------2018/12/09更新---------------------------lt_cus/spangt_cus\r\nlt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n之前在pc端上试着不稳定，还是移动端和平板比较好用lt_cusbrgt_cus\r\n然后你需要有一个连接vps服务器的客户端，遗憾的是很多免费客户端都已经被大陆和谐了，所以这里提供一些下载链接：lt_cusbrgt_cus\r\n如果您是Android系统的话，可以点击lt_cusa class=\'a-link\' target=\'_blank\' href=\"https://github.com/shadowsocks/shadowsocks-android/releases\"gt_cus这里lt_cus/agt_cus下载apk安装包(安卓端的成功案例可以咨询@ZmSss 同学)lt_cusbrgt_cus\r\n如果您是iOS系统的话，点击lt_cusa class=\'a-link\' target=\'_blank\' href=\"https://pan.baidu.com/s/1cQPjoCu2cLaeoS_loES6mw\"gt_cus这里lt_cus/agt_cus下载其他网友提供的ipa安装包(百度网盘提取码7y3j)。lt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n如果您不知道该怎么安装的话，可以用数据线连接电脑，通过lt_cusa \r\n target=\'_blank\' class=\'a-link\' href=\"https://pro.25pp.com/download/25pp_00018/8005/\"gt_cuspp助手lt_cus/agt_cus(实在不是打广告，你们也可以用其它的)之类的软件来安装。\r\nlt_cusbrgt_cus\r\n实在不行就来微信找我或者寻求搜索引擎的帮助叭 :-)lt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n当你安装好客户端之后，就可以使用文章开头提到的账号信息登录vpn了，体验从零开始的翻墙生活\r\n\r\n\r\nlt_cusdiv class=\"clr-size clr-fix-bottom\"gt_cus\r\nlt_cusspan class=\"clr-Crimson\"gt_cus[上海·徐汇]lt_cus/spangt_cus\r\nlt_cusspan class=\"clr-purple \"gt_cus[小雪]lt_cus/spangt_cus\r\nlt_cus/divgt_cus','资源',506,'2018-08-20 14:21:45.434928','2018-12-09 20:44:20.891727',1),(7,'','发现一个有趣的网站','','karis','','最近发现一个把人工智能，区块链和动画生成联系起来的lt_cusa target=\'_blank\' href=\'https://crypko.ai/\' class=\'a-link\'gt_cus应用lt_cus/agt_cus，好像还挺好玩的。lt_cus/brgt_cus\r\nu2b上面有个视频把它搬过来..\r\nlt_cus/ brgt_cus\r\nlt_cusbr /gt_cus\r\nlt_cusspan class=\"clr-Magenta\"gt_cus[视频]lt_cus/spangt_cus\r\n\r\n#####\r\n\r\n最近发现一个把人工智能，区块链和动画生成联系起来的lt_cusa target=\'_blank\' href=\'https://crypko.ai/\' class=\'a-link\'gt_cus应用lt_cus/agt_cus，好像还挺好玩的。lt_cus/brgt_cus\r\nu2b上面有个视频把它搬过来..\r\n\r\nlt_cusdiv class=\"dp-border\"gt_cus\r\nlt_cusdiv id=\"cry7_1\"gt_cuslt_cus/divgt_cus\r\nlt_cus/divgt_cus\r\nlt_cusbr /gt_cus\r\nlt_cusimg data-action=\"zoom\" class=\"ar-pic\" src=\"http://45.32.23.169/pic/7/ml.jpg\"gt_cuslt_cus/imggt_cus\r\n\r\nlt_cusdiv class=\"clr-size clr-fix-bottom\"gt_cus\r\nlt_cusspan class=\"clr-Crimson\"gt_cus[上海·徐汇]lt_cus/spangt_cus\r\nlt_cusspan class=\"clr-purple \"gt_cus[晴]lt_cus/spangt_cus\r\nlt_cusspan class=\"clr-Coral\"gt_cus[打了一下午的王者荣耀和麻将]lt_cus/spangt_cus\r\nlt_cusspan class=\"clr-GreenYellow\"gt_cus[再玩剁手]lt_cus/spangt_cus\r\nlt_cus/divgt_cus','未分类',461,'2018-11-24 20:14:24.477661','2018-11-25 20:26:01.815003',1),(8,'','最后一课','','karis','','\"琪亚娜lt_cusbrgt_cus\r\n当你醒来，会看到一切都变了lt_cusbrgt_cus\r\n你会发现，这个世界不再美好lt_cusbrgt_cus\r\n那些平凡的日常，都将一去不回lt_cusbrgt_cus\r\n但是，不要放弃，永远不要放弃lt_cusbrgt_cus\r\n琪亚娜，抬起头，继续前进吧lt_cusbrgt_cus\r\n去把这个不完美的故事lt_cusbrgt_cus\r\n变成你所期望的样子lt_cusbrgt_cus\r\n活下去，琪亚娜lt_cusbrgt_cus\r\n这就是..最后一课了\"lt_cusbrgt_cus\r\nlt_cusspan class=\"clr-Magenta\"gt_cus[视频]lt_cus/spangt_cus\r\n#####\r\nlt_cusdiv class=\"dp-border\"gt_cus\r\nlt_cusdiv id=\"cry8_1\"gt_cuslt_cus/divgt_cus\r\nlt_cus/divgt_cus\r\n\r\nlt_cusbrgt_cus\r\n\"琪亚娜lt_cusbrgt_cus\r\n当你醒来，会看到一切都变了lt_cusbrgt_cus\r\n你会发现，这个世界不再美好lt_cusbrgt_cus\r\n那些平凡的日常，都将一去不回lt_cusbrgt_cus\r\n但是，不要放弃，永远不要放弃lt_cusbrgt_cus\r\n琪亚娜，抬起头，继续前进吧lt_cusbrgt_cus\r\n去把这个不完美的故事lt_cusbrgt_cus\r\n变成你所期望的样子lt_cusbrgt_cus\r\n活下去，琪亚娜lt_cusbrgt_cus\r\n这就是..最后一课了\"lt_cusbrgt_cus\r\n\r\nlt_cusdiv class=\"clr-size clr-fix-bottom\"gt_cus\r\nlt_cusspan class=\"clr-Crimson\"gt_cus[休伯利安]lt_cus/spangt_cus\r\nlt_cusspan class=\"clr-purple \"gt_cus[夜气辉]lt_cus/spangt_cus\r\nlt_cus/divgt_cus','崩坏3',241,'2018-12-24 23:25:24.644474','2018-12-24 23:50:03.244375',1),(9,'','BuZhiDaoGaiXieShenMeQAQ','','karis','','大约有半年没动了，除草。。。因为一直没什么时间（其实是懒）lt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n说一下对主页做的一些小改动。lt_cusbrgt_cus\r\n首先是把域名从eientei.moe换成了himarisa.moe，以后应该都用这个了，毕竟我是住在雾雨魔法之森的人类，并不在永远亭lt_cusbrgt_cus\r\n然后把以前的黑历史删了一些，还要继续删，现在每看一遍自己的黑历史都好羞耻lt_cusbrgt_cus\r\n还有把标题栏改成了小莎莎的弹幕回忆，主要记录摸你傻的日常，制造更多的黑历史（xlt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n以及这个网站连同我的vps一起被qiang掉了，所以本来就没什么流量的地方，现在更没有流量了lt_cusbrgt_cus\r\n打算搬回到国内的服务器（还好之前已经把这些东西上了docker，所以搬回来就变得轻松了很多）lt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n要是有人fo我的话，一定勤更（开玩笑的，这本来就是比较隐秘的地方，我甚至都没怎么和人说过我的主页地址）lt_cusbrgt_cus\r\n\r\n#####\r\n\r\n大约有半年没动了，除草。。。因为一直没什么时间（其实是懒）lt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n说一下对主页做的一些小改动。lt_cusbrgt_cus\r\n首先是把域名从eientei.moe换成了himarisa.moe，以后应该都用这个了，毕竟我是住在雾雨魔法之森的人类，并不在永远亭lt_cusbrgt_cus\r\n然后把以前的黑历史删了一些，还要继续删，现在每看一遍自己的黑历史都好羞耻lt_cusbrgt_cus\r\n还有把标题栏改成了小莎莎的弹幕回忆，主要记录摸你傻的日常，制造更多的黑历史（xlt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n以及这个网站连同我的vps一起被qiang掉了，所以本来就没什么流量的地方，现在更没有流量了lt_cusbrgt_cus\r\n打算搬回到国内的服务器（还好之前已经把这些东西上了docker，所以搬回来就变得轻松了很多）lt_cusbrgt_cus\r\nlt_cusbrgt_cus\r\n要是有人fo我的话，一定勤更（开玩笑的，这本来就是比较隐秘的地方，我甚至都没怎么和人说过我的主页地址）lt_cusbrgt_cus','除草',0,'2019-06-30 10:42:19.287583','2019-06-30 10:43:47.186409',1);
/*!40000 ALTER TABLE `polls_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_choice`
--

DROP TABLE IF EXISTS `polls_choice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choice_text` varchar(200) NOT NULL,
  `votes` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_choice_question_id_c5b4b260_fk_polls_question_id` (`question_id`),
  CONSTRAINT `polls_choice_question_id_c5b4b260_fk_polls_question_id` FOREIGN KEY (`question_id`) REFERENCES `polls_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_choice`
--

LOCK TABLES `polls_choice` WRITE;
/*!40000 ALTER TABLE `polls_choice` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_choice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_likemedata`
--

DROP TABLE IF EXISTS `polls_likemedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_likemedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `LikeMeCount` int(11) NOT NULL,
  `UnLikeMeCount` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_likemedata`
--

LOCK TABLES `polls_likemedata` WRITE;
/*!40000 ALTER TABLE `polls_likemedata` DISABLE KEYS */;
INSERT INTO `polls_likemedata` VALUES (1,1359,0);
/*!40000 ALTER TABLE `polls_likemedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_question`
--

DROP TABLE IF EXISTS `polls_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_text` varchar(201) NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_question`
--

LOCK TABLES `polls_question` WRITE;
/*!40000 ALTER TABLE `polls_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_singlemsgboard`
--

DROP TABLE IF EXISTS `polls_singlemsgboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_singlemsgboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `msg_pickle_str` longblob NOT NULL,
  `is_exist` int(11) NOT NULL,
  `hash_value` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_singlemsgboard`
--

LOCK TABLES `polls_singlemsgboard` WRITE;
/*!40000 ALTER TABLE `polls_singlemsgboard` DISABLE KEYS */;
INSERT INTO `polls_singlemsgboard` VALUES (14,1002,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-03-25 22:21:53.896288qX\0\0\0哇qcbuiltins\nset\nq]qKa�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-03-25 22:22:04.580311q\nX\0\0\0咔咔qh]q�q\rRqX\0\0\0Neeqee.',0,'tczy92z2p9'),(15,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-25 22:22:35.997089qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'18z9qdkc54'),(16,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-26 11:35:05.754260qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'gg5v5z63ni'),(17,1001,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-03-26 11:40:55.074956qX\0\0\01qcbuiltins\nset\nq]qKa�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-03-26 11:41:10.402221q\nX\0\0\012qh]q�q\rRqX\0\0\0Neeqe]q(KKX\Z\0\0\02018-03-26 11:41:15.539042qX\0\0\0122qh]q�qRqX\0\0\0Neeqe]q(KKX\Z\0\0\02018-03-26 11:41:18.610505qX\0\0\012qh]q\Z�qRqX\0\0\0Neeqee.',0,'05jbxj04bf'),(18,1001,_binary '�]q\0]q(KKX\Z\0\0\02018-03-26 14:06:26.693699qX	\0\0\0哇咔咔qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',1,'wtg4028itg'),(19,1002,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-26 14:07:09.021894qX\0\0\0233qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'ty90d5aoor'),(20,1002,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-26 19:42:58.158070qXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/91260cbbc2.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'xi69kre5aj'),(21,1002,_binary '�]q\0]q(KKX\Z\0\0\02018-03-26 19:43:06.130056qXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/0b01ce848b.gif\"gt_cusqcbuiltins\nset\nq]qKa�qRqX\0\0\0\0qea.',1,'owhwya0brt'),(22,1002,_binary '�]q\0]q(KKX\Z\0\0\02018-03-27 00:43:42.494749qX\0\0\0啊哈哈这个。。qcbuiltins\nset\nq]qKa�qRqX\0\0\0\0qea.',1,'u3gmbbnmkf'),(23,1002,_binary '�]q\0]q(KKX\Z\0\0\02018-03-27 00:46:28.556227qXB\0\0\0lt_cusspan class=\"cute-font\"gt_cus(..›ᴗ‹..)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',1,'1q1myeyji3'),(24,1002,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-27 19:58:11.953895qX�\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/91260cbbc2.gif\"gt_cuslt_cusspan class=\"cute-font\"gt_cus( ꒪⌓꒪)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'vveoxphks1'),(25,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-28 00:52:30.037983qXW\0\0\0lt_cusspan class=\"cute-font\"gt_cus ̋(ˊᵒ̴̶̷̤ ꇴ ᵒ̴̶̷̤ˋ)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'b7glk8yazb'),(26,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-28 11:15:29.163964qX\0\0\0弱弱qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'uhpjq3nfy2'),(27,1002,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-28 20:36:12.099857qXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/4ed2dac213.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'wlx88y416y'),(28,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 20:55:24.922874qXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/55b2bdbd4c.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'7ilz3yacw8'),(29,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 20:55:53.914076qX\0\0\0要qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'xtnmqnmp29'),(30,1002,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 21:55:14.701232qXA\0\0\0lt_cusspan class=\"cute-font\"gt_cus( ˶ˇωˇ˶ )lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'8bodvzfs9h'),(31,1002,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 21:55:49.795022qX\0\0\0她qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'ipt3wb2b9u'),(32,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 23:33:32.237768qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'oagf7ccacp'),(33,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 23:33:37.209787qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'4icfv83sgd'),(34,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 23:33:41.171455qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'2jiviuf7p8'),(35,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 23:37:21.135916qX\0\0\02qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'fyo56aqhzw'),(36,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 23:41:30.153680qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'yeff82if3d'),(37,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-03-31 23:41:45.192729qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'l0xufjyns8'),(38,1002,_binary '�]q\0]q(KK\0X\Z\0\0\02018-04-01 01:31:55.404742qX\0\0\0去qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'unoqs1fe61'),(39,1001,_binary '�]q\0]q(KKX\Z\0\0\02018-04-29 18:19:28.941403qX[\0\0\0没有gravatar吗lt_cusspan class=\"cute-font\"gt_cus(ᵒ̤̑ ₀̑ ᵒ̤̑)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',1,'lbn24t7c8s'),(40,1001,_binary '�]q\0]q(KKX\Z\0\0\02018-05-30 00:41:50.869307qXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/4ed2dac213.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',1,'9cb4tsk05u'),(41,1001,_binary '�]q\0]q(KKX\Z\0\0\02018-05-30 00:43:59.489325qX@\0\0\0lt_cusspan class=\"cute-font\"gt_cusᕕ( ᐛ )ᕗlt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',1,'8tveg0pe7t'),(42,1001,_binary '�]q\0(]q(KKX\Z\0\0\02018-05-30 00:44:45.343943qX\0\0\0我居然是抖S，笑哭qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KK\0X\Z\0\0\02018-05-30 00:45:41.942389q\nX\0\0\0嘻嘻qh]q�q\rRqX\0\0\07079359qe]q(KKX\Z\0\0\02018-05-30 00:47:50.364597qX\0\0\0嘻嘻qh]q�qRqX\0\0\07079359qee.',1,'oydmtfq47a'),(43,2,_binary '�]q\0]q(KK\0X\Z\0\0\02018-05-30 22:24:49.681479qX?\0\0\0lt_cusspan class=\"cute-font\"gt_cus( ꒪⌓꒪)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'xnlhgvajtv'),(44,2,_binary '�]q\0]q(KK\0X\Z\0\0\02018-05-30 22:25:05.176562qXI\0\0\0lt_cusspan class=\"cute-font\"gt_cus( •̀ .̫ •́ )✧lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'6rbbryy3zm'),(45,32,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 05:06:38.665150qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'rdg7y7wxry'),(46,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 05:26:11.152677qX\0\0\03qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'ik5ywmoo1d'),(47,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 05:26:27.405775qX\0\0\05qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'9c5ieq92eg'),(48,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 05:37:03.565039qX\0\0\07qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'a92ai38a4o'),(49,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:23:27.342531qXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/91260cbbc2.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'wiwfmphx1j'),(50,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:23:41.208642qX\0\0\05qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'3cs6o445ts'),(51,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:23:44.119001qX\0\0\06qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'qvdcq8ugvh'),(52,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:23:46.489826qX\0\0\07qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'7soyd90mv2'),(53,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:23:48.613823qX\0\0\08qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'xptm9uehn9'),(54,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:25:57.719603qXW\0\0\0lt_cusspan class=\"cute-font\"gt_cus ̋(ˊᵒ̴̶̷̤ ꇴ ᵒ̴̶̷̤ˋ)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'34v7x3ovv6'),(55,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:32:37.167240qXW\0\0\0lt_cusspan class=\"cute-font\"gt_cus ̋(ˊᵒ̴̶̷̤ ꇴ ᵒ̴̶̷̤ˋ)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'3rd0o7h6c9'),(56,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:34:54.938140qXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/91260cbbc2.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'45j77zujly'),(57,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:46:59.476088qXW\0\0\0lt_cusspan class=\"cute-font\"gt_cus ̋(ˊᵒ̴̶̷̤ ꇴ ᵒ̴̶̷̤ˋ)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'0xb0s9mvz7'),(58,3,_binary '�]q\0]q(KK\0X\Z\0\0\02018-06-03 06:51:30.496186qXW\0\0\0lt_cusspan class=\"cute-font\"gt_cus ̋(ˊᵒ̴̶̷̤ ꇴ ᵒ̴̶̷̤ˋ)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'a9kg5d84hd'),(59,2,_binary '�]q\0(]q(K\rK\0X\Z\0\0\02018-06-03 14:29:26.909908qX\0\0\02345qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KK\0X\Z\0\0\02018-06-03 14:30:19.595449q\nXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/c868b742e5.gif\"gt_cusqh]q�q\rRqX\n\0\0\0h胡萝卜qee.',0,'g6w6xj06pa'),(60,2,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 14:53:24.668105qX\0\0\0Rqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'97ogan4d7j'),(61,2,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 15:13:05.522703qX\0\0\0H发挥qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'z76ilr5vle'),(62,2,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 15:13:21.657381qX\0\0\0在qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'427tgzzv8n'),(63,2,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 15:20:07.647969qX\0\0\0这qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'csmnuwz9gd'),(64,2,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 16:09:35.626532qX\0\0\0Fh岗qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'j3oq2vm8f1'),(65,2,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 16:14:47.302160qX\0\0\0这qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'w35sey4ze5'),(66,2,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 16:16:48.662355qX\0\0\0你是怎么回短信的qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'4x86du5g8c'),(67,2,_binary '�]q\0(]q(K\rK\0X\Z\0\0\02018-06-03 16:22:36.511290qX\0\0\0かqcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(K\rKX\Z\0\0\02018-06-03 16:23:18.187907q\nX	\0\0\0抜いてqh]q�q\rRqX\n\0\0\0h胡萝卜qee.',0,'an0tt6ng3l'),(68,2,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 16:40:46.719573qX\0\0\0あqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'yw3bl406jw'),(69,1002,_binary '�]q\0]q(K\rK\0X\Z\0\0\02018-06-03 19:06:30.465155qX\0\0\0等等qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'wxqw7x3vdh'),(70,1002,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-06-07 22:10:41.007455qX�\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/19082ca464.gif\"gt_cuslt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/55b2bdbd4c.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-06-07 22:11:10.336699q\nX\r\0\0\0_(:з」∠)_qh]q�q\rRqX\0\0\0Nasacoqee.',0,'0ewp8fmjwa'),(71,2,_binary '�]q\0(]q(K\rKX\Z\0\0\02018-06-07 23:09:30.280437qX\0\0\0对qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-07-07 14:32:17.423355q\nXY\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/91260cbbc2.gif\"gt_cusqh]q�q\rRqX\n\0\0\0h胡萝卜qee.',1,'11hjt4qqhz'),(72,1002,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-07-19 11:26:27.913116qX\0\0\0hhhhhhhhhhhhqcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-07-19 12:18:37.992545q\nXB\0\0\0lt_cusspan class=\"cute-font\"gt_cus(..›ᴗ‹..)lt_cus/spangt_cusqh]q�q\rRqX\0\0\0腿腿qee.',0,'om4aq6t0y5'),(73,1001,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-07-19 11:27:07.129166qX\0\0\0留爪qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-07-19 12:18:20.906608q\nX\0\0\0hello 腿腿qh]q�q\rRqX\0\0\0腿腿qe]q(KKX\Z\0\0\02018-07-19 16:07:44.457290qXO\0\0\0哈喽lt_cusspan class=\"cute-font\"gt_cus (๑•̀ω•́ ๑)lt_cus/spangt_cusqh]q�qRqX\0\0\0Nasacoqee.',0,'v0aii1vuuo'),(74,1001,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-07-22 17:24:01.536420qX\0\0\07qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-07-22 17:24:14.137436q\nX\0\0\054qh]q�q\rRqX\0\0\0Nasacoqee.',0,'glw2ih1hdb'),(75,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-07-22 17:24:21.459926qX\0\0\043 qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'e54kajznpd'),(76,1001,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-07-22 17:24:29.765386qX\0\0\08qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-07-22 17:24:40.219020q\nX\0\0\087qh]q�q\rRqX\0\0\0Nasacoqee.',0,'cm5c20rjnl'),(77,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-07-22 17:24:47.399229qX\0\0\087qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'xv19eo3iaj'),(78,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-07-22 17:24:53.132216qX\0\0\0097qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'zd7o3gfz5h'),(79,1001,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-07-22 17:32:37.326323qX\0\0\011111111111111qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-07-22 17:35:15.957666q\nX\r\0\0\02333333333333qh]q�q\rRqX\0\0\0Nasacoqee.',0,'k46i8fh9py'),(80,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-07-22 17:33:00.126999qX\0\0\011111111111111qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'sjovegqkqs'),(81,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-07-22 17:33:38.199976qX\0\0\0434343434343qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'r7hf3d192m'),(82,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-07-22 17:35:26.181158qX\0\0\0324qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'l02jvlnhdy'),(83,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-07-22 17:38:48.140168qX\0\0\0111qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'k8ibgrbiv5'),(84,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-07-22 17:42:23.943016qX\0\0\0323422qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'xhvah19y9r'),(85,1001,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-07-22 17:48:52.248096qX\0\0\0543qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-07-22 17:49:00.069563q\nX\0\0\0432qh]q�q\rRqX\0\0\0Nasacoqe]q(KKX\Z\0\0\02018-07-22 17:49:21.277934qX\0\0\054546456qh]q�qRqX\0\0\0Nasacoqe]q(KKX\Z\0\0\02018-07-22 17:49:55.358319qX\0\0\00qh]q\Z�qRqX\0\0\0Nasacoqe]q(KKX\Z\0\0\02018-07-22 17:50:17.065818qX\0\0\098q h]q!�q\"Rq#X\0\0\0Nasacoq$ee.',0,'414imvd3nv'),(86,2,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-07-31 13:47:32.530006qX	\0\0\0超棒derqcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-07-31 13:50:57.800909q\nXa\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/617406e82e.gif\"gt_cus 乾杯~qh]q�q\rRqX\0\0\0腿腿qee.',0,'vamcp6u2cj'),(87,4,_binary '�]q\0(]q(KK\0X\Z\0\0\02018-08-13 17:40:52.833767qXX\0\0\0这是谁呀怎么这么酷lt_cusspan class=\"cute-font\"gt_cus(〃ω〃)lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02018-08-13 18:20:30.072769q\nX\'\0\0\0怠惰啊，一个月没更新了。。qh]q�q\rRqX\0\0\0腿腿qee.',0,'k5q1s6ca3f'),(88,5,_binary '�]q\0]q(KK\0X\Z\0\0\02018-08-20 13:09:29.234874qX\0\0\0存在感=100%qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'5fufwm6u6a'),(89,1001,_binary '�]q\0]q(KK\0X\Z\0\0\02018-09-12 00:29:42.688443qXi\0\0\0日常深夜思考人生 托腮lt_cusspan class=\"cute-font\"gt_cus( •̥́ ˍ •̀ू )lt_cus/spangt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'nyga5irde7'),(90,1002,_binary '�]q\0]q(KK\0X\Z\0\0\02018-11-11 01:53:29.780853qX\0\0\01qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'l4pjnpi2se'),(91,6,_binary '�]q\0]q(KK\0X\Z\0\0\02019-02-12 20:13:59.902632qXq\0\0\0偶尔也会出故障Orzlt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/55b2bdbd4c.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'72vcdoxa80'),(92,6,_binary '�]q\0]q(KK\0X\Z\0\0\02019-02-12 20:14:17.011732qXr\0\0\0偶尔也会出故障Orz\nlt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/55b2bdbd4c.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',0,'kfg7blz5si'),(93,6,_binary '�]q\0(]q(KK\0X\Z\0\0\02019-02-12 20:15:04.510142qXw\0\0\0偶尔也会出故障Orz<br/>\nlt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/55b2bdbd4c.gif\"gt_cusqcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02019-02-12 20:15:35.952658q\nX\0\0\0&lt;br/&gt;\ndddqh]qKa�q\rRqX\0\0\0karisqee.',0,'5cuh5u24ji'),(94,6,_binary '�]q\0]q(KKX\Z\0\0\02019-02-12 20:16:39.061211qXr\0\0\0lt_cusimg class=\"bilibili-img-scale-up\" src=\"/static/polls/bilibili/55b2bdbd4c.gif\"gt_cus\n偶尔也会出故障Orzqcbuiltins\nset\nq]qKa�qRqX\0\0\0\0qea.',1,'e5jqvhi4lo'),(95,6,_binary '�]q\0(]q(KKX\Z\0\0\02019-02-17 15:09:04.298029qX5\0\0\0原来的1024的端口被封了，改成2019就好了qcbuiltins\nset\nq]q�qRqX\0\0\0\0qe]q	(KKX\Z\0\0\02019-03-08 00:40:43.572742q\nX,\0\0\0又被封了，现在是20190（。。无奈qh]q�q\rRqX\0\0\0karisqee.',1,'diluts9jev'),(96,1001,_binary '�]q\0]q(KKX\Z\0\0\02019-06-30 10:38:13.835849qX\0\0\0?qcbuiltins\nset\nq]q�qRqX\0\0\0\0qea.',1,'t8540ab2dy');
/*!40000 ALTER TABLE `polls_singlemsgboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_userinfo`
--

DROP TABLE IF EXISTS `polls_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(500) NOT NULL,
  `email` varchar(50) NOT NULL,
  `sex` varchar(2) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `com_power` int(11) NOT NULL,
  `level_tag` varchar(20) NOT NULL,
  `birthday` datetime(6) NOT NULL,
  `introduce` varchar(100) NOT NULL,
  `avatar_url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_userinfo`
--

LOCK TABLES `polls_userinfo` WRITE;
/*!40000 ALTER TABLE `polls_userinfo` DISABLE KEYS */;
INSERT INTO `polls_userinfo` VALUES (1,'karis','voc#2017','707935952@qq.com','7','2018-03-25 21:53:25.367805',0,'超能力者','2018-03-25 21:53:25.367814','','vx_avatar.jpg'),(5,'123123123','111111','e12@1.com','1','2018-05-29 23:48:20.602809',184,'大能力者','2018-05-29 23:48:20.602838','','github26.png'),(6,'Nee','123123','1@1.com','1','2018-03-25 22:01:45.483471',0,'超能力者','2018-03-25 22:01:45.483491','','6.png'),(7,'wak','123123','22@2.com','8','2018-03-27 00:42:26.652164',0,'超能力者','2018-03-27 00:42:26.652178','','7.png'),(8,'Nas','123123','12134@1.com','7','2018-04-29 18:15:52.043327',0,'超能力者','2018-04-29 18:15:52.043342','','8.png'),(9,'小饼子','111111','1223134@1.com','1','2018-05-26 14:47:04.693023',0,'超能力者','2018-05-26 14:47:04.693036','','github15.png'),(10,'333','111111','121334@1.com','1','2018-05-29 23:42:48.519513',459,'大能力者','2018-05-29 23:42:48.519539','','github6.png'),(12,'7079359','111111','121123334@1.com','1','2018-05-29 23:49:44.278295',141,'抖S','2018-05-29 23:49:44.278321','','github15.png'),(13,'h胡萝卜','111111','2066584567@qq.com','3','2018-06-03 14:28:04.989476',449,'抖M','2018-06-03 14:28:04.989493','','13.png'),(14,'腿腿','ly19960413','515098384@qq.com','12','2018-07-19 11:25:32.171737',364,'死宅','2018-07-19 11:25:32.171759','','14.png'),(15,'永琳','nihao123','545689881@qq.com','2','2018-12-25 23:18:50.583372',314,'精灵','2018-12-25 23:18:50.583391','','github26.png'),(16,'air','fcc1995813','2224544595@qq.com','1','2019-03-20 15:28:38.984522',75,'大能力者','2019-03-20 15:28:38.984547','','github14.png'),(17,'kki','1111112','8534354354@qq.com','7','2019-05-22 13:24:46.827860',5,'精灵','2019-05-22 13:24:46.827878','','github22.png'),(18,'hfh','111111','707952@qq.com','2','2019-05-22 13:52:13.634197',53,'光之精灵','2019-05-22 13:52:13.634216','','github8.png');
/*!40000 ALTER TABLE `polls_userinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-30 12:04:39
