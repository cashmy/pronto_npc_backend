-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: pronto_npc_old
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-28 18:28:05
