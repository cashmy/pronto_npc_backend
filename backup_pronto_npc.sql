-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: pronto_npc
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `archetype_archetype`
--

DROP TABLE IF EXISTS `archetype_archetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `archetype_archetype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `notes` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `expansion` tinyint(1) NOT NULL,
  `related_archetypes` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archetype_archetype`
--

LOCK TABLES `archetype_archetype` WRITE;
/*!40000 ALTER TABLE `archetype_archetype` DISABLE KEYS */;
INSERT INTO `archetype_archetype` VALUES (1,'Hero','The central figure.\r\nEmbarks on the adventure, faces challenges, transforms, and returns changed.','','2025-04-27 13:50:16.155568','2025-04-27 13:50:16.155568',0,NULL),(2,'Mentor','Provides guidance, wisdom, and training.\r\nOften gives the Hero tools, advice, or magical gifts for the journey (e.g., Merlin to King Arthur).','','2025-04-27 13:50:34.026128','2025-04-27 13:50:34.026128',0,NULL),(3,'Threshold Guardian','Tests the Hero at important moments.\r\nMay appear as an obstacle to the Hero’s initial steps or later stages.\r\nNot always \"evil\" — sometimes just a tester or challenger.','','2025-04-27 13:50:52.602624','2025-04-27 13:50:52.602624',0,NULL),(4,'Herald','Announces the call to adventure.\r\nCan be a person, event, or even inner feeling that propels the Hero forward.','','2025-04-27 13:51:06.818141','2025-04-27 13:51:06.818141',0,NULL),(5,'Shapeshifter','A character whose loyalty, appearance, or role seems unstable or uncertain.\r\nCreates tension and doubt (e.g., mysterious allies, betrayers).','','2025-04-27 13:51:19.688469','2025-04-27 13:51:19.688469',0,NULL),(6,'Shadow','Represents the Hero’s greatest fear, enemy, or even darker parts of themselves.\r\nOften the villain or antagonist but symbolically represents internal struggles too.','','2025-04-27 13:51:30.971919','2025-04-27 13:51:30.971919',0,NULL),(7,'Trickster','Brings mischief, humor, and sometimes chaos.\r\nForces change or new perspectives through disruption (e.g., Loki in Norse myths).','','2025-04-27 13:51:43.798869','2025-04-27 13:51:43.798869',0,NULL),(8,'Ally/Sidekick','Friends or companions who assist the Hero on their journey.\r\nMay form a team or aid with different strengths.','','2025-04-27 13:51:59.529418','2025-04-27 13:57:53.474498',0,NULL),(9,'Temptor/Temptress','(or Temptation)\r\nSymbolizes worldly temptations that may lead the Hero off the path.\r\nNot always a literal \"Temptor/Temptress\" — it could be wealth, comfort, pride, etc.','','2025-04-27 13:52:19.874708','2025-04-27 13:53:28.825333',0,NULL),(10,'Father Figure','(or Atonement with the Father)\r\nRepresents authority, judgment, protection, or challenge.\r\nThe Hero often has to confront or reconcile with this figure to achieve growth.','','2025-04-27 13:52:54.086724','2025-04-27 13:52:54.086724',0,NULL),(11,'Protector','Defends and safeguards the Hero (body, spirit, or mission).','','2025-04-27 14:08:42.541422','2025-04-27 14:08:42.541422',1,'Ally (more active role)'),(12,'Mirror','Reflects the Hero’s strengths, weaknesses, or hidden truth.','','2025-04-27 14:09:07.396515','2025-04-27 14:09:07.396515',1,'Shapeshifter, Shadow'),(13,'Secondary Hero','Takes up the Hero’s cause temporarily or evolves into their own Hero\'s Journey.','','2025-04-27 14:12:41.720872','2025-04-27 14:12:41.720872',1,'Ally evolving into Hero'),(14,'Guardian of the Soul','Reminds the Hero of their true purpose and inner light when they forget.','','2025-04-27 14:13:11.768654','2025-04-27 14:13:11.768654',1,'Ally, Mentor (emotional version)'),(15,'Comic Relief','Lightens the tone, helping the audience and Hero breathe or reset.','','2025-04-27 14:13:36.807412','2025-04-27 14:13:36.807412',1,'Trickster (lighter form)'),(16,'Love Interest','Personifies connection, compassion, and emotional stakes for the Hero.','','2025-04-27 14:13:55.994679','2025-04-27 14:13:55.994679',1,'Can overlap with Ally, Temptress'),(17,'False Mentor','Appears wise but misguides the Hero intentionally or accidentally.','','2025-04-27 14:14:15.895557','2025-04-27 14:14:15.895557',1,'Shapeshifter, Shadow'),(18,'Shadow Ally','An \"ally\" figure whose actions accidentally cause harm or delay.','','2025-04-27 14:14:38.338421','2025-04-27 14:14:38.338421',1,'Shapeshifter'),(19,'Wise Fool','Appears foolish but delivers critical truth or insight in unexpected ways.','','2025-04-27 14:14:54.076132','2025-04-27 14:14:54.076132',1,'Trickster (with deeper wisdom)'),(20,'Threshold Companion','Only helps the Hero during a specific \"threshold\" phase, not the whole journey.','','2025-04-27 14:15:18.266019','2025-04-27 14:15:18.266019',1,'Ally (limited)'),(21,'Wounded Healer','A mentor or guide whose own pain or mistakes are critical to their wisdom.','','2025-04-27 14:15:39.222949','2025-04-27 14:15:39.223955',1,'Mentor (expanded emotional layer)'),(22,'Rebel','Questions authority, the rules, or the Hero’s mission, often forcing important change.','','2025-04-27 14:16:02.356562','2025-04-27 14:16:02.356562',1,'Trickster, Shapeshifter'),(23,'Sacrificial Lamb','Gives up something (often their life) to help the Hero succeed.','','2025-04-27 14:16:31.635922','2025-04-27 14:16:31.635922',1,'Ally (tragic form)'),(24,'Contagonist','A character who tempts or delays the Hero without being a villain (i.e., not the Shadow).','Contagonist (term from Dramatica theory)','2025-04-27 14:17:07.068209','2025-04-27 14:17:07.068209',1,'Temptress, Shapeshifter'),(25,'Moral Compass','Acts as the Hero’s ethical anchor, challenging them to do the right thing even when it’s hard.','','2025-04-27 14:17:33.137887','2025-04-27 14:17:33.137887',1,'Ally, Mentor');
/*!40000 ALTER TABLE `archetype_archetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Administrator');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40);
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
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add system',7,'add_system'),(26,'Can change system',7,'change_system'),(27,'Can delete system',7,'delete_system'),(28,'Can view system',7,'view_system'),(29,'Can add Image',8,'add_image'),(30,'Can change Image',8,'change_image'),(31,'Can delete Image',8,'delete_image'),(32,'Can view Image',8,'view_image'),(33,'Can add System Group',9,'add_systemgroup'),(34,'Can change System Group',9,'change_systemgroup'),(35,'Can delete System Group',9,'delete_systemgroup'),(36,'Can view System Group',9,'view_systemgroup'),(37,'Can add npc system',10,'add_npcsystem'),(38,'Can change npc system',10,'change_npcsystem'),(39,'Can delete npc system',10,'delete_npcsystem'),(40,'Can view npc system',10,'view_npcsystem'),(41,'Can add Character Group',11,'add_charactergroup'),(42,'Can change Character Group',11,'change_charactergroup'),(43,'Can delete Character Group',11,'delete_charactergroup'),(44,'Can view Character Group',11,'view_charactergroup'),(45,'Can add Character Sub Group',12,'add_charactersubgroup'),(46,'Can change Character Sub Group',12,'change_charactersubgroup'),(47,'Can delete Character Sub Group',12,'delete_charactersubgroup'),(48,'Can view Character Sub Group',12,'view_charactersubgroup'),(49,'Can add archetype',13,'add_archetype'),(50,'Can change archetype',13,'change_archetype'),(51,'Can delete archetype',13,'delete_archetype'),(52,'Can view archetype',13,'view_archetype'),(53,'Can add Genre',14,'add_genre'),(54,'Can change Genre',14,'change_genre'),(55,'Can delete Genre',14,'delete_genre'),(56,'Can view Genre',14,'view_genre'),(57,'Can add Character',15,'add_character'),(58,'Can change Character',15,'change_character'),(59,'Can delete Character',15,'delete_character'),(60,'Can view Character',15,'view_character'),(61,'Can add Character Image',16,'add_characterimage'),(62,'Can change Character Image',16,'change_characterimage'),(63,'Can delete Character Image',16,'delete_characterimage'),(64,'Can view Character Image',16,'view_characterimage'),(65,'Can add Race',17,'add_npcsystemrace'),(66,'Can change Race',17,'change_npcsystemrace'),(67,'Can delete Race',17,'delete_npcsystemrace'),(68,'Can view Race',17,'view_npcsystemrace'),(69,'Can add Class',18,'add_npcsystemrpgclass'),(70,'Can change Class',18,'change_npcsystemrpgclass'),(71,'Can delete Class',18,'delete_npcsystemrpgclass'),(72,'Can view Class',18,'view_npcsystemrpgclass'),(73,'Can add Profession',19,'add_npcsystemprofession'),(74,'Can change Profession',19,'change_npcsystemprofession'),(75,'Can delete Profession',19,'delete_npcsystemprofession'),(76,'Can view Profession',19,'view_npcsystemprofession'),(77,'Can add Table Group',20,'add_tablegroup'),(78,'Can change Table Group',20,'change_tablegroup'),(79,'Can delete Table Group',20,'delete_tablegroup'),(80,'Can view Table Group',20,'view_tablegroup'),(81,'Can add Table Header',21,'add_tableheader'),(82,'Can change Table Header',21,'change_tableheader'),(83,'Can delete Table Header',21,'delete_tableheader'),(84,'Can view Table Header',21,'view_tableheader'),(85,'Can add Table Item',22,'add_tableitem'),(86,'Can change Table Item',22,'change_tableitem'),(87,'Can delete Table Item',22,'delete_tableitem'),(88,'Can view Table Item',22,'view_tableitem'),(89,'Can add user',23,'add_user'),(90,'Can change user',23,'change_user'),(91,'Can delete user',23,'delete_user'),(92,'Can view user',23,'view_user');
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
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1000000$V7Lo4L6OIHDwwRNNaBeOw1$vxSs1P6K23/xFr3/8UHVACLUqCLVisI94bopTYVLEHs=','2025-04-26 15:46:04.764383',1,'admin','','','cmyers880@gmail.com',1,1,'2025-04-26 15:45:43.312090'),(2,'!qNfSqtmhlgsaWO2zL70fA6p2xyKMdwemS6QPqV42',NULL,1,'cmyers-ldap','Cash','Myers - LDAP','cmyers880@gmail.com',1,1,'2025-04-26 15:53:13.000000'),(3,'pbkdf2_sha256$1000000$EOKLf2WCYo4K1VcOolRTs4$IsPB9aZrPtvQGk2hHp2xYTdXvOst+IRKjrjO6v+YPZ4=',NULL,1,'cmyers','Cash','Myers','cmyers880@gmail.com',1,1,'2025-04-26 15:53:27.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (29,2,1),(30,2,2),(31,2,3),(32,2,4),(33,2,5),(34,2,6),(35,2,7),(36,2,8),(37,2,9),(38,2,10),(39,2,11),(40,2,12),(41,2,13),(42,2,14),(43,2,15),(44,2,16),(45,2,17),(46,2,18),(47,2,19),(48,2,20),(49,2,21),(50,2,22),(51,2,23),(52,2,24),(53,2,25),(54,2,26),(55,2,27),(56,2,28),(1,3,1),(2,3,2),(3,3,3),(4,3,4),(5,3,5),(6,3,6),(7,3,7),(8,3,8),(9,3,9),(10,3,10),(11,3,11),(12,3,12),(13,3,13),(14,3,14),(15,3,15),(16,3,16),(17,3,17),(18,3,18),(19,3,19),(20,3,20),(21,3,21),(22,3,22),(23,3,23),(24,3,24),(25,3,25),(26,3,26),(27,3,27),(28,3,28);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_group_charactergroup`
--

DROP TABLE IF EXISTS `character_group_charactergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_group_charactergroup` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `character_group_name` varchar(75) NOT NULL,
  `character_group_short_name` varchar(25) DEFAULT NULL,
  `description` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `npc_system_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `character_group_char_npc_system_id_bcf9f809_fk_npc_syste` (`npc_system_id`),
  CONSTRAINT `character_group_char_npc_system_id_bcf9f809_fk_npc_syste` FOREIGN KEY (`npc_system_id`) REFERENCES `npc_system_npcsystem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_group_charactergroup`
--

LOCK TABLES `character_group_charactergroup` WRITE;
/*!40000 ALTER TABLE `character_group_charactergroup` DISABLE KEYS */;
INSERT INTO `character_group_charactergroup` VALUES (1,'Big City Denizens','Big City Denizens','test','2025-04-26 21:57:44.485114','2025-04-26 22:03:20.268756',2),(2,'Small Town Tenants','Small Town Tenants','Test','2025-04-26 22:03:35.474683','2025-04-26 22:03:35.474683',2),(3,'Outskirts & Outposts','Outskirts & Outposts','Test','2025-04-26 22:03:50.859117','2025-04-26 22:03:59.010640',2),(4,'Underdwellers','Underdwellers','','2025-04-26 22:04:21.789707','2025-04-26 22:04:21.789707',2);
/*!40000 ALTER TABLE `character_group_charactergroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_images_characterimage`
--

DROP TABLE IF EXISTS `character_images_characterimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_images_characterimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `character_id` bigint NOT NULL,
  `image_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `character_images_cha_character_id_40bcfd76_fk_character` (`character_id`),
  KEY `character_images_cha_image_id_2ad2923a_fk_images_im` (`image_id`),
  CONSTRAINT `character_images_cha_character_id_40bcfd76_fk_character` FOREIGN KEY (`character_id`) REFERENCES `characters_character` (`id`),
  CONSTRAINT `character_images_cha_image_id_2ad2923a_fk_images_im` FOREIGN KEY (`image_id`) REFERENCES `images_image` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_images_characterimage`
--

LOCK TABLES `character_images_characterimage` WRITE;
/*!40000 ALTER TABLE `character_images_characterimage` DISABLE KEYS */;
INSERT INTO `character_images_characterimage` VALUES (1,'2025-04-27 19:35:42.924493','2025-04-27 19:35:42.924493',1,1);
/*!40000 ALTER TABLE `character_images_characterimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_sub_group_charactersubgroup`
--

DROP TABLE IF EXISTS `character_sub_group_charactersubgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_sub_group_charactersubgroup` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `character_sub_group_name` varchar(75) NOT NULL,
  `character_sub_group_short_name` varchar(25) DEFAULT NULL,
  `description` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `character_group_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `character_sub_group__character_group_id_fc979093_fk_character` (`character_group_id`),
  CONSTRAINT `character_sub_group__character_group_id_fc979093_fk_character` FOREIGN KEY (`character_group_id`) REFERENCES `character_group_charactergroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_sub_group_charactersubgroup`
--

LOCK TABLES `character_sub_group_charactersubgroup` WRITE;
/*!40000 ALTER TABLE `character_sub_group_charactersubgroup` DISABLE KEYS */;
INSERT INTO `character_sub_group_charactersubgroup` VALUES (1,'Common Folk','Common Folk','','2025-04-26 22:39:47.608757','2025-04-26 22:39:47.608757',1),(2,'Nobles & Leaders','Nobles & Leaders','','2025-04-26 22:40:03.576330','2025-04-26 22:40:03.576330',1),(3,'Lawkeepers & Lawbreakers','Lawkeepers & Lawbreakers','','2025-04-26 22:40:22.399073','2025-04-26 22:40:22.399073',1),(4,'Oddballs & Outskirts','Oddballs & Outskirts','','2025-04-26 22:40:34.331079','2025-04-26 22:40:34.331079',1),(5,'Common Folk','Common Folk','','2025-04-26 22:41:11.416725','2025-04-26 22:41:17.635329',2),(6,'Nobles & Leaders','Nobles & Leaders','','2025-04-26 22:41:29.800059','2025-04-26 22:41:29.800059',2),(7,'Lawkeepers & Lawbreakers','Lawkeepers & Lawbreakers','','2025-04-26 22:41:41.945818','2025-04-26 22:41:41.945818',2),(8,'Oddballs & Outskirts','Oddballs & Outskirts','','2025-04-26 22:41:56.265495','2025-04-26 22:41:56.265495',2),(9,'Common Folk','Common Folk','','2025-04-26 22:42:09.264071','2025-04-26 22:42:09.264071',3),(10,'Lawkeepers & Lawbreakders','Lawkeepers & Lawbreakders','','2025-04-26 22:42:22.219216','2025-04-26 22:42:22.219216',3),(11,'Oddballs & Outskirts','Oddballs & Outskirts','','2025-04-26 22:42:41.100901','2025-04-26 22:42:41.100901',3),(12,'Common Folk','Common Folk','','2025-04-26 22:42:54.852948','2025-04-26 22:42:54.852948',4),(13,'Nobles & Leaders','Nobles & Leaders','','2025-04-26 22:43:05.577877','2025-04-26 22:43:05.577877',4),(14,'Lawkeepers & Lawbreakers','Lawkeepers & Lawbreakers','','2025-04-26 22:43:20.904206','2025-04-26 22:43:20.904206',4),(15,'Oddballs & Outskirts','Oddballs & Outskirts','','2025-04-26 22:43:31.721637','2025-04-26 22:43:31.721637',4);
/*!40000 ALTER TABLE `character_sub_group_charactersubgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `characters_character`
--

DROP TABLE IF EXISTS `characters_character`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `characters_character` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `alias` varchar(100) DEFAULT NULL,
  `age_category_description` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `race` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `bulk_generated` tinyint(1) NOT NULL,
  `reviewed` tinyint(1) NOT NULL,
  `current_location` varchar(100) DEFAULT NULL,
  `description` longtext,
  `notes` longtext,
  `ai_integration_exists` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `archetype_id` bigint DEFAULT NULL,
  `character_group_id` bigint NOT NULL,
  `character_sub_group_id` bigint NOT NULL,
  `npc_system_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `characters_character_character_group_id_96290ca7_fk_character` (`character_group_id`),
  KEY `characters_character_character_sub_group__e76ca7a0_fk_character` (`character_sub_group_id`),
  KEY `characters_character_npc_system_id_a693c22d_fk_npc_syste` (`npc_system_id`),
  KEY `characters_character_archetype_id_6e8aa346_fk_archetype` (`archetype_id`),
  CONSTRAINT `characters_character_archetype_id_6e8aa346_fk_archetype` FOREIGN KEY (`archetype_id`) REFERENCES `archetype_archetype` (`id`),
  CONSTRAINT `characters_character_character_group_id_96290ca7_fk_character` FOREIGN KEY (`character_group_id`) REFERENCES `character_group_charactergroup` (`id`),
  CONSTRAINT `characters_character_character_sub_group__e76ca7a0_fk_character` FOREIGN KEY (`character_sub_group_id`) REFERENCES `character_sub_group_charactersubgroup` (`id`),
  CONSTRAINT `characters_character_npc_system_id_a693c22d_fk_npc_syste` FOREIGN KEY (`npc_system_id`) REFERENCES `npc_system_npcsystem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `characters_character`
--

LOCK TABLES `characters_character` WRITE;
/*!40000 ALTER TABLE `characters_character` DISABLE KEYS */;
INSERT INTO `characters_character` VALUES (1,'Farah','Noosecatcher',NULL,'an adult',NULL,'dragon-born','F',0,0,'City of Brassleague','','Brother is Hadley (Fraternal twin)',0,'2025-04-27 18:18:17.006874','2025-04-27 18:39:51.357774',NULL,1,1,2);
/*!40000 ALTER TABLE `characters_character` ENABLE KEYS */;
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
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=146 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-04-26 15:46:44.439752','1','Test System',1,'[{\"added\": {}}]',7,1),(2,'2025-04-26 15:53:13.887090','2','cmyers-ldap',1,'[{\"added\": {}}]',4,1),(3,'2025-04-26 15:53:28.590951','3','cmyers',1,'[{\"added\": {}}]',4,1),(4,'2025-04-26 15:54:20.534471','3','cmyers',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\", \"Superuser status\", \"User permissions\"]}}]',4,1),(5,'2025-04-26 15:54:52.232529','2','cmyers-ldap',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\", \"Superuser status\", \"User permissions\"]}}]',4,1),(6,'2025-04-26 16:08:28.942912','1','Test System',2,'[{\"changed\": {\"fields\": [\"Is global\"]}}]',7,1),(7,'2025-04-26 16:20:00.447555','2','General',1,'[{\"added\": {}}]',7,1),(8,'2025-04-26 21:29:01.801039','1','Test System',1,'[{\"added\": {}}]',10,1),(9,'2025-04-26 21:30:03.574189','1','Administrator',1,'[{\"added\": {}}]',3,1),(10,'2025-04-26 21:33:01.812458','2','GM Books',1,'[{\"added\": {}}]',10,1),(11,'2025-04-26 21:57:44.487116','1','GM Books - Big City Denize',1,'[{\"added\": {}}]',11,1),(12,'2025-04-26 21:59:17.152520','1','GM Books - Big City Denizens',2,'[{\"changed\": {\"fields\": [\"Character group short name\"]}}]',11,1),(13,'2025-04-26 22:03:20.270269','1','GM Books - Big City Denizens',2,'[]',11,1),(14,'2025-04-26 22:03:35.475677','2','GM Books - Small Town Tenants',1,'[{\"added\": {}}]',11,1),(15,'2025-04-26 22:03:50.860717','3','GM Books - Outskirts & Outposts',1,'[{\"added\": {}}]',11,1),(16,'2025-04-26 22:03:59.013144','3','GM Books - Outskirts & Outposts',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',11,1),(17,'2025-04-26 22:04:21.790714','4','GM Books - Underdwellers',1,'[{\"added\": {}}]',11,1),(18,'2025-04-26 22:39:47.611757','1','GM Books / Big City Denizens / Common Folk',1,'[{\"added\": {}}]',12,1),(19,'2025-04-26 22:40:03.579332','2','GM Books / Big City Denizens / Nobles & Leaders',1,'[{\"added\": {}}]',12,1),(20,'2025-04-26 22:40:22.401070','3','GM Books / Big City Denizens / Lawkeepers & Lawbreakers',1,'[{\"added\": {}}]',12,1),(21,'2025-04-26 22:40:34.333078','4','GM Books / Big City Denizens / Oddballs & Outskirts',1,'[{\"added\": {}}]',12,1),(22,'2025-04-26 22:41:11.418719','5','GM Books / Small Town Tenants / Common Folk',1,'[{\"added\": {}}]',12,1),(23,'2025-04-26 22:41:17.637329','5','GM Books / Small Town Tenants / Common Folk',2,'[]',12,1),(24,'2025-04-26 22:41:29.802567','6','GM Books / Small Town Tenants / Nobles & Leaders',1,'[{\"added\": {}}]',12,1),(25,'2025-04-26 22:41:41.948007','7','GM Books / Small Town Tenants / Lawkeepers & Lawbreakers',1,'[{\"added\": {}}]',12,1),(26,'2025-04-26 22:41:56.267502','8','GM Books / Small Town Tenants / Oddballs & Outskirts',1,'[{\"added\": {}}]',12,1),(27,'2025-04-26 22:42:09.267079','9','GM Books / Outskirts & Outposts / Common Folk',1,'[{\"added\": {}}]',12,1),(28,'2025-04-26 22:42:22.221722','10','GM Books / Outskirts & Outposts / Lawkeepers & Lawbreakders',1,'[{\"added\": {}}]',12,1),(29,'2025-04-26 22:42:41.103415','11','GM Books / Outskirts & Outposts / Oddballs & Outskirts',1,'[{\"added\": {}}]',12,1),(30,'2025-04-26 22:42:54.854941','12','GM Books / Underdwellers / Common Folk',1,'[{\"added\": {}}]',12,1),(31,'2025-04-26 22:43:05.580391','13','GM Books / Underdwellers / Nobles & Leaders',1,'[{\"added\": {}}]',12,1),(32,'2025-04-26 22:43:20.906205','14','GM Books / Underdwellers / Lawkeepers & Lawbreakers',1,'[{\"added\": {}}]',12,1),(33,'2025-04-26 22:43:31.723152','15','GM Books / Underdwellers / Oddballs & Outskirts',1,'[{\"added\": {}}]',12,1),(34,'2025-04-27 13:50:16.157570','1','Hero',1,'[{\"added\": {}}]',13,1),(35,'2025-04-27 13:50:34.028135','2','Mentor',1,'[{\"added\": {}}]',13,1),(36,'2025-04-27 13:50:52.604638','3','Threshold Guardian',1,'[{\"added\": {}}]',13,1),(37,'2025-04-27 13:51:06.819140','4','Herald',1,'[{\"added\": {}}]',13,1),(38,'2025-04-27 13:51:19.690466','5','Shapeshifter',1,'[{\"added\": {}}]',13,1),(39,'2025-04-27 13:51:30.974103','6','Shadow',1,'[{\"added\": {}}]',13,1),(40,'2025-04-27 13:51:43.799874','7','Trickster',1,'[{\"added\": {}}]',13,1),(41,'2025-04-27 13:51:59.530419','8','Ally',1,'[{\"added\": {}}]',13,1),(42,'2025-04-27 13:52:19.876213','9','Temptress (or Temptation)',1,'[{\"added\": {}}]',13,1),(43,'2025-04-27 13:52:54.087723','10','Father Figure',1,'[{\"added\": {}}]',13,1),(44,'2025-04-27 13:53:28.828855','9','Temptor/Temptress',2,'[{\"changed\": {\"fields\": [\"Name\", \"Description\"]}}]',13,1),(45,'2025-04-27 13:57:53.477001','8','Ally/Sidekick',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',13,1),(46,'2025-04-27 14:08:42.544458','11','Protector',1,'[{\"added\": {}}]',13,1),(47,'2025-04-27 14:09:07.398517','12','Mirror',1,'[{\"added\": {}}]',13,1),(48,'2025-04-27 14:12:41.721865','13','Secondary Hero',1,'[{\"added\": {}}]',13,1),(49,'2025-04-27 14:13:11.769653','14','Guardian of the Soul',1,'[{\"added\": {}}]',13,1),(50,'2025-04-27 14:13:36.808409','15','Comic Relief',1,'[{\"added\": {}}]',13,1),(51,'2025-04-27 14:13:55.996686','16','Love Interest',1,'[{\"added\": {}}]',13,1),(52,'2025-04-27 14:14:15.897559','17','False Mentor',1,'[{\"added\": {}}]',13,1),(53,'2025-04-27 14:14:38.339422','18','Shadow Ally',1,'[{\"added\": {}}]',13,1),(54,'2025-04-27 14:14:54.077649','19','Wise Fool',1,'[{\"added\": {}}]',13,1),(55,'2025-04-27 14:15:18.267019','20','Threshold Companion',1,'[{\"added\": {}}]',13,1),(56,'2025-04-27 14:15:39.224957','21','Wounded Healer',1,'[{\"added\": {}}]',13,1),(57,'2025-04-27 14:16:02.357627','22','Rebel',1,'[{\"added\": {}}]',13,1),(58,'2025-04-27 14:16:31.637922','23','Sacrificial Lamb',1,'[{\"added\": {}}]',13,1),(59,'2025-04-27 14:17:07.069211','24','Contagonist',1,'[{\"added\": {}}]',13,1),(60,'2025-04-27 14:17:33.138887','25','Moral Compass',1,'[{\"added\": {}}]',13,1),(61,'2025-04-27 16:25:31.877951','1','Fantasy',1,'[{\"added\": {}}]',14,1),(62,'2025-04-27 16:25:46.340201','2','GM Books',2,'[{\"changed\": {\"fields\": [\"Genre\"]}}]',10,1),(63,'2025-04-27 16:25:57.083686','1','Test System',2,'[{\"changed\": {\"fields\": [\"Genre\"]}}]',10,1),(64,'2025-04-27 16:26:29.697548','2','Science Fiction',1,'[{\"added\": {}}]',14,1),(65,'2025-04-27 16:26:42.927077','3','Horror',1,'[{\"added\": {}}]',14,1),(66,'2025-04-27 16:26:57.314893','4','Mystery / Detective',1,'[{\"added\": {}}]',14,1),(67,'2025-04-27 16:27:11.265166','5','Adventure / Action',1,'[{\"added\": {}}]',14,1),(68,'2025-04-27 16:27:27.058598','6','Post-Apocalyptic',1,'[{\"added\": {}}]',14,1),(69,'2025-04-27 16:27:43.802759','7','Historical Fiction',1,'[{\"added\": {}}]',14,1),(70,'2025-04-27 16:27:58.089903','8','Superhero',1,'[{\"added\": {}}]',14,1),(71,'2025-04-27 16:28:11.104618','9','Mythological / Epic',1,'[{\"added\": {}}]',14,1),(72,'2025-04-27 16:28:24.358536','10','Romance',1,'[{\"added\": {}}]',14,1),(73,'2025-04-27 16:28:37.642193','11','Comedy / Parody',1,'[{\"added\": {}}]',14,1),(74,'2025-04-27 16:28:50.842038','12','Dark Fantasy',1,'[{\"added\": {}}]',14,1),(75,'2025-04-27 16:29:04.984193','13','Urban Fantasy',1,'[{\"added\": {}}]',14,1),(76,'2025-04-27 16:29:40.453794','14','Military / Wargame',1,'[{\"added\": {}}]',14,1),(77,'2025-04-27 16:29:59.624480','15','Steampunk / Gaslamp Fantasy',1,'[{\"added\": {}}]',14,1),(78,'2025-04-27 16:59:46.212749','3','MVC',1,'[{\"added\": {}}]',10,1),(79,'2025-04-27 17:04:12.444117','3','MVC',2,'[{\"changed\": {\"fields\": [\"Genre\"]}}]',10,1),(80,'2025-04-27 17:25:45.311523','3','MVC',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',10,1),(81,'2025-04-27 17:27:13.154365','3','MVC',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',10,1),(82,'2025-04-27 18:18:17.010372','1','Character object (1)',1,'[{\"added\": {}}]',15,1),(83,'2025-04-27 18:27:34.073137','1','Character object (1)',2,'[]',15,1),(84,'2025-04-27 18:39:44.160305','1','Farah Noosecatcher',2,'[{\"changed\": {\"fields\": [\"Archetype\"]}}]',15,1),(85,'2025-04-27 18:39:51.358774','1','Farah Noosecatcher',2,'[]',15,1),(86,'2025-04-27 19:26:08.705676','1','Cash Myers',1,'[{\"added\": {}}]',8,1),(87,'2025-04-27 19:35:42.925490','1','Farah Noosecatcher (dragon-born) - Cash_profile_2a',1,'[{\"added\": {}}]',16,1),(88,'2025-04-27 19:59:56.666170','3','MVC',2,'[{\"changed\": {\"fields\": [\"Race table header\"]}}]',10,1),(89,'2025-04-27 20:00:04.576666','2','GM Books',2,'[]',10,1),(90,'2025-04-27 20:00:08.105499','1','Test System',2,'[]',10,1),(91,'2025-04-27 21:01:14.955335','1','GM Books - Race: Human',1,'[{\"added\": {}}]',17,1),(92,'2025-04-27 21:01:23.641260','1','GM Books - Race: Human',2,'[]',17,1),(93,'2025-04-27 21:11:51.029452','2','GM Books - Race: Dwarf',1,'[{\"added\": {}}]',17,1),(94,'2025-04-27 21:16:55.373420','3','GM Books - Race: HalfElf',1,'[{\"added\": {}}]',17,1),(95,'2025-04-27 21:18:47.616515','3','GM Books - Race: HalfElf',2,'[]',17,1),(96,'2025-04-27 21:19:21.752937','3','GM Books - Race: HalfElf',2,'[{\"changed\": {\"fields\": [\"Race id\"]}}]',17,1),(97,'2025-04-27 21:19:27.966616','3','GM Books - Race: Half Elf',2,'[{\"changed\": {\"fields\": [\"Value\"]}}]',17,1),(98,'2025-04-27 21:24:00.118087','1','GM Books - Race: dwarf',2,'[{\"changed\": {\"fields\": [\"Value\"]}}]',17,1),(99,'2025-04-27 21:24:14.747247','2','GM Books - Race: dragon-born',2,'[{\"changed\": {\"fields\": [\"Value\"]}}]',17,1),(100,'2025-04-27 21:24:26.410611','3','GM Books - Race: elf',2,'[{\"changed\": {\"fields\": [\"Value\"]}}]',17,1),(101,'2025-04-27 21:24:36.874894','4','GM Books - Race: half-elf',1,'[{\"added\": {}}]',17,1),(102,'2025-04-27 21:24:44.842625','5','GM Books - Race: half-orc',1,'[{\"added\": {}}]',17,1),(103,'2025-04-27 21:24:55.226563','6','GM Books - Race: halfling',1,'[{\"added\": {}}]',17,1),(104,'2025-04-27 21:25:03.096150','7','GM Books - Race: human',1,'[{\"added\": {}}]',17,1),(105,'2025-04-27 21:25:10.265354','8','GM Books - Race: monstrous race',1,'[{\"added\": {}}]',17,1),(106,'2025-04-27 21:25:17.356264','9','GM Books - Race: tiefling',1,'[{\"added\": {}}]',17,1),(107,'2025-04-27 21:25:26.884086','10','MVC - Clan: Vampire Clan 1',1,'[{\"added\": {}}]',17,1),(108,'2025-04-27 21:57:24.403773','1','GM Books - RPG Class: Fighter',1,'[{\"added\": {}}]',18,1),(109,'2025-04-27 21:57:31.885128','2','GM Books - RPG Class: Fighter',1,'[{\"added\": {}}]',18,1),(110,'2025-04-27 21:57:49.600255','2','GM Books - RPG Class: Magic-user',2,'[{\"changed\": {\"fields\": [\"Value\"]}}]',18,1),(111,'2025-04-27 22:07:22.093639','1','GM Books - Profession: Blacksmith',1,'[{\"added\": {}}]',19,1),(112,'2025-04-27 22:07:29.425856','2','GM Books - Profession: Innkeeper',1,'[{\"added\": {}}]',19,1),(113,'2025-04-28 00:22:45.887161','2','Concept Builder',1,'[{\"added\": {}}]',20,1),(114,'2025-04-28 00:22:58.162763','2','Concept Builder',2,'[]',20,1),(115,'2025-04-28 00:23:51.018772','3','Pivotal Event',1,'[{\"added\": {}}]',20,1),(116,'2025-04-28 00:25:17.447439','4','Habits',1,'[{\"added\": {}}]',20,1),(117,'2025-04-28 00:25:52.666283','5','Signposts',1,'[{\"added\": {}}]',20,1),(118,'2025-04-28 00:25:58.163392','4','Habits',2,'[{\"changed\": {\"fields\": [\"Number of rolls\"]}}]',20,1),(119,'2025-04-28 00:40:55.128166','2','Concept Builder',2,'[]',20,1),(120,'2025-04-28 00:41:02.753182','6','test',1,'[{\"added\": {}}]',20,1),(121,'2025-04-28 00:41:15.153930','6','test',3,'',20,1),(122,'2025-04-28 00:52:43.815139','1','Concept Builder Adjective',1,'[{\"added\": {}}]',21,1),(123,'2025-04-28 00:53:39.982433','2','Concept Builder Identity/Roll',1,'[{\"added\": {}}]',21,1),(124,'2025-04-28 00:54:20.478587','3','Concept Builder Characteristic',1,'[{\"added\": {}}]',21,1),(125,'2025-04-28 01:29:50.674906','1','MVC - Concept Builder Identity/Roll [0] (Item 1) - Depressed',1,'[{\"added\": {}}]',22,1),(126,'2025-04-28 01:30:03.855799','2','MVC - Concept Builder Adjective [0] (Item 1) - Surly',1,'[{\"added\": {}}]',22,1),(127,'2025-04-28 01:30:41.987508','1','MVC - Concept Builder Identity/Roll [0] (Item 1) - Depressed',3,'',22,1),(128,'2025-04-28 01:30:52.914592','3','MVC - Concept Builder Adjective [0] (Item 2) - Surly',1,'[{\"added\": {}}]',22,1),(129,'2025-04-28 01:31:10.040325','2','MVC - Concept Builder Adjective [0] (Item 1) - Surly',3,'',22,1),(130,'2025-04-28 01:31:10.040325','3','MVC - Concept Builder Adjective [0] (Item 2) - Surly',3,'',22,1),(131,'2025-04-28 01:31:24.012699','4','MVC - Concept Builder Adjective [0] (Item 1) - Depressed',1,'[{\"added\": {}}]',22,1),(132,'2025-04-28 01:31:33.904554','5','MVC - Concept Builder Adjective [0] (Item 2) - Surly',1,'[{\"added\": {}}]',22,1),(133,'2025-04-28 01:31:53.792652','6','MVC - Concept Builder Adjective [0] (Item 3) - Straightforward',1,'[{\"added\": {}}]',22,1),(134,'2025-04-28 01:32:20.262233','7','MVC - Concept Builder Identity/Roll [0] (Item 1) - Cop / Detective',1,'[{\"added\": {}}]',22,1),(135,'2025-04-28 01:32:31.705979','8','MVC - Concept Builder Identity/Roll [0] (Item 2) - Social Worker / Activist',1,'[{\"added\": {}}]',22,1),(136,'2025-04-28 01:32:40.533966','9','MVC - Concept Builder Identity/Roll [0] (Item 3) - Doctor / Nurse / EMT',1,'[{\"added\": {}}]',22,1),(137,'2025-04-28 01:37:15.632083','10','MVC - Concept Builder Characteristic [0] (Item 1) - Imprisoned (Wrongfully ?)',1,'[{\"added\": {}}]',22,1),(138,'2025-04-28 01:40:16.577721','4','MVC - Concept Builder Adjective  (Item 1) - Depressed',2,'[]',22,1),(139,'2025-04-28 01:40:39.158482','11','MVC - Concept Builder Adjective  (Item 4) - Timid',1,'[{\"added\": {}}]',22,1),(140,'2025-04-28 01:40:49.831824','12','MVC - Concept Builder Adjective  (Item 5) - Clever',1,'[{\"added\": {}}]',22,1),(141,'2025-04-28 01:40:59.824293','13','MVC - Concept Builder Adjective  (Item 6) - Bold',1,'[{\"added\": {}}]',22,1),(142,'2025-04-28 01:41:10.360397','14','MVC - Concept Builder Adjective  (Item 7) - Inquisitive',1,'[{\"added\": {}}]',22,1),(143,'2025-04-28 01:41:24.923145','15','MVC - Concept Builder Adjective  (Item 8) - Circumspect',1,'[{\"added\": {}}]',22,1),(144,'2025-04-28 01:41:35.341566','16','MVC - Concept Builder Adjective  (Item 9) - Outgoing',1,'[{\"added\": {}}]',22,1),(145,'2025-04-28 01:41:48.132931','17','MVC - Concept Builder Adjective  (Item 10) - Optimistic',1,'[{\"added\": {}}]',22,1);
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(13,'archetype','archetype'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(11,'character_group','charactergroup'),(16,'character_images','characterimage'),(12,'character_sub_group','charactersubgroup'),(15,'characters','character'),(5,'contenttypes','contenttype'),(14,'genre','genre'),(8,'images','image'),(10,'npc_system','npcsystem'),(19,'npc_system_professions','npcsystemprofession'),(17,'npc_system_races','npcsystemrace'),(18,'npc_system_rpg_classes','npcsystemrpgclass'),(6,'sessions','session'),(7,'system','system'),(9,'system_group','systemgroup'),(20,'table_group','tablegroup'),(21,'table_header','tableheader'),(22,'table_items','tableitem'),(23,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (18,'sessions','0001_initial','2025-04-26 15:15:15.152998'),(19,'system','0001_initial','2025-04-26 15:43:47.335739'),(20,'system','0002_system_is_global_system_owner','2025-04-26 16:08:07.657286'),(21,'images','0001_initial','2025-04-26 19:28:03.715361'),(22,'images','0002_image_image','2025-04-26 19:30:26.294907'),(23,'images','0003_image_alt_text','2025-04-26 19:38:09.182428'),(24,'images','0004_alter_image_owner_alter_image_thumbnail','2025-04-26 19:45:19.774995'),(25,'images','0005_remove_image_file_url','2025-04-26 19:50:26.856359'),(26,'system_group','0001_initial','2025-04-26 20:51:27.679485'),(27,'npc_system','0001_initial','2025-04-26 21:26:00.925022'),(28,'character_group','0001_initial','2025-04-26 21:53:20.379615'),(29,'character_group','0002_alter_charactergroup_character_group_name_and_more','2025-04-26 21:59:07.483595'),(30,'character_group','0003_alter_charactergroup_options','2025-04-26 22:39:06.948944'),(31,'character_sub_group','0001_initial','2025-04-26 22:39:07.058124'),(32,'archetype','0001_initial','2025-04-27 13:48:48.888063'),(33,'archetype','0002_alter_archetype_options_archetype_expansion_and_more','2025-04-27 14:07:56.370335'),(34,'archetype','0003_alter_archetype_options','2025-04-27 16:08:37.894231'),(35,'genre','0001_initial','2025-04-27 16:08:37.931838'),(36,'npc_system','0002_npcsystem_genre','2025-04-27 16:08:37.979311'),(37,'characters','0001_initial','2025-04-27 18:15:28.337676'),(38,'characters','0002_alter_character_archetype','2025-04-27 18:39:35.434146'),(39,'character_images','0001_initial','2025-04-27 19:35:19.755551'),(40,'npc_system','0003_npcsystem_profession_table_header_and_more','2025-04-27 19:59:25.637534'),(41,'npc_system','0004_alter_npcsystem_profession_table_header_and_more','2025-04-27 20:58:43.028225'),(42,'npc_system_races','0001_initial','2025-04-27 20:58:43.145735'),(43,'npc_system_races','0002_alter_npcsystemrace_race_id','2025-04-27 21:14:22.272664'),(44,'npc_system_rpg_classes','0001_initial','2025-04-27 21:56:41.691068'),(45,'npc_system_professions','0001_initial','2025-04-27 22:07:00.672399'),(46,'table_group','0001_initial','2025-04-28 00:17:38.228569'),(47,'table_group','0002_alter_tablegroup_number_of_rolls','2025-04-28 00:39:33.213574'),(48,'table_header','0001_initial','2025-04-28 00:50:50.753031'),(49,'table_items','0001_initial','2025-04-28 01:28:50.405102'),(50,'table_items','0002_alter_tableitem_options_and_more','2025-04-28 01:38:43.849985'),(51,'npc_system_races','0003_alter_npcsystemrace_race_id','2025-04-28 13:04:54.009463'),(52,'npc_system_professions','0002_alter_npcsystemprofession_profession_id','2025-04-28 13:09:41.274507'),(53,'npc_system_rpg_classes','0002_alter_npcsystemrpgclass_rpg_class_id','2025-04-28 13:13:59.395205');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('t8u2ql0228fljdrzzcwvzayhb148pggq','.eJxVjMsOwiAURP-FtSHQAi0u3fsN5L6wVQNJHyvjvytJF7qbzDkzL5Vg36a0r7KkmdVZWXX67RDoIaUBvkO5VU21bMuMuin6oKu-Vpbn5XD_DiZYp7Z2XqLzeWRPllDIhH6IzOEbYpeNG6jvKLgQED0MPGYEyQassbGTGNX7A_LQODw:1u8hjA:wARKmq-w3lH2I_wfEo1Sz46rATtuhDeV1E9KaFcr81I','2025-05-10 15:46:04.768894');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre_genre`
--

DROP TABLE IF EXISTS `genre_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre_genre` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `notes` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre_genre`
--

LOCK TABLES `genre_genre` WRITE;
/*!40000 ALTER TABLE `genre_genre` DISABLE KEYS */;
INSERT INTO `genre_genre` VALUES (1,'Fantasy','Magic, mythical creatures, imaginary worlds.','Most popular RPG genre (e.g., D&D, Pathfinder)','2025-04-27 16:25:31.876433','2025-04-27 16:25:31.876433'),(2,'Science Fiction','Advanced tech, space travel, future worlds.','Space opera, cyberpunk RPGs (e.g., Starfinder, Shadowrun)','2025-04-27 16:26:29.695548','2025-04-27 16:26:29.695548'),(3,'Horror','Fear, suspense, supernatural threats.','Emphasizes survival and atmosphere (e.g., Call of Cthulhu)','2025-04-27 16:26:42.924570','2025-04-27 16:26:42.924570'),(4,'Mystery / Detective','Solving crimes, uncovering secrets.','Puzzle-driven RPGs or mystery modules (e.g., Gumshoe system)','2025-04-27 16:26:57.313892','2025-04-27 16:26:57.313892'),(5,'Adventure / Action','Quests, exploration, constant physical challenges.','Core to almost all RPGs as an activity loop','2025-04-27 16:27:11.263151','2025-04-27 16:27:11.263151'),(6,'Post-Apocalyptic','After the fall of civilization; survival themes.','Fallout RPG, Mutant: Year Zero','2025-04-27 16:27:27.057599','2025-04-27 16:27:27.057599'),(7,'Historical Fiction','Real historical periods, sometimes with light fantasy.','Vampire: The Dark Ages, Warhammer (Old World)','2025-04-27 16:27:43.800251','2025-04-27 16:27:43.800251'),(8,'Superhero','Heroes with superpowers facing grand-scale threats.','Masks: A New Generation, Mutants & Masterminds','2025-04-27 16:27:58.088852','2025-04-27 16:27:58.088852'),(9,'Mythological / Epic','Gods, ancient heroes, legendary struggles.','Highly tied to classic myths (e.g., Scion RPG)','2025-04-27 16:28:11.102506','2025-04-27 16:28:11.102506'),(10,'Romance','Emotional, relationship-focused stories.','Rare in classic RPGs, but growing (e.g., Thirsty Sword Lesbians)','2025-04-27 16:28:24.357540','2025-04-27 16:28:24.357540'),(11,'Comedy / Parody','Satirical, humorous tone and absurd scenarios.','Paranoia RPG, Toon RPG','2025-04-27 16:28:37.641109','2025-04-27 16:28:37.641109'),(12,'Dark Fantasy','Grim, violent, and morally gray fantasy worlds.','Warhammer Fantasy, Blades in the Dark','2025-04-27 16:28:50.840038','2025-04-27 16:28:50.840038'),(13,'Urban Fantasy','Magic hidden within the modern world.','World of Darkness, Dresden Files RPG','2025-04-27 16:29:04.983192','2025-04-27 16:29:04.983192'),(14,'Military / Wargame','Strategy, tactics, battlefield conflicts.','Warhammer 40k RPGs, Twilight 2000','2025-04-27 16:29:40.451780','2025-04-27 16:29:40.451780'),(15,'Steampunk / Gaslamp Fantasy','Victorian-era tech with magic/science blend.','Iron Kingdoms, Victoriana RPG','2025-04-27 16:29:59.622883','2025-04-27 16:29:59.622883');
/*!40000 ALTER TABLE `genre_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images_image`
--

DROP TABLE IF EXISTS `images_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images_image` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `file_name` varchar(255) NOT NULL,
  `file_size` int unsigned NOT NULL,
  `mime_type` varchar(25) NOT NULL,
  `image_type` varchar(1) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `owner_id` int DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `alt_text` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `images_image_owner_id_d47da4d9_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `images_image_owner_id_d47da4d9_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `images_image_chk_1` CHECK ((`file_size` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images_image`
--

LOCK TABLES `images_image` WRITE;
/*!40000 ALTER TABLE `images_image` DISABLE KEYS */;
INSERT INTO `images_image` VALUES (1,'Cash_profile_2a',471040,'image/jpg','i','','2025-04-27 19:26:08.702358','2025-04-27 19:26:08.702358',NULL,'images/Cash_profile_2a.jpg','Cash Myers');
/*!40000 ALTER TABLE `images_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `npc_system_npcsystem`
--

DROP TABLE IF EXISTS `npc_system_npcsystem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `npc_system_npcsystem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `npc_system_name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `standard_app_dsp` tinyint(1) NOT NULL,
  `is_global` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `owner_id` int DEFAULT NULL,
  `genre_id` varchar(25) DEFAULT NULL,
  `profession_table_header` varchar(25) NOT NULL,
  `race_table_header` varchar(25) NOT NULL,
  `rpg_class_table_header` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `npc_system_npcsystem_owner_id_b8c9f0aa_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `npc_system_npcsystem_owner_id_b8c9f0aa_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `npc_system_npcsystem`
--

LOCK TABLES `npc_system_npcsystem` WRITE;
/*!40000 ALTER TABLE `npc_system_npcsystem` DISABLE KEYS */;
INSERT INTO `npc_system_npcsystem` VALUES (1,'Test System','This is a generic random system generator.',1,1,'2025-04-26 21:29:01.800038','2025-04-27 20:00:08.103492',NULL,'1','Profession','Race','RPG Class'),(2,'GM Books','Based upon the Random NPC GM Book',1,1,'2025-04-26 21:33:01.809458','2025-04-27 20:00:04.575661',NULL,'1','Profession','Race','RPG Class'),(3,'MVC','Minimum Viable Character\r\nAdapted from a 2018 blog post by Jon Wake entitled \"Building a Compelling Character\", (https://jonwake.blogspot.com/2018/07/minimal-viable-character-for-vampire.html).\r\n\r\nThis sysem builds upon the following areas\r\n1) Basic Concept (3 tables) - 1x  Concept\r\n2) Pivotal Event (3 tables)  - 1x Event\r\n3) Habits (2 tables - 3 rolls) - 1-2 Habits \r\n4) Signposts (2 tables) - 2x Signposts',1,1,'2025-04-27 16:59:46.210746','2025-04-27 19:59:56.664562',NULL,'7','Profession','Clan','RPG Class');
/*!40000 ALTER TABLE `npc_system_npcsystem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `npc_system_professions_npcsystemprofession`
--

DROP TABLE IF EXISTS `npc_system_professions_npcsystemprofession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `npc_system_professions_npcsystemprofession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profession_id` int unsigned DEFAULT NULL,
  `value` varchar(25) NOT NULL,
  `npc_system_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `npc_system_professions_n_npc_system_id_id_8a17acf1_uniq` (`npc_system_id`,`id`),
  KEY `npc_system_professions_npcs_profession_id_94f36a9e` (`profession_id`),
  CONSTRAINT `npc_system_professio_npc_system_id_aa513e18_fk_npc_syste` FOREIGN KEY (`npc_system_id`) REFERENCES `npc_system_npcsystem` (`id`),
  CONSTRAINT `npc_system_professions_npcsystemprofession_chk_1` CHECK ((`profession_id` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `npc_system_professions_npcsystemprofession`
--

LOCK TABLES `npc_system_professions_npcsystemprofession` WRITE;
/*!40000 ALTER TABLE `npc_system_professions_npcsystemprofession` DISABLE KEYS */;
INSERT INTO `npc_system_professions_npcsystemprofession` VALUES (1,1,'Blacksmith',2),(2,2,'Innkeeper',2);
/*!40000 ALTER TABLE `npc_system_professions_npcsystemprofession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `npc_system_races_npcsystemrace`
--

DROP TABLE IF EXISTS `npc_system_races_npcsystemrace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `npc_system_races_npcsystemrace` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `race_id` int unsigned DEFAULT NULL,
  `value` varchar(25) NOT NULL,
  `npc_system_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `npc_system_races_npcsystemrace_npc_system_id_id_70289d1f_uniq` (`npc_system_id`,`id`),
  KEY `npc_system_races_npcsystemrace_race_id_58e186ac` (`race_id`),
  CONSTRAINT `npc_system_races_npc_npc_system_id_3733e8e1_fk_npc_syste` FOREIGN KEY (`npc_system_id`) REFERENCES `npc_system_npcsystem` (`id`),
  CONSTRAINT `npc_system_races_npcsystemrace_chk_1` CHECK ((`race_id` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `npc_system_races_npcsystemrace`
--

LOCK TABLES `npc_system_races_npcsystemrace` WRITE;
/*!40000 ALTER TABLE `npc_system_races_npcsystemrace` DISABLE KEYS */;
INSERT INTO `npc_system_races_npcsystemrace` VALUES (1,1,'dwarf',2),(2,2,'dragon-born',2),(3,3,'elf',2),(4,4,'half-elf',2),(5,5,'half-orc',2),(6,6,'halfling',2),(7,7,'human',2),(8,8,'monstrous race',2),(9,9,'tiefling',2),(10,1,'Vampire Clan 1',3);
/*!40000 ALTER TABLE `npc_system_races_npcsystemrace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `npc_system_rpg_classes_npcsystemrpgclass`
--

DROP TABLE IF EXISTS `npc_system_rpg_classes_npcsystemrpgclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `npc_system_rpg_classes_npcsystemrpgclass` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rpg_class_id` int unsigned DEFAULT NULL,
  `value` varchar(25) NOT NULL,
  `npc_system_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `npc_system_rpg_classes_n_npc_system_id_id_6c8ba88b_uniq` (`npc_system_id`,`id`),
  KEY `npc_system_rpg_classes_npcsystemrpgclass_rpg_class_id_f6153a56` (`rpg_class_id`),
  CONSTRAINT `npc_system_rpg_class_npc_system_id_89fa05aa_fk_npc_syste` FOREIGN KEY (`npc_system_id`) REFERENCES `npc_system_npcsystem` (`id`),
  CONSTRAINT `npc_system_rpg_classes_npcsystemrpgclass_chk_1` CHECK ((`rpg_class_id` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `npc_system_rpg_classes_npcsystemrpgclass`
--

LOCK TABLES `npc_system_rpg_classes_npcsystemrpgclass` WRITE;
/*!40000 ALTER TABLE `npc_system_rpg_classes_npcsystemrpgclass` DISABLE KEYS */;
INSERT INTO `npc_system_rpg_classes_npcsystemrpgclass` VALUES (1,1,'Fighter',2),(2,2,'Magic-user',2);
/*!40000 ALTER TABLE `npc_system_rpg_classes_npcsystemrpgclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles_profile`
--

DROP TABLE IF EXISTS `profiles_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profiles_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `avatar` varchar(100) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `bio` longtext NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles_profile`
--

LOCK TABLES `profiles_profile` WRITE;
/*!40000 ALTER TABLE `profiles_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `profiles_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table_group_tablegroup`
--

DROP TABLE IF EXISTS `table_group_tablegroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_group_tablegroup` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `report_display_heading` varchar(50) NOT NULL,
  `display_order` int unsigned NOT NULL,
  `number_of_rolls` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `npc_system_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_group_tablegroup_npc_system_id_name_44de73d7_uniq` (`npc_system_id`,`name`),
  CONSTRAINT `table_group_tablegro_npc_system_id_4c564a60_fk_npc_syste` FOREIGN KEY (`npc_system_id`) REFERENCES `npc_system_npcsystem` (`id`),
  CONSTRAINT `table_group_tablegroup_chk_1` CHECK ((`display_order` >= 0)),
  CONSTRAINT `table_group_tablegroup_chk_2` CHECK ((`number_of_rolls` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_group_tablegroup`
--

LOCK TABLES `table_group_tablegroup` WRITE;
/*!40000 ALTER TABLE `table_group_tablegroup` DISABLE KEYS */;
INSERT INTO `table_group_tablegroup` VALUES (2,'Concept Builder','The character concept tells you what your character does and how they do it. Most of us are pretty good and forming a concept.\r\nThere are three tables for this group\r\n1) A leading adjective\r\n2) A Identity/Role\r\n3) A quality','Character Concept',10,1,'2025-04-28 00:22:45.884021','2025-04-28 00:40:55.126166',3),(3,'Pivotal Event','Backstory can be a trap for players. Building a massively in-depth backstory for your character can be fun and informative, but when it comes to gaming and performance we need surprisingly little. The Pivotal Event covers just the moment that informs your performance the most. \r\n \r\nWhat we’re looking for with the Pivotal Event is unresolved emotion.  The event itself could be resolved- the criminal who stabbed you was arrested, the move across country went without a hitch- but the emotions this event provoked aren’t resolved. Creating a Pivotal Event has three parts.\r\n1) What Happened? \r\nTell us about a singular event or chain of events in your character’s life. It can be mundane but it should be enough to provoke a response from someone. It could be anything from seeing your family die in a car accident to getting fired from your job. What you choose tells us a lot about your character, so most any choice is valid.\r\n2) How did it make you feel?\r\nYou have an event in your history that made you feel some way, made you feel strongly some way. How did you feel? Describe in a couple words the feeling you had after the event, but don’t worry about it making perfectly logical sense. In fact, it’s better if the emotion is unexpected. What if after seeing your family die in a car accident you were filled with a feeling of overwhelming joy? As you try to cross that gap between the response and the event, you’ll learn what makes your character tick.\r\n3) Why can’t you let it go?\r\nThis is the reason why this emotion matters to your character at the table. If the emotion was resolved and the character was satisfied with how they grew and changed as a person, there is no drama or tension in the character. When the feeling persists, even long after  the cause has passed, it drives the character to act. It is important that the event itself doesn’t need to be ongoing, just the emotion. Something, sometimes external to your character, stepped in an arrested your development. \r\n \r\nWe don’t need to make more than one or at the most two events. If you’re playing Vampire, the Embrace is a giant event that you’re still learning how you feel about it. Knowing how past events affected you will inform your choices in the here and now.\r\n \r\nIf you’re stuck, try using the chart below. You’re not beholden to it, but it can clarify your choices. Roll 1d10 three times to generate an Event, Emotion, and Unresolved Reason','Pivotal Event',20,1,'2025-04-28 00:23:51.017729','2025-04-28 00:23:51.017729',3),(4,'Habits','Each personality tick you play at the table reveals something about the character. No matter how mundane it is, if the quirk illustrates a deeper experience, opinion, or story to the character, the audience will want to know more.  But just like with our Pivotal Event, we don’t want to create a character with a singular throughline to their personality. We want a character that can surprise us and the other players. \r\n \r\nWe do this by building Habits in opposed pairs. Both habits tell us something about a particular aspect of the character, but one of them establishes the aspect and the other undermines people’s expectations. For example, if we have a character born and raised in the deep Alabama South, we could decide that she’s never quite lost her country Alabama drawl. This establishes the character trait, and sets some expectations for the other players. Now we want to subvert those expectations. Perhaps our Southerner has an intense love for science and technology, and will bring up articles she read whenever she gets the chance. We’ve now created an element of tension in the audience’s perception of the character-- they have a set of assumptions about a country girl from the deep south, and we challenge those assumptions with her love of science.\r\n \r\nPick one or two character traits you want to illustrate with affect. It can be where the character was raised, what their profession is, who they associate with, or what their ambitions are. The important thing is that we look at how the character fits into society. Then we choose a Habit  that establishes the background trait, then another that undermines it.','Habits',30,1,'2025-04-28 00:25:17.445438','2025-04-28 00:25:58.161697',3),(5,'Signposts','You’ll notice that we’re focusing a lot on the emotions the character has, and there’s a good reason for it. A character without emotion is a flat, dull, lifeless character. One with all the charm in the world and no emotional resonance will strike people as a deranged psychopath. \r\n \r\nSignposts mark out clear reactions the character has towards events around them. They are by nature abstract and extreme, because we cannot control the events of the game and subtlety often gets lost at the table. We’re not expecting you to become a method actor, though, and each reaction has a more common emotion tied to it. Think of it as a roadmap-- not everyone can jump to Rage, but most of us know what irritation feels like and can depict that.\r\n \r\nWhen you’ve built out these reaction, don’t feel beholden to them forever. The goal is to give you a guidepost for your character, a true north to aim at. If you know your character is enraged by abuse of power, that tells you a lot about how she’s going to interact with authority figures. If the character feels desire for respect, this will also guide your character.','Signposts',40,2,'2025-04-28 00:25:52.664284','2025-04-28 00:25:52.664284',3);
/*!40000 ALTER TABLE `table_group_tablegroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table_header_tableheader`
--

DROP TABLE IF EXISTS `table_header_tableheader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_header_tableheader` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `report_display_heading` varchar(50) NOT NULL,
  `display_order` int unsigned NOT NULL,
  `number_of_rolls` int unsigned NOT NULL,
  `roll_die_type` varchar(50) NOT NULL,
  `roll_mod` int NOT NULL,
  `random_gen_inclusision_level` smallint unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `npc_system_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_header_tableheader_npc_system_id_name_2e50ceb1_uniq` (`npc_system_id`,`name`),
  CONSTRAINT `table_header_tablehe_npc_system_id_6d53be39_fk_npc_syste` FOREIGN KEY (`npc_system_id`) REFERENCES `npc_system_npcsystem` (`id`),
  CONSTRAINT `table_header_tableheader_chk_1` CHECK ((`display_order` >= 0)),
  CONSTRAINT `table_header_tableheader_chk_2` CHECK ((`number_of_rolls` >= 0)),
  CONSTRAINT `table_header_tableheader_chk_3` CHECK ((`random_gen_inclusision_level` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_header_tableheader`
--

LOCK TABLES `table_header_tableheader` WRITE;
/*!40000 ALTER TABLE `table_header_tableheader` DISABLE KEYS */;
INSERT INTO `table_header_tableheader` VALUES (1,'Concept Builder Adjective','','I\'m a',0,1,'d10',0,1,'2025-04-28 00:52:43.814138','2025-04-28 00:52:43.814138',3),(2,'Concept Builder Identity/Roll','','...',0,1,'d10',0,1,'2025-04-28 00:53:39.981427','2025-04-28 00:53:39.981427',3),(3,'Concept Builder Characteristic','','who was/is ...',0,1,'d10',0,1,'2025-04-28 00:54:20.477585','2025-04-28 00:54:20.477585',3);
/*!40000 ALTER TABLE `table_header_tableheader` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table_items_tableitem`
--

DROP TABLE IF EXISTS `table_items_tableitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_items_tableitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_id` int unsigned DEFAULT NULL,
  `value` longtext NOT NULL,
  `reroll_this_item` tinyint(1) NOT NULL,
  `description` longtext NOT NULL,
  `notes` longtext NOT NULL,
  `subsequent_table_roll` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `npc_system_id` bigint NOT NULL,
  `subsequent_table_id` bigint DEFAULT NULL,
  `table_header_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_items_tableitem_table_header_id_item_id_7f9d2bd8_uniq` (`table_header_id`,`item_id`),
  KEY `table_items_tableite_npc_system_id_b9fe954f_fk_npc_syste` (`npc_system_id`),
  KEY `table_items_tableite_subsequent_table_id_9e83b93d_fk_table_hea` (`subsequent_table_id`),
  KEY `table_items_tableitem_item_id_f55a4def` (`item_id`),
  CONSTRAINT `table_items_tableite_npc_system_id_b9fe954f_fk_npc_syste` FOREIGN KEY (`npc_system_id`) REFERENCES `npc_system_npcsystem` (`id`),
  CONSTRAINT `table_items_tableite_subsequent_table_id_9e83b93d_fk_table_hea` FOREIGN KEY (`subsequent_table_id`) REFERENCES `table_header_tableheader` (`id`),
  CONSTRAINT `table_items_tableite_table_header_id_d28e106d_fk_table_hea` FOREIGN KEY (`table_header_id`) REFERENCES `table_header_tableheader` (`id`),
  CONSTRAINT `table_items_tableitem_chk_1` CHECK ((`item_id` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_items_tableitem`
--

LOCK TABLES `table_items_tableitem` WRITE;
/*!40000 ALTER TABLE `table_items_tableitem` DISABLE KEYS */;
INSERT INTO `table_items_tableitem` VALUES (4,1,'Depressed',0,'','',0,'2025-04-28 01:31:24.010699','2025-04-28 01:40:16.575720',3,NULL,1),(5,2,'Surly',0,'','',0,'2025-04-28 01:31:33.903553','2025-04-28 01:31:33.903553',3,NULL,1),(6,3,'Straightforward',0,'','',0,'2025-04-28 01:31:53.790642','2025-04-28 01:31:53.790642',3,NULL,1),(7,1,'Cop / Detective',0,'','',0,'2025-04-28 01:32:20.261232','2025-04-28 01:32:20.261232',3,NULL,2),(8,2,'Social Worker / Activist',0,'','',0,'2025-04-28 01:32:31.703979','2025-04-28 01:32:31.703979',3,NULL,2),(9,3,'Doctor / Nurse / EMT',0,'','',0,'2025-04-28 01:32:40.532384','2025-04-28 01:32:40.532384',3,NULL,2),(10,1,'Imprisoned (Wrongfully ?)',0,'','',0,'2025-04-28 01:37:15.630085','2025-04-28 01:37:15.630085',3,NULL,3),(11,4,'Timid',0,'','',0,'2025-04-28 01:40:39.157481','2025-04-28 01:40:39.157481',3,NULL,1),(12,5,'Clever',0,'','',0,'2025-04-28 01:40:49.829709','2025-04-28 01:40:49.829709',3,NULL,1),(13,6,'Bold',0,'','',0,'2025-04-28 01:40:59.823291','2025-04-28 01:40:59.823291',3,NULL,1),(14,7,'Inquisitive',0,'','',0,'2025-04-28 01:41:10.359397','2025-04-28 01:41:10.359397',3,NULL,1),(15,8,'Circumspect',0,'','',0,'2025-04-28 01:41:24.921139','2025-04-28 01:41:24.921139',3,NULL,1),(16,9,'Outgoing',0,'','',0,'2025-04-28 01:41:35.340566','2025-04-28 01:41:35.340566',3,NULL,1),(17,10,'Optimistic',0,'','',0,'2025-04-28 01:41:48.131237','2025-04-28 01:41:48.131237',3,NULL,1);
/*!40000 ALTER TABLE `table_items_tableitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-28 16:40:34
